import math

def solve():
    limit_n = 50000000

    def mod_pow(base, exp, mod):
        return pow(base, exp, mod)

    def tonelli_shanks(n, p):
        if n == 0:
            return 0
        if p == 2:
            return n
        if mod_pow(n, (p - 1) // 2, p) != 1:
            return 0
        if p % 4 == 3:
            return mod_pow(n, (p + 1) // 4, p)
        q = p - 1
        s = 0
        while q % 2 == 0:
            q //= 2
            s += 1
        z = 2
        while mod_pow(z, (p - 1) // 2, p) != p - 1:
            z += 1
        m = s
        c = mod_pow(z, q, p)
        t = mod_pow(n, q, p)
        r = mod_pow(n, (q + 1) // 2, p)
        while t != 1:
            i = 1
            t2 = (t * t) % p
            while t2 != 1:
                t2 = (t2 * t2) % p
                i += 1
            b = mod_pow(c, 1 << (m - i - 1), p)
            r = (r * b) % p
            t = (t * b % p * b) % p
            c = (b * b) % p
            m = i
        return r

    def sieve_primes(lim):
        is_p = bytearray(b'\x01' * (lim + 1))
        is_p[0] = 0
        is_p[1] = 0
        for p in range(2, math.isqrt(lim) + 1):
            if is_p[p]:
                is_p[p*p::p] = bytearray(len(is_p[p*p::p]))
        return [p for p in range(2, lim + 1) if is_p[p]]

    max_t = 2 * limit_n * limit_n - 1
    max_prime = math.isqrt(max_t)
    primes = sieve_primes(max_prime)

    composite = bytearray(limit_n + 1)

    for p in primes:
        if p == 2:
            continue
        mod8 = p & 7
        if mod8 != 1 and mod8 != 7:
            continue

        inv2 = (p + 1) // 2
        if mod8 == 7:
            sqrt2 = mod_pow(2, (p + 1) // 4, p)
            root = (sqrt2 * inv2) % p
        else:
            root = tonelli_shanks(inv2, p)
            if root == 0:
                continue

        r1 = root
        r2 = (p - r1) if r1 != 0 else 0

        half = (p + 1) // 2
        sr = math.isqrt(half)
        skip_n = sr if sr * sr == half else -1

        for residue in (r1, r2):
            if residue == r2 and r2 == r1:
                continue
            n = residue
            if n < 2:
                delta = 2 - n
                n += ((delta + p - 1) // p) * p
            while n <= limit_n:
                if n != skip_n:
                    composite[n] = 1
                n += p

    count = 0
    for n in range(2, limit_n + 1):
        if not composite[n]:
            count += 1
    return str(count)

if __name__ == '__main__':
    print(solve())
