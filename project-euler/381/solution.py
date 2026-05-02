def solve():
    limit = 100_000_000

    # Sieve primes
    is_composite = bytearray(limit)
    primes = []
    for i in range(2, limit):
        if not is_composite[i]:
            primes.append(i)
            if i <= (limit - 1) // i:
                for j in range(i*i, limit, i):
                    is_composite[j] = 1

    def inv8_mod_prime(p):
        r = p & 7
        k = 8 - r
        return (k * p + 1) // 8

    def S_of_prime(p):
        inv8 = inv8_mod_prime(p)
        return (p + p - (3 * inv8) % p) % p

    total = 0
    for p in primes:
        if p < 5:
            continue
        total += S_of_prime(p)

    return str(total)

if __name__ == '__main__':
    print(solve())
