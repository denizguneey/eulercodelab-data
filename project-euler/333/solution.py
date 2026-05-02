def solve():
    prime_limit = 1000000
    limit = prime_limit - 1

    # Build terms: rows of 2^a * 3^b values
    rows = []
    p2 = 1
    while p2 <= limit:
        row = []
        v = p2
        while v <= limit:
            row.append(v)
            if v > limit // 3:
                break
            v *= 3
        rows.append(row)
        p2 <<= 1

    # DFS partition counting
    count = [0] * (limit + 1)

    def dfs(i, j_limit, s):
        if i == len(rows):
            if s > 0:
                count[s] += 1
            return
        dfs(i + 1, j_limit, s)
        upper = min(j_limit, len(rows[i]))
        for j in range(upper):
            val = rows[i][j]
            if s + val > limit:
                break
            dfs(i + 1, j, s + val)

    import sys
    sys.setrecursionlimit(100000)
    dfs(0, 1000, 0)

    # Sieve primes
    is_prime = bytearray(b'\x01' * prime_limit)
    is_prime[0] = 0
    is_prime[1] = 0
    p = 2
    while p * p < prime_limit:
        if is_prime[p]:
            is_prime[p*p::p] = bytearray(len(is_prime[p*p::p]))
        p += 1

    total = 0
    for q in range(2, prime_limit):
        if is_prime[q] and count[q] == 1:
            total += q

    return str(total)

if __name__ == '__main__':
    print(solve())
