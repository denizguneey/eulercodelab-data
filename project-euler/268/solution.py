def primes_below_100():
    max_n = 100
    composite = [False] * (max_n + 1)
    primes = []
    for i in range(2, max_n):
        if not composite[i]:
            primes.append(i)
        for p in primes:
            v = i * p
            if v >= max_n:
                break
            composite[v] = True
            if i % p == 0:
                break
    return primes

def binom(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    numer = 1
    denom = 1
    for i in range(1, k + 1):
        numer *= (n - k + i)
        denom *= i
    return numer // denom

def solve_limit(limit):
    if limit <= 1:
        return 0

    primes = primes_below_100()
    subset_sums = [0] * 26
    max_value = limit - 1

    def dfs(index, taken, product):
        if taken >= 4:
            subset_sums[taken] += max_value // product

        if index >= len(primes):
            return

        for i in range(index, len(primes)):
            p = primes[i]
            if product > max_value // p:
                continue
            dfs(i + 1, taken + 1, product * p)

    dfs(0, 0, 1)

    answer = 0
    for k in range(4, len(primes) + 1):
        coeff = (1 if (k - 4) % 2 == 0 else -1) * binom(k - 1, 3)
        answer += coeff * subset_sums[k]

    return answer

def solve():
    limit = 10000000000000000
    ans = solve_limit(limit)
    return str(ans)

if __name__ == '__main__':
    print(solve())
