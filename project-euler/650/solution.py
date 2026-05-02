def solve():
    MOD = 1_000_000_007
    N = 20000

    def mod_pow(a, e, m=MOD):
        r = 1
        a %= m
        while e > 0:
            if e & 1: r = r * a % m
            a = a * a % m
            e >>= 1
        return r

    def mod_add(a, b): return (a + b) % MOD
    def mod_mul(a, b): return a * b % MOD

    # SPF sieve
    spf = [0] * (N + 1)
    primes = []
    for i in range(2, N + 1):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
        for p in primes:
            if p > spf[i] or i * p > N: break
            spf[i * p] = p

    P = len(primes)
    pidx = [-1] * (N + 1)
    for i, p in enumerate(primes):
        pidx[p] = i

    invp = [mod_pow(p, MOD - 2) for p in primes]
    invpm1 = [mod_pow(p - 1, MOD - 2) for p in primes]

    invPowA = [1] * P
    powE1 = [p % MOD for p in primes]

    S = 0
    for n in range(1, N + 1):
        for i in range(P):
            powE1[i] = mod_mul(powE1[i], invPowA[i])

        x = n
        while x > 1:
            p = spf[x]
            v = 0
            while x % p == 0:
                x //= p
                v += 1
            i = pidx[p]
            add_e = (n - 1) * v
            if add_e:
                powE1[i] = mod_mul(powE1[i], mod_pow(p, add_e))
            invPowA[i] = mod_mul(invPowA[i], mod_pow(invp[i], v))

        D = 1
        for i in range(P):
            t = powE1[i]
            num = (t + MOD - 1) % MOD
            term = mod_mul(num, invpm1[i])
            D = mod_mul(D, term)

        S = mod_add(S, D)

    return str(S)

if __name__ == '__main__':
    print(solve())
