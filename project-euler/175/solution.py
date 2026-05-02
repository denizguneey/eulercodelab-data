# Problem 175: Fractions involving the number of different ways a number can be expressed as a sum of powers of 2.
# f(n)/f(n-1) = p/q  => shortened binary expansion of n = shortened expansion of p/q

from math import gcd

def solve():
    p, q = 123456789, 987654321
    g = gcd(p, q)
    p, q = p // g, q // g

    def expansion(p, q):
        result = []
        while q != 0:
            if p > q:
                nxt = (p - 1) % q + 1
                result.append((p - nxt) // q)
                p = nxt
            else:
                nxt = q % p
                result.append((q - nxt) // p)
                q = nxt
        result.reverse()
        return result

    print(','.join(str(x) for x in expansion(p, q)))

solve()
