def solve():
    P = 10000019; MOD = P * P
    N = 1000000000; K = 1000000000000000; J = K // N

    def mul_mod(a, b): return a * b % MOD
    def pow_mod(base, exp):
        r = 1; base %= MOD
        while exp > 0:
            if exp & 1: r = r * base % MOD
            base = base * base % MOD; exp >>= 1
        return r
    def modinv(a, mod):
        t, nt, r, nr = 0, 1, mod, a
        while nr:
            q = r // nr; t, nt = nt, t - q*nt; r, nr = nr, r - q*nr
        return t % mod if r == 1 else 0

    # Build tables
    fact = [0]*P; fact[0] = 1
    for i in range(1, P): fact[i] = mul_mod(fact[i-1], i)
    fact_pm1 = fact[P-1]

    inv = [0]*P; inv[1] = 1
    for i in range(2, P): inv[i] = (MOD - mul_mod(MOD // i, inv[MOD % i])) % MOD

    H = [0]*P
    for i in range(1, P): H[i] = (H[i-1] + inv[i]) % MOD

    def vp_factorial(n):
        e = 0
        while n > 0: n //= P; e += n
        return e

    def fact_without_p(n):
        if n == 0: return 1
        q, r = divmod(n, P)
        res = fact_without_p(q)
        res = mul_mod(res, pow_mod(fact_pm1, q))
        res = mul_mod(res, fact[r])
        if r:
            qm = q % P
            if qm: res = mul_mod(res, (1 + mul_mod(mul_mod(qm, P), H[r])) % MOD)
        return res

    def binom_mod_p2(n, k):
        if k > n: return 0
        e = vp_factorial(n) - vp_factorial(k) - vp_factorial(n-k)
        if e >= 2: return 0
        a = fact_without_p(n); b = fact_without_p(k); c = fact_without_p(n-k)
        denom = mul_mod(b, c); res = mul_mod(a, modinv(denom, MOD))
        if e == 1: res = mul_mod(res, P)
        return res

    def coeff_lp(m, k):
        if k == 0: return 1
        if m == 0: return 0
        c = binom_mod_p2(m-k-1, k-1)
        ik = modinv(k % MOD, MOD)
        return mul_mod(c, mul_mod(m % MOD, ik))

    # Compute L(N, K)
    binN = [0]*(J+1); binN[0] = 1
    for j in range(J):
        num = (N - j) % MOD
        binN[j+1] = mul_mod(binN[j], mul_mod(num, inv[(j+1) % P] if j+1 < P else modinv((j+1) % MOD, MOD)))

    total = 0
    for j in range(J+1):
        k = K - N*j
        coeff = coeff_lp(N*(N-2*j), k)
        term = mul_mod(binN[j], coeff)
        if (N & 1) and (j & 1) and term: term = MOD - term
        total = (total + term) % MOD

    return str(total)

if __name__ == '__main__':
    print(solve())
