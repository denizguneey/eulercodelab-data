def solve():
    MOD = 1000000087
    n = 10000000

    # SPF sieve
    spf = list(range(n + 1))
    primes = []
    for i in range(2, n + 1):
        if spf[i] == i: primes.append(i)
        for p in primes:
            if p > spf[i] or i * p > n: break
            spf[i * p] = p

    # Max term bound
    def max_term_bound(n):
        e2 = 0; x = n
        while x > 0: e2 += x // 2; x //= 2
        return 2 * e2 + 1

    bound = max_term_bound(n)
    inv = [0] * (bound + 1); inv[1] = 1
    for i in range(2, bound + 1):
        inv[i] = MOD - (MOD // i) * inv[MOD % i] % MOD

    exp = [0] * (n + 1)
    current = 1; ans = 0

    for i in range(2, n + 1):
        x = i
        while x > 1:
            p = spf[x]; c = 0
            while x % p == 0: x //= p; c += 1
            old_t = 1 + 2 * exp[p]
            exp[p] += c
            new_t = 1 + 2 * exp[p]
            current = current * new_t % MOD * inv[old_t] % MOD
        ans = (ans + current) % MOD

    return str(ans)

if __name__ == '__main__':
    print(solve())
