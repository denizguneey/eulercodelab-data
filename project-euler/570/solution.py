import math

def solve():
    N = 10000000

    def pow_mod(b4, b3, exp, mod):
        r4, r3 = 1 % mod, 1 % mod
        e = exp
        while e:
            if e & 1: r4 = r4 * b4 % mod; r3 = r3 * b3 % mod
            b4 = b4 * b4 % mod; b3 = b3 * b3 % mod
            e >>= 1
        return r4, r3

    total = 0
    for n in range(3, N + 1):
        exp = n - 2; m = 7*n + 3
        p4, p3 = pow_mod(4, 3, exp, m)
        v = (2 * p4 - p3) % m
        g = math.gcd(m, v)
        total += 6 * g

    return str(total)

if __name__ == '__main__':
    print(solve())
