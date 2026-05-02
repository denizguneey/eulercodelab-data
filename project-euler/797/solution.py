def solve():
    MOD = 1000000007
    N = 10000000

    def mod_pow(a, e):
        r = 1; a %= MOD
        while e > 0:
            if e & 1: r = r * a % MOD
            a = a * a % MOD; e >>= 1
        return r

    # Linear sieve for Mobius
    mu = [0]*(N+1); mu[1] = 1; lp = [0]*(N+1); primes = []
    for i in range(2, N+1):
        if lp[i] == 0: lp[i] = i; primes.append(i); mu[i] = -1
        for p in primes:
            if i*p > N: break
            lp[i*p] = p
            if p == lp[i]: mu[i*p] = 0; break
            mu[i*p] = -mu[i]

    mertens_mod = [0]*(N+1)
    for i in range(1, N+1):
        v = mertens_mod[i-1] + mu[i]
        mertens_mod[i] = v % MOD

    # base[i] = 2^i - 1 mod MOD
    base = [0]*(N+1); p2 = 1
    for i in range(1, N+1):
        p2 = p2 * 2 % MOD; base[i] = (p2 - 1) % MOD

    # inv_base prefix product and individual inverses
    inv_pref = [1]*(N+1)
    for i in range(1, N+1): inv_pref[i] = inv_pref[i-1] * base[i] % MOD
    inv_total = mod_pow(inv_pref[N], MOD-2)
    inv_base = [0]*(N+1)
    for i in range(N, 0, -1):
        inv_base[i] = inv_total * inv_pref[i-1] % MOD
        inv_total = inv_total * base[i] % MOD

    # phi2[n] = product over d|n of base[d]^mu(n/d)
    phi2 = [1]*(N+1)
    for k in range(1, N+1):
        mk = mu[k]
        if mk == 0: continue
        limit = N // k; nn = k
        if mk > 0:
            for m in range(1, limit+1): phi2[nn] = phi2[nn] * base[m] % MOD; nn += k
        else:
            nn = k
            for m in range(1, limit+1): phi2[nn] = phi2[nn] * inv_base[m] % MOD; nn += k

    F = [1]*(N+1)
    for d in range(1, N+1):
        factor = (phi2[d] + 1) % MOD
        for nn in range(d, N+1, d): F[nn] = F[nn] * factor % MOD

    ans = 0
    for nn in range(1, N+1):
        ans = (ans + F[nn] * mertens_mod[N // nn]) % MOD

    return str(ans)

if __name__ == '__main__':
    print(solve())
