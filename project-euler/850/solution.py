import math

def solve():
    MOD = 977676779
    N = 33557799775533
    mod2 = 2 * MOD; oh = (N+1)//2

    lim = int(N**0.5) + 1
    # Linear sieve for primes up to sqrt(N)
    lp = [0]*(lim+1); primes = []
    for i in range(2, lim+1):
        if lp[i] == 0: lp[i] = i; primes.append(i)
        for p in primes:
            if i*p > lim or p > lp[i]: break
            lp[i*p] = p
    pl = len(primes); prime_limit = 0
    while prime_limit < pl and primes[prime_limit]**2 <= N: prime_limit += 1

    def add_mod(a, b): return a+b-mod2 if a+b >= mod2 else a+b
    def mul_mod(a, b): return a*b % mod2

    def contribute(prd, rad, ps, es, max_e, phi_mod):
        Np = N // prd; K = max_e + 2; shift = K // 2
        base = (Np // rad) * (oh - shift)
        ret = base % mod2
        if ret < 0: ret += mod2
        for k in range(K - (K & 1) - 2, 0, -2):
            newr = 1; over = False
            for i in range(len(ps)):
                need = es[i] // k + 1
                for _ in range(need):
                    if newr > Np // ps[i]: over = True; break
                    newr *= ps[i]
                if over: break
            if over: break
            ret = (ret + Np // newr) % mod2
        return mul_mod(ret, phi_mod)

    def rec(ind, prd, rad, ps, es, max_e, phi_mod):
        ret = contribute(prd, rad, ps, es, max_e, phi_mod)
        for i in range(ind, prime_limit):
            p = primes[i]
            if prd > N // p or rad > N // p: break
            nxt_prd = prd * p; nxt_rad = rad * p
            prd_lim = N // nxt_rad
            if nxt_prd > prd_lim: break
            ps.append(p); es.append(-1)
            cur_prd = nxt_prd; phi_e = phi_mod
            while cur_prd <= prd_lim:
                e = es[-1] + 1; es[-1] = e
                if e == 0: phi_e = mul_mod(phi_mod, (p-1) % mod2)
                else: phi_e = mul_mod(phi_e, p % mod2)
                cm = max(max_e, e)
                ret = add_mod(ret, rec(i+1, cur_prd, nxt_rad, ps, es, cm, phi_e))
                if cur_prd > prd_lim // p: break
                cur_prd *= p
            ps.pop(); es.pop()
        return ret

    h_mod = contribute(1, 1, [], [], -1, 1)
    for i in range(prime_limit):
        p = primes[i]
        if p > N // p: continue
        prd_lim = N // p
        if p > prd_lim: continue
        ps = [p]; es = [-1]; cur_prd = p; phi_e = 1
        while cur_prd <= prd_lim:
            e = es[0] + 1; es[0] = e
            if e == 0: phi_e = (p-1) % mod2
            else: phi_e = mul_mod(phi_e, p % mod2)
            h_mod = add_mod(h_mod, rec(i+1, cur_prd, p, ps, es, e, phi_e))
            if cur_prd > prd_lim // p: break
            cur_prd *= p

    sum_n = N * (N+1) // 2 % mod2
    a_mod = (oh % mod2) * sum_n % mod2
    t_mod = (a_mod - h_mod + mod2) % mod2
    answer = (t_mod - (t_mod & 1)) // 2
    return str(answer % MOD)

if __name__ == '__main__':
    print(solve())
