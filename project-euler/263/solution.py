import math

def solve():
    LIMIT = 2_000_000_000
    TARGET_COUNT = 4

    def isqrt(n):
        return math.isqrt(n)

    def sieve_primes(limit):
        if limit < 2:
            return []
        is_p = bytearray(b'\x01' * (limit + 1))
        is_p[0] = 0
        is_p[1] = 0
        for p in range(2, isqrt(limit) + 1):
            if is_p[p]:
                is_p[p*p::p] = bytearray(len(is_p[p*p::p]))
        return [p for p in range(2, limit + 1) if is_p[p]]

    def factorize(n, primes):
        factors = []
        if n <= 1:
            return factors
        m = n
        for p in primes:
            if p * p > m:
                break
            if m % p != 0:
                continue
            e = 0
            while m % p == 0:
                m //= p
                e += 1
            factors.append((p, e))
        if m > 1:
            factors.append((m, 1))
        return factors

    def sigma_pp(prime, exp):
        s = 1
        pw = 1
        for _ in range(exp):
            pw *= prime
            s += pw
        return s

    def is_practical(n, primes):
        if n == 1:
            return True
        if n & 1:
            return False
        factors = factorize(n, primes)
        if not factors or factors[0][0] != 2:
            return False
        sigma_prefix = sigma_pp(factors[0][0], factors[0][1])
        for i in range(1, len(factors)):
            p = factors[i][0]
            if p > sigma_prefix + 1:
                return False
            sigma_prefix *= sigma_pp(factors[i][0], factors[i][1])
        return True

    def is_paradise_candidate(n, primes):
        if n < 9:
            return False
        for off in [-8, -4, 0, 4, 8]:
            if not is_practical(n + off, primes):
                return False
        return True

    sieve_max = LIMIT + 9
    root = isqrt(sieve_max) + 1
    base_primes = sieve_primes(root)

    def sieve_segment(low, high):
        if high < 2 or low > high:
            return []
        odd_low = max(3, low | 1)
        if odd_low > high:
            return []
        odd_count = (high - odd_low) // 2 + 1
        is_p = bytearray(b'\x01' * odd_count)
        for p in base_primes:
            if p == 2:
                continue
            if p * p > high:
                break
            start = ((odd_low + p - 1) // p) * p
            if start < p * p:
                start = p * p
            if start % 2 == 0:
                start += p
            idx = (start - odd_low) // 2
            while idx < odd_count:
                is_p[idx] = 0
                idx += p
        return [odd_low + 2 * i for i in range(odd_count) if is_p[i]]

    prime_limit = LIMIT + 9
    window = []
    paradises = []
    total_sum = 0

    def process_prime(p):
        nonlocal total_sum
        window.append(p)
        if len(window) > 4:
            window.pop(0)
        if len(window) != 4:
            return
        if (window[1]-window[0] != 6 or window[2]-window[1] != 6 or window[3]-window[2] != 6):
            return
        n = window[0] + 9
        if n > LIMIT:
            return
        if not is_paradise_candidate(n, base_primes):
            return
        paradises.append(n)
        total_sum += n

    process_prime(2)
    seg_size = 8_000_000
    seg_low = 3
    while seg_low <= prime_limit and len(paradises) < TARGET_COUNT:
        seg_high = min(prime_limit, seg_low + seg_size - 1)
        primes = sieve_segment(seg_low, seg_high)
        for p in primes:
            process_prime(p)
            if len(paradises) >= TARGET_COUNT:
                break
        seg_low = seg_high + 1

    return str(total_sum)

if __name__ == '__main__':
    print(solve())
