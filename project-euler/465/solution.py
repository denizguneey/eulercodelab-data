def solve():
    MOD = 1000000007
    n = 7**13  # default_n

    def mm(a, b): return a * b % MOD

    def mod_pow(base, exp):
        base %= MOD; r = 1
        while exp > 0:
            if exp & 1: r = mm(r, base)
            base = mm(base, base); exp >>= 1
        return r

    # Phi summatory with memoization
    import math
    limit = min(n, max(1000000, int(n**(2/3))))
    limit = min(limit, 10000000)
    limit = max(1, min(limit, n))

    phi = list(range(limit + 1))
    primes = []
    for i in range(2, limit + 1):
        if phi[i] == i:
            primes.append(i); phi[i] = i - 1
        for p in primes:
            v = i * p
            if v > limit: break
            if i % p == 0: phi[v] = phi[i] * p; break
            phi[v] = phi[i] * (p - 1)

    prefix = [0] * (limit + 1)
    for i in range(1, limit + 1): prefix[i] = prefix[i-1] + phi[i]

    memo = {}
    def phi_sum(n):
        if n <= 0: return 0
        if n <= limit: return prefix[n]
        if n in memo: return memo[n]
        res = n * (n+1) // 2
        i = 2
        while i <= n:
            q = n // i; j = n // q
            res -= (j - i + 1) * phi_sum(q)
            i = j + 1
        memo[n] = res; return res

    # Build ranges
    ranges = []; r = 1
    while r <= n:
        q = n // r; R = n // q
        sp = phi_sum(R) - phi_sum(r - 1)
        cnt = sp * 4
        ranges.append((q, cnt, cnt % MOD))
        r = R + 1

    h, s1, s2 = 1, 0, 0
    for q, cnt, cm in ranges:
        h = mm(h, mod_pow(q + 1, cnt))
        qm = q % MOD; q2 = mm(qm, qm)
        s1 = (s1 + mm(cm, qm)) % MOD
        s2 = (s2 + mm(cm, q2)) % MOD

    result = (mm(h, h) - 1 - mm(2*h % MOD, s1) + s2) % MOD
    return str(result)

if __name__ == '__main__':
    print(solve())
