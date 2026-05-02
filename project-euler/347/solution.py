def solve():
    limit = 10_000_000

    # Sieve primes
    is_composite = bytearray(limit + 1)
    primes = []
    for i in range(2, limit + 1):
        if not is_composite[i]:
            primes.append(i)
            if i <= limit // i:
                for j in range(i*i, limit + 1, i):
                    is_composite[j] = 1

    def max_for_pair(p, q):
        if p * q > limit:
            return 0
        best = 0
        pa = p
        while pa <= limit // q:
            value = pa * q
            while value <= limit:
                if value > best:
                    best = value
                if value > limit // q:
                    break
                value *= q
            if pa > limit // p:
                break
            pa *= p
        return best

    seen = bytearray(limit + 1)
    total = 0
    for i in range(len(primes)):
        p = primes[i]
        if p * 2 > limit:
            break
        for j in range(i + 1, len(primes)):
            q = primes[j]
            if p * q > limit:
                break
            m = max_for_pair(p, q)
            if m > 0 and not seen[m]:
                seen[m] = 1
                total += m

    return str(total)

if __name__ == '__main__':
    print(solve())
