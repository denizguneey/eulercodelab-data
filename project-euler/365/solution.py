def solve():
    N = 10**18
    K = 10**9

    def mod_pow(base, exp, mod):
        result = 1 % mod
        base %= mod
        while exp > 0:
            if exp & 1:
                result = (result * base) % mod
            base = (base * base) % mod
            exp >>= 1
        return result

    def primes_between(lo_exc, hi_exc):
        sieve = bytearray(b'\x01' * hi_exc)
        sieve[0] = 0
        if hi_exc > 1:
            sieve[1] = 0
        p = 2
        while p * p < hi_exc:
            if sieve[p]:
                sieve[p*p::p] = bytearray(len(sieve[p*p::p]))
            p += 1
        return [x for x in range(max(2, lo_exc + 1), hi_exc) if sieve[x]]

    def binom_mod_prime_lucas(n, k, p):
        fact = [1] * p
        for i in range(1, p):
            fact[i] = (fact[i-1] * i) % p
        inv_fact = [1] * p
        inv_fact[p-1] = mod_pow(fact[p-1], p-2, p)
        for i in range(p-1, 0, -1):
            inv_fact[i-1] = (inv_fact[i] * i) % p

        nn, kk = n, k
        result = 1
        while nn > 0 or kk > 0:
            ni = nn % p
            ki = kk % p
            if ki > ni:
                return 0
            term = (fact[ni] * inv_fact[ki] % p) * inv_fact[ni - ki] % p
            result = (result * term) % p
            nn //= p
            kk //= p
        return result

    primes = primes_between(1000, 5000)
    m = len(primes)

    # Precompute residues
    residues = [binom_mod_prime_lucas(N, K, p) for p in primes]

    # Precompute inverses
    inv = [[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            if i != j:
                mod = primes[j]
                inv[i][j] = mod_pow(primes[i] % mod, mod - 2, mod)

    # CRT triple sum
    total = 0
    for i in range(m - 2):
        p = primes[i]
        a = residues[i]
        for j in range(i + 1, m - 1):
            q = primes[j]
            b = residues[j]
            diff_ab = (b - a + q) % q
            t = (diff_ab * inv[i][j]) % q
            x_pq = a + p * t
            pq = p * q
            for kidx in range(j + 1, m):
                r = primes[kidx]
                c = residues[kidx]
                diff_c = (c - (x_pq % r) + r) % r
                inv_pq_mod_r = (inv[i][kidx] * inv[j][kidx]) % r
                u = (diff_c * inv_pq_mod_r) % r
                x = x_pq + pq * u
                total += x

    return str(total)

if __name__ == '__main__':
    print(solve())
