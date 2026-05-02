import math

def solve():
    N_val = 1000000000

    def calc_lattice(a, b, c):
        if a < b: a, b = b, a
        if a > c: return 0
        m = c // a
        if a == b: return m * (m - 1) // 2
        k = (a - 1) // b
        h = (c - a * m) // b
        return calc_lattice(b, a - b*k, c - b*(k*m + h)) + k*m*(m-1)//2 + m*h

    memo = {0: 0, 1: 1}
    def mertens(n):
        if n <= 1: return n
        if n in memo: return memo[n]
        z = 1
        f = int(math.isqrt(n))
        lim = n // (f + 1)
        for i in range(1, lim + 1):
            c = n // i
            if c < n: z -= mertens(c)
        for i in range(f, 0, -1):
            a = n // (i + 1) + 1; b = n // i; c2 = i
            if c2 < n: z -= mertens(c2) * (b - a + 1)
        memo[n] = z; return z

    def mertens_nm3(n):
        z = 0
        while n > 0: z += mertens(n); n //= 3
        return z

    n = 3 * N_val + 6
    f = int(math.isqrt(n))
    z = 0

    lim = n // (f + 1)
    for i in range(1, lim + 1):
        g = n // i
        q = calc_lattice(18, 10, g) - calc_lattice(18, 30, g)
        if q == 0: break
        z += (mertens_nm3(i) - mertens_nm3(i - 1)) * q

    for i in range(f, 0, -1):
        a = n // (i + 1) + 1; b = n // i; g = i
        q = calc_lattice(18, 10, g) - calc_lattice(18, 30, g)
        if q == 0: break
        z += (mertens_nm3(b) - mertens_nm3(a - 1)) * q

    return str(4 * z + 2)

if __name__ == '__main__':
    print(solve())
