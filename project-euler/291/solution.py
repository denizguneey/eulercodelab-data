import math

def solve():
    LIMIT = 5_000_000_000_000_000

    def isqrt(x):
        r = math.isqrt(x)
        return r

    def q_value(n):
        return 2 * n * n + 2 * n + 1

    def max_index_for_limit(limit):
        if limit <= 5:
            return 0
        m = (isqrt(2 * limit - 1) - 1) // 2
        while m > 0 and q_value(m) >= limit:
            m -= 1
        while q_value(m + 1) < limit:
            m += 1
        return m

    m = max_index_for_limit(LIMIT)
    if m == 0:
        return '0'

    values = [0] * (m + 1)
    composite = bytearray(m + 1)
    for i in range(1, m + 1):
        values[i] = q_value(i)

    count = 0
    for i in range(1, m + 1):
        if composite[i] == 0:
            count += 1
        prime = values[i]
        if prime == 1:
            continue

        for j in range(i + prime, m + 1, prime):
            composite[j] = 1
            v = values[j]
            while v % prime == 0:
                v //= prime
            values[j] = v

        mod = (i + 1) % prime
        start = prime if mod == 0 else prime - mod
        if start == i:
            start += prime
        for j in range(start, m + 1, prime):
            composite[j] = 1
            v = values[j]
            while v % prime == 0:
                v //= prime
            values[j] = v

    return str(count)

if __name__ == '__main__':
    print(solve())
