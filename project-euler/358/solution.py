def solve():
    def mod_pow(base, exp, mod):
        result = 1 % mod
        base %= mod
        while exp > 0:
            if exp & 1:
                result = (result * base) % mod
            base = (base * base) % mod
            exp >>= 1
        return result

    def is_prime(n):
        if n < 2:
            return False
        if n % 2 == 0:
            return n == 2
        d = 3
        while d * d <= n:
            if n % d == 0:
                return False
            d += 2
        return True

    def prime_factors_distinct(n):
        factors = []
        if n % 2 == 0:
            factors.append(2)
            while n % 2 == 0:
                n //= 2
        d = 3
        while d * d <= n:
            if n % d == 0:
                factors.append(d)
                while n % d == 0:
                    n //= d
            d += 2
        if n > 1:
            factors.append(n)
        return factors

    def is_full_reptend(p):
        if not is_prime(p) or p == 2 or p == 5:
            return False
        phi = p - 1
        factors = prime_factors_distinct(phi)
        for q in factors:
            if mod_pow(10, phi // q, p) == 1:
                return False
        return True

    # Find prime p with specific constraints
    low = 100000000000 // 138 + 1
    high = 100000000000 // 137
    mod = 100000
    residue = 9891

    start = low
    rem = start % mod
    if rem <= residue:
        start += residue - rem
    else:
        start += mod - (rem - residue)

    found = 0
    p = start
    while p <= high:
        if 100000000000 // p == 137:
            if is_full_reptend(p):
                if (p * 56789 + 1) % mod == 0:
                    found = p
        p += mod

    answer = (9 * (found - 1)) // 2
    return str(answer)

if __name__ == '__main__':
    print(solve())
