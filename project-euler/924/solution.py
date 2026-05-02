def solve():
    MOD = 1000000007; TAIL_MOD = 100000000000; TAIL_CL = 15625000; N = 10000000000000000

    def am(x, y):
        x += y; return x - MOD if x >= MOD else x
    def sm(x, y): return x - y if x >= y else x + MOD - y
    def mm(x, y, m): return x * y % m
    def step(x, m): return (x * x + 2) % m

    def next_perm_u64(n):
        s = list(str(n)); i = len(s)-2
        while i >= 0 and s[i] >= s[i+1]: i -= 1
        if i < 0: return 0
        j = len(s)-1
        while s[j] <= s[i]: j -= 1
        s[i], s[j] = s[j], s[i]; s[i+1:] = s[i+1:][::-1]
        return int(''.join(s))

    def next_perm_delta_11(tail):
        d = []; x = tail
        for i in range(11): d.append(x % 10); x //= 10
        d.reverse()
        i = 9
        while i >= 0 and d[i] >= d[i+1]: i -= 1
        if i < 0: return False, 0
        j = 10
        while d[j] <= d[i]: j -= 1
        d[i], d[j] = d[j], d[i]; d[i+1:] = d[i+1:][::-1]
        nt = 0
        for dig in d: nt = nt*10 + dig
        return True, nt - tail

    # Build cycle for a mod MOD
    seen = {}; vals = [0]; x = 0; seen[x] = 0
    idx = 1
    while True:
        x = step(x, MOD)
        if x in seen: mu = seen[x]; lam = idx - mu; break
        seen[x] = idx; vals.append(x); idx += 1
    pref = [0]*(len(vals)+1)
    for i in range(len(vals)): pref[i+1] = am(pref[i], vals[i])

    def prefix_sum(n):
        if n + 1 <= len(vals): return pref[n+1]
        sm_val = pref[mu]; cs = sm(pref[mu+lam], pref[mu])
        rem = n - mu + 1; fc = rem // lam; r = rem % lam
        total = sm_val; total = am(total, mm(fc % MOD, cs, MOD))
        total = am(total, sm(pref[mu+r], pref[mu]))
        return total

    def range_sum(l, r):
        pr = prefix_sum(r); pl = prefix_sum(l-1) if l > 0 else 0
        return sm(pr, pl)

    # Small exact (n=1..5)
    ans = 0; a = 0
    for n in range(1, min(N, 5)+1):
        a = a*a + 2
        ans = am(ans, next_perm_u64(a) % MOD)

    if N >= 6:
        ans = am(ans, range_sum(6, N))  # sum of a_n mod MOD

    # Delta terms
    if N >= 6:
        a5t = 0
        for _ in range(5): a5t = step(a5t, TAIL_MOD)
        count = N - 5; cycle_sum = 0; tail = a5t
        for _ in range(TAIL_CL):
            tail = step(tail, TAIL_MOD)
            ok, delta = next_perm_delta_11(tail)
            cycle_sum = am(cycle_sum, delta % MOD)
        fc = count // TAIL_CL; r = count % TAIL_CL
        dt = mm(fc % MOD, cycle_sum, MOD)
        tail = a5t
        for _ in range(r):
            tail = step(tail, TAIL_MOD)
            ok, delta = next_perm_delta_11(tail)
            dt = am(dt, delta % MOD)
        ans = am(ans, dt)

    return str(ans)

if __name__ == '__main__':
    print(solve())
