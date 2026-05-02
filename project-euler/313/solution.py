def sieve_primes(limit):
    is_prime = bytearray([1] * (limit + 1))
    is_prime[0] = 0
    is_prime[1] = 0
    for p in range(2, int(limit ** 0.5) + 1):
        if is_prime[p]:
            for q in range(p * p, limit + 1, p):
                is_prime[q] = 0
                
    return [p for p in range(2, limit + 1) if is_prime[p]]

def count_grids_for_prime_square(p2):
    if (p2 & 1) == 0:
        return 0
    h = (p2 + 13) // 2
    low = h // 4 + 1
    high = (h - 2) // 3 if h >= 2 else 0
    if high < low:
        return 0
    return 2 * (high - low + 1)

def solve(prime_limit=1000000):
    primes = sieve_primes(prime_limit - 1)
    total = 0
    for p in primes:
        p2 = p * p
        total += count_grids_for_prime_square(p2)
    return str(total)

if __name__ == '__main__':
    print(solve())
