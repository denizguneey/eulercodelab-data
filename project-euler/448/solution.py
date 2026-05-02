def solve():
    MOD = 999999017
    N = 99999999019

    def mod_norm(x): return x % MOD
    def mod_add(a, b): return (a + b) % MOD
    def mod_sub(a, b): return (a - b) % MOD
    def mod_mul(a, b): return (a % MOD) * (b % MOD) % MOD

    def mod_inv(a):
        a = a % MOD
        b = MOD
        x0, x1 = 1, 0
        while b:
            q = a // b
            a, b = b, a - q * b
            x0, x1 = x1, x0 - q * x1
        return x0 % MOD

    INV2 = (MOD + 1) // 2
    INV6 = mod_inv(6)

    def sum_arith(l, r):
        if l > r: return 0
        cnt = (r - l + 1) % MOD
        s = (l + r) % MOD
        return s * cnt % MOD * INV2 % MOD

    def sum_sq(n):
        n = n % MOD
        return n * ((n+1) % MOD) % MOD * ((2*n+1) % MOD) % MOD * INV6 % MOD

    # Build sieve
    LIM = int(N ** (2/3)) + 10
    if LIM < 100: LIM = 100

    mu = [0] * (LIM + 1)
    phi = [0] * (LIM + 1)
    is_comp = bytearray(LIM + 1)
    primes = []
    mu[1] = 1; phi[1] = 1
    for i in range(2, LIM + 1):
        if not is_comp[i]:
            primes.append(i)
            mu[i] = -1
            phi[i] = i - 1
        for p in primes:
            v = i * p
            if v > LIM: break
            is_comp[v] = 1
            if i % p == 0:
                mu[v] = 0
                phi[v] = phi[i] * p
                break
            mu[v] = -mu[i]
            phi[v] = phi[i] * (p - 1)

    prefH = [0] * (LIM + 1)
    prefG = [0] * (LIM + 1)
    for i in range(1, LIM + 1):
        addH = 0
        if mu[i] == 1: addH = i
        elif mu[i] == -1: addH = MOD - i
        prefH[i] = mod_add(prefH[i-1], addH)
        addG = (i * phi[i]) % MOD
        prefG[i] = mod_add(prefG[i-1], addG)

    memoH = {}
    memoG = {}

    def H(n):
        if n <= 0: return 0
        if n <= LIM: return prefH[n]
        if n in memoH: return memoH[n]
        res = 1 % MOD
        l = 2
        while l <= n:
            v = n // l
            r = n // v
            coef = sum_arith(l, r)
            res = mod_sub(res, coef * H(v) % MOD)
            l = r + 1
        memoH[n] = res
        return res

    def G(n):
        if n <= 0: return 0
        if n <= LIM: return prefG[n]
        if n in memoG: return memoG[n]
        res = 0
        l = 1
        while l <= n:
            v = n // l
            r = n // v
            mu_seg = mod_sub(H(r), H(l-1))
            res = mod_add(res, mu_seg * sum_sq(v) % MOD)
            l = r + 1
        memoG[n] = res
        return res

    def T(n):
        res = 0
        l = 1
        while l <= n:
            v = n // l
            r = n // v
            seg = mod_sub(G(r), G(l-1))
            res = mod_add(res, (v % MOD) * seg % MOD)
            l = r + 1
        return res

    ans = mod_add(N % MOD, T(N))
    ans = ans * INV2 % MOD
    return str(ans)

if __name__ == '__main__':
    print(solve())
