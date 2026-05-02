import math

def solve():
    # Factorize 43!
    n_fact = 43
    sieve = [True]*(n_fact+1); sieve[0] = sieve[1] = False
    for i in range(2, n_fact+1):
        if not sieve[i]: continue
        for j in range(i+i, n_fact+1, i): sieve[j] = False
    primes = []; exps = []
    for i in range(2, n_fact+1):
        if not sieve[i]: continue
        primes.append(i); e = 0; t = n_fact
        while t > 0: t //= i; e += t
        exps.append(e)

    pc = len(primes)
    log_p = [math.log(p) for p in primes]
    log_n = sum(e*lp for e, lp in zip(exps, log_p))
    rem_log = [0.0]*(pc+1)
    for i in range(pc-1, -1, -1): rem_log[i] = rem_log[i+1] + exps[i]*log_p[i]

    # Precompute powers
    pow_val = [[1]*(exps[i]+1) for i in range(pc)]
    for i in range(pc):
        for e in range(1, exps[i]+1): pow_val[i][e] = pow_val[i][e-1] * primes[i]

    n_value = 1
    for i in range(pc): n_value *= pow_val[i][exps[i]]

    # Splits sorted by balance
    splits_by = {}
    for e in range(max(exps)+1):
        sp = []
        for x in range(e+1):
            for y in range(e+1-x):
                z = e-x-y; sp.append((x,y,z))
        sp.sort(key=lambda s: (max(s)-min(s), abs(3*s[0]-e)+abs(3*s[1]-e)+abs(3*s[2]-e)))
        splits_by[e] = sp

    def lb_range(l1, l2, l3, rem):
        t = l2 - l1
        if rem <= t: mv = l1+rem
        else:
            rem -= t; need = 2*(l3-l2)
            mv = l2+rem/2 if rem <= need else l3
        return l3 - mv

    best_lr = [1e100]; best_sum = [0]; best_abc = [None]

    def update(bins):
        vals = sorted(1 if all(b[i]==0 for i in range(pc)) else
                      math.prod(pow_val[i][b[i]] for i in range(pc)) for b in bins)
        s = sum(vals)
        lr = math.log(vals[2]) - math.log(vals[0]) if vals[0] > 0 else 1e100
        if lr < best_lr[0] - 1e-18 or (abs(lr-best_lr[0]) < 1e-18 and (best_sum[0] == 0 or s < best_sum[0])):
            best_lr[0] = lr; best_sum[0] = s; best_abc[0] = vals[:]

    # Greedy seed
    logs = [0.0, 0.0, 0.0]; bins = [[0]*pc, [0]*pc, [0]*pc]
    desc = sorted(range(pc), key=lambda i: -primes[i])
    for pi in desc:
        for _ in range(exps[pi]):
            t = min(range(3), key=lambda j: logs[j])
            logs[t] += log_p[pi]; bins[t][pi] += 1
    # Sort
    order = sorted(range(3), key=lambda i: logs[i])
    logs = [logs[i] for i in order]; bins = [bins[i] for i in order]
    best_lr[0] = logs[2] - logs[0]; update(bins)

    # Phase A: DFS
    nodes = [0]; cap = 3000000
    def phase_a(idx, logs, bins):
        if nodes[0] >= cap: return
        nodes[0] += 1
        if idx == pc: update(bins); return
        if lb_range(logs[0], logs[1], logs[2], rem_log[idx]) >= best_lr[0] - 1e-18: return
        for s in splits_by[exps[idx]]:
            nl = [logs[j] + s[j]*log_p[idx] for j in range(3)]
            nb = [bins[j][:] for j in range(3)]
            for j in range(3): nb[j][idx] += s[j]
            order = sorted(range(3), key=lambda j: nl[j])
            nl = [nl[j] for j in order]; nb = [nb[j] for j in order]
            phase_a(idx+1, nl, nb)

    phase_a(0, [0.0,0.0,0.0], [[0]*pc,[0]*pc,[0]*pc])

    # Phase B: enumerate a
    cr = int(round(n_value ** (1/3)))
    while (cr+1)**3 <= n_value: cr += 1
    while cr**3 > n_value: cr -= 1
    a_high = cr

    def max_div_leq(residual, limit):
        best_b = [0]
        desc2 = sorted(range(pc), key=lambda i: -primes[i])
        rem_max = [1]*(pc+1)
        for i in range(pc-1, -1, -1):
            pi = desc2[i]; rem_max[i] = rem_max[i+1] * pow_val[pi][residual[pi]]
        def dfs(idx, cur):
            if cur > limit: return
            if idx == pc:
                if cur > best_b[0]: best_b[0] = cur; return
            else:
                if cur * rem_max[idx] <= best_b[0]: return
                pi = desc2[idx]; pw = pow_val[pi]
                lim = limit // cur; e = residual[pi]
                kmax = e
                while kmax > 0 and pw[kmax] > lim: kmax -= 1
                for k in range(kmax, -1, -1):
                    nxt = cur * pw[k]
                    if nxt * rem_max[idx+1] <= best_b[0]: break
                    dfs(idx+1, nxt)
        dfs(0, 1)
        return best_b[0]

    def isqrt_big(x):
        if x <= 0: return 0
        r = int(math.isqrt(x))
        while (r+1)*(r+1) <= x: r += 1
        while r*r > x: r -= 1
        return r

    def eval_cand(a, a_exp):
        qa = n_value // a
        u = isqrt_big(qa)
        res = [exps[i] - a_exp[i] for i in range(pc)]
        b = max_div_leq(res, u)
        if b < a: return
        c = qa // b
        if c < b: return
        la = math.log(a); lc = math.log(c)
        lr = lc - la
        if lr < best_lr[0] - 1e-18 or (abs(lr - best_lr[0]) < 1e-18 and a + b + c < best_sum[0]):
            best_lr[0] = lr; best_sum[0] = a + b + c; best_abc[0] = [a, b, c]

    # Lower bound for a
    base_log_low = (log_n - 2*best_lr[0]) / 3.0
    log_high = math.log(a_high)

    def phase_b(idx, cur, lv, a_exp):
        dyn_low = max(base_log_low, (log_n - 2*best_lr[0])/3.0)
        if idx == pc:
            if lv + 1e-18 >= dyn_low and cur <= a_high:
                eval_cand(cur, a_exp)
            return
        if lv > log_high + 1e-18: return
        if lv + rem_log[idx] < dyn_low - 1e-18: return
        mul = 1
        for k in range(exps[idx]+1):
            if cur > a_high // mul: break
            a_exp[idx] = k
            phase_b(idx+1, cur*mul, lv + k*log_p[idx], a_exp)
            if k < exps[idx]: mul *= primes[idx]
        a_exp[idx] = 0

    phase_b(0, 1, 0.0, [0]*pc)
    return str(best_sum[0])

if __name__ == '__main__':
    print(solve())
