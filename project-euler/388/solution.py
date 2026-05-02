def solve():
    import math

    n = 10000000000
    sieve_limit = max(1000000, int(math.pow(n, 2.0 / 3.0)) + 1000)

    primes = []
    lp = [0] * (sieve_limit + 1)
    mu = [0] * (sieve_limit + 1)
    mu[1] = 1

    for i in range(2, sieve_limit + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
            mu[i] = -1
        for p in primes:
            x = i * p
            if x > sieve_limit:
                break
            lp[x] = p
            if p == lp[i]:
                mu[x] = 0
                break
            mu[x] = -mu[i]

    prefix = [0] * (sieve_limit + 1)
    for i in range(1, sieve_limit + 1):
        prefix[i] = prefix[i - 1] + mu[i]

    cache = {}

    def M(x):
        if x <= sieve_limit:
            return prefix[x]
        if x in cache:
            return cache[x]

        ans = 1
        l = 2
        while l <= x:
            q = x // l
            r = x // q
            ans -= (r - l + 1) * M(q)
            l = r + 1

        cache[x] = ans
        return ans

    answer = 0
    l = 1
    while l <= n:
        q = n // l
        r = n // q
        mu_block = M(r) - M(l - 1)

        f = (q + 1) ** 3 - 1
        answer += f * mu_block

        l = r + 1

    s = str(answer)
    if len(s) <= 18:
        return s
    return s[:9] + s[-9:]

if __name__ == '__main__':
    print(solve())
