def solve():
    MOD = 123456789
    N = 100000000

    def next_value(x, mod):
        y = x - 1 if x > 0 else mod - 1
        return (y * y % mod * y + 2) % mod

    # Cycle detection
    tort = next_value(1, MOD); hare = next_value(next_value(1, MOD), MOD)
    while tort != hare:
        tort = next_value(tort, MOD); hare = next_value(next_value(hare, MOD), MOD)
    mu = 0; tort = 1
    while tort != hare:
        tort = next_value(tort, MOD); hare = next_value(hare, MOD); mu += 1
    lam = 1; hare = next_value(tort, MOD)
    while tort != hare: hare = next_value(hare, MOD); lam += 1

    cs = mu + 1; need = cs + lam
    s_mod = [0]*(need+1); s_mod[1] = 1
    for i in range(2, need+1): s_mod[i] = next_value(s_mod[i-1], MOD)

    def val_idx(k):
        if k < cs: return s_mod[k]
        return s_mod[cs + (k - cs) % lam]

    # Euler phi summatory with memoization
    LIM = min(N, 1000000)
    phi = list(range(LIM+1))
    lp = [0]*(LIM+1); primes = []
    phi[1] = 1
    for i in range(2, LIM+1):
        if lp[i] == 0:
            lp[i] = i; primes.append(i); phi[i] = i - 1
        for p in primes:
            if i*p > LIM or p > lp[i]: break
            lp[i*p] = p
            phi[i*p] = phi[i] * p if i % p == 0 else phi[i] * (p - 1)
    prefix = [0]*(LIM+1)
    for i in range(1, LIM+1): prefix[i] = prefix[i-1] + phi[i]

    memo = {}
    def sum_phi(n):
        if n <= LIM: return prefix[n]
        if n in memo: return memo[n]
        ans = n * (n+1) // 2
        l = 2
        while l <= n:
            q = n // l; r = n // q
            ans -= (r-l+1) * sum_phi(q); l = r + 1
        memo[n] = ans; return ans

    # Groups
    groups = []; l = 1
    while l <= N:
        q = N // l; r = N // q; groups.append((l, r, q)); l = r + 1

    answer = 0; pref = 0; prev_pref = 0
    d = 1; s_d_lam = 1 % lam
    small_idx = [0, 1, 2, 3, 10]

    for gl, gr, gq in groups:
        while d <= gr:
            if d <= 4: ud = val_idx(small_idx[d])
            else:
                sm = cs % lam; delta = (s_d_lam + lam - sm) % lam
                ud = s_mod[cs + delta]
            pref = (pref + ud) % MOD
            s_d_lam = next_value(s_d_lam, lam)
            d += 1
        seg = (pref - prev_pref) % MOD
        sp = sum_phi(gq) % MOD
        cmod = (2 * sp + MOD - 1) % MOD
        answer = (answer + seg * cmod) % MOD
        prev_pref = pref

    return str(answer % MOD)

if __name__ == '__main__':
    print(solve())
