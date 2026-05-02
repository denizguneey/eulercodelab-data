import math

def solve():
    LIMIT = 100_000_000

    # Sieve primes up to LIMIT + 1
    max_p = LIMIT + 1
    is_prime = bytearray(b'\x01' * (max_p + 1))
    is_prime[0] = 0
    is_prime[1] = 0
    for i in range(4, max_p + 1, 2):
        is_prime[i] = 0
    p = 3
    while p * p <= max_p:
        if is_prime[p]:
            for j in range(p*p, max_p + 1, 2*p):
                is_prime[j] = 0
        p += 2

    # Build SPF for odd numbers up to LIMIT/2
    half = LIMIT // 2
    spf_odd = [0] * (half + 1)
    root = math.isqrt(half)
    p = 3
    while p <= root:
        if spf_odd[p // 2] == 0:
            for j in range(p*p, half + 1, 2*p):
                if spf_odd[j // 2] == 0:
                    spf_odd[j // 2] = p
        p += 2

    def check_n(n):
        if n == 1:
            return True
        if n & 1:
            return False
        if n & 3 == 0:
            return False
        m = n // 2
        factors = [2]
        while m > 1:
            p = spf_odd[m // 2]
            if p == 0:
                p = m
            factors.append(p)
            m //= p
            if m % p == 0:
                return False

        # Generate all divisors
        divisors = [1]
        for p in factors:
            size = len(divisors)
            for i in range(size):
                divisors.append(divisors[i] * p)

        for d in divisors:
            q = n // d
            if d > q:
                continue
            if not is_prime[d + q]:
                return False
        return True

    total = 0
    # Check n = p - 1 for each prime p
    for p in range(2, max_p + 1):
        if not is_prime[p]:
            continue
        n = p - 1
        if n > LIMIT:
            continue
        if check_n(n):
            total += n

    return str(total)

if __name__ == '__main__':
    print(solve())
