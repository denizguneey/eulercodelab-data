def solve():
    prime_limit = 5000

    def primes_below(limit):
        is_p = bytearray(b'\x01' * limit)
        is_p[0] = 0
        is_p[1] = 0
        for p in range(2, limit):
            if p * p >= limit:
                break
            if is_p[p]:
                for q in range(p*p, limit, p):
                    is_p[q] = 0
        return [p for p in range(2, limit) if is_p[p]]

    primes = primes_below(prime_limit)
    n = len(primes)
    answer = 0
    for i in range(n):
        p = primes[i]
        for j in range(i + 1, n):
            q = primes[j]
            pq = p * q
            for k in range(j + 1, n):
                r = primes[k]
                answer += 2 * pq * r - pq - p * r - q * r
    return str(answer)

if __name__ == '__main__':
    print(solve())
