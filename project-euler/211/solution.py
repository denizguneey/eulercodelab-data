import math

def solve():
    limit = 64000000

    def is_perfect_square(x):
        r = math.isqrt(x)
        return r * r == x

    def prime_list_upto(lim):
        if lim < 2:
            return []
        is_p = bytearray(b'\x01' * (lim + 1))
        is_p[0] = 0
        is_p[1] = 0
        r = math.isqrt(lim)
        for p in range(2, r + 1):
            if is_p[p]:
                is_p[p*p::p] = bytearray(len(is_p[p*p::p]))
        return [p for p in range(2, lim + 1) if is_p[p]]

    primes = prime_list_upto(limit - 1)

    def contribution(from_idx, s0, n0, lim):
        result = 0
        max_n = lim - 1
        for i in range(from_idx, len(primes)):
            p = primes[i]
            if n0 > max_n // p:
                break
            p2 = p * p
            s = 1
            pwr = p
            while n0 <= max_n // pwr:
                n = n0 * pwr
                s = s * p2 + 1
                s2 = s0 * s
                if is_perfect_square(s2):
                    result += n
                result += contribution(i + 1, s2, n, lim)
                if pwr > max_n // p:
                    break
                pwr *= p
        return result

    total = 1
    for i in range(len(primes)):
        p = primes[i]
        max_n = limit - 1
        if p > max_n:
            break
        p2 = p * p
        s = 1
        pwr = p
        while pwr <= max_n:
            s = s * p2 + 1
            if is_perfect_square(s):
                total += pwr
            total += contribution(i + 1, s, pwr, limit)
            if pwr > max_n // p:
                break
            pwr *= p
    return str(total)

if __name__ == '__main__':
    print(solve())
