import math

def solve():
    N = 100_000_000

    # Odd sieve for primality
    half = (N + 1) // 2
    sieve = bytearray([1]) * half
    sieve[0] = 0  # 1 is not prime
    for i in range(1, half):
        p = 2 * i + 1
        if p * p > N: break
        if sieve[i]:
            start = (p * p) >> 1
            for j in range(start, half, p):
                sieve[j] = 0

    def is_prime(x):
        if x == 2: return True
        if x < 2 or x % 2 == 0: return False
        return sieve[x >> 1] != 0

    limit = int(N ** 0.5)
    total = 0
    for v in range(2, limit + 1):
        v2 = v * v
        max_d = N // v2
        for u in range(1, v):
            if math.gcd(u, v) != 1: continue
            u2 = u * u
            uv = u * v

            # Odd d=3 special case
            if u == 1 and v % 2 == 0 and max_d >= 3:
                d = 3
                a = u2 * d - 1
                b = uv * d - 1
                c = v2 * d - 1
                if is_prime(a) and is_prime(b) and is_prime(c):
                    total += a + b + c

            # Even d
            for d in range(2, max_d + 1, 2):
                a = u2 * d - 1
                b = uv * d - 1
                c = v2 * d - 1
                if is_prime(a) and is_prime(b) and is_prime(c):
                    total += a + b + c

    return str(total)

if __name__ == '__main__':
    print(solve())
