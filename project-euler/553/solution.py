def solve():
    MOD = 1_000_000_007
    N_VAL = 10_000
    K_VAL = 10

    def mod_pow(base, exp, mod):
        result = 1 % mod
        cur = base % mod
        while exp > 0:
            if exp & 1: result = result * cur % mod
            cur = cur * cur % mod
            exp >>= 1
        return result

    def mod_inv(a): return mod_pow(a, MOD - 2, MOD)

    max_n = max(N_VAL, K_VAL, 100)

    fact = [1] * (max_n + 1)
    for i in range(1, max_n + 1): fact[i] = fact[i-1] * i % MOD
    invfact = [1] * (max_n + 1)
    invfact[max_n] = mod_inv(fact[max_n])
    for i in range(max_n, 0, -1): invfact[i-1] = invfact[i] * i % MOD
    invInt = [0] * (max_n + 1)
    invInt[1] = 1
    for i in range(2, max_n + 1):
        invInt[i] = MOD - (MOD // i) * invInt[MOD % i] % MOD

    kModM1 = MOD - 1
    pow2_modM1 = [1] * (max_n + 1)
    for r in range(1, max_n + 1):
        pow2_modM1[r] = 2 * pow2_modM1[r-1] % kModM1

    T = [0] * (max_n + 1)
    for r in range(max_n + 1):
        e = pow2_modM1[r] - 1
        if e < 0: e += kModM1
        v = mod_pow(2, e, MOD)
        T[r] = (v - 1) % MOD

    def poly_mul(a, b, n):
        c = [0] * (n + 1)
        for i in range(n + 1):
            s = 0
            for j in range(i + 1):
                s += a[j] * b[i - j]
            c[i] = s % MOD
        return c

    def poly_pow(base, exp, n):
        res = [0] * (n + 1)
        res[0] = 1
        while exp > 0:
            if exp & 1: res = poly_mul(res, base, n)
            exp >>= 1
            if exp > 0: base = poly_mul(base, base, n)
        return res

    invfactS = list(invfact[:max_n+1])
    Bsign = [0] * (max_n + 1)
    for r in range(max_n + 1):
        b = T[r] * invfact[r] % MOD
        Bsign[r] = (MOD - b) % MOD if r & 1 else b

    convA = poly_mul(Bsign, invfactS, max_n)
    Acoef = [0] * (max_n + 1)
    Acoef[0] = 1
    for n in range(1, max_n + 1):
        v = convA[n]
        if n & 1: v = (MOD - v) % MOD
        Acoef[n] = v

    Gcoef = [0] * (max_n + 1)
    iG = [0] * (max_n + 1)
    for m in range(1, max_n + 1):
        s = 0
        for i in range(1, m):
            s = (s + iG[i] * Acoef[m - i]) % MOD
        corr = s * invInt[m] % MOD
        gm = (Acoef[m] - corr) % MOD
        Gcoef[m] = gm
        iG[m] = m * gm % MOD

    Gpow = poly_pow(Gcoef, K_VAL, max_n)
    S = poly_mul(invfactS, Gpow, max_n)
    answer = fact[N_VAL] * S[N_VAL] % MOD * invfact[K_VAL] % MOD

    return str(answer)

if __name__ == '__main__':
    print(solve())
