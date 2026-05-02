def solve():
    MOD = 998244353
    INV2 = (MOD + 1) // 2
    N = 100_000_000_000
    SIEVE_LIMIT = 5_000_000

    def mod_mul(a, b):
        return a % MOD * (b % MOD) % MOD

    def tri_mod(l, r):
        a = (l + r) % MOD
        b = (r - l + 1) % MOD
        return a * b % MOD * INV2 % MOD

    # Totient sieve
    phi = list(range(SIEVE_LIMIT + 1))
    is_comp = bytearray(SIEVE_LIMIT + 1)
    primes = []
    phi[0] = 0
    phi[1] = 1
    for i in range(2, SIEVE_LIMIT + 1):
        if not is_comp[i]:
            primes.append(i)
            phi[i] = i - 1
        for p in primes:
            if i * p > SIEVE_LIMIT:
                break
            is_comp[i * p] = 1
            if i % p == 0:
                phi[i * p] = phi[i] * p
                break
            phi[i * p] = phi[i] * (p - 1)

    pref = [0] * (SIEVE_LIMIT + 1)
    for i in range(1, SIEVE_LIMIT + 1):
        pref[i] = (pref[i-1] + phi[i]) % MOD

    memo = {}

    def sum_phi(n):
        if n <= SIEVE_LIMIT:
            return pref[n]
        if n in memo:
            return memo[n]
        res = n % MOD * ((n + 1) % MOD) % MOD * INV2 % MOD
        l = 2
        while l <= n:
            q = n // l
            r = n // q
            cnt = (r - l + 1) % MOD
            sub = cnt * sum_phi(q) % MOD
            res = (res - sub) % MOD
            l = r + 1
        memo[n] = res
        return res

    sum_phi(N)

    ans = 0
    l = 1
    while l <= N:
        q = N // l
        r = N // q
        sd = tri_mod(l, r)
        sp = sum_phi(q)
        ans = (ans + sd * sp) % MOD
        l = r + 1

    return str(ans % MOD)

if __name__ == '__main__':
    print(solve())
