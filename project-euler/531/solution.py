import math

def solve():
    L, R = 1000000, 1005000
    N = R - L

    # Euler phi sieve
    phi = list(range(R + 1))
    for p in range(2, R + 1):
        if phi[p] != p: continue
        for m in range(p, R + 1, p):
            phi[m] -= phi[m] // p

    def ext_gcd(a, b):
        if b == 0: return a, 1, 0
        g, x1, y1 = ext_gcd(b, a % b)
        return g, y1, x1 - (a // b) * y1

    def crt_min(a, n, b, m):
        g = math.gcd(n, m)
        diff = b - a
        if diff % g != 0: return 0
        n1, m1 = n // g, m // g
        rhs = diff // g
        _, inv, _ = ext_gcd(n1, m1)
        inv %= m1
        rhs_mod = rhs % m1
        t = rhs_mod * inv % m1
        return a + n * t

    total = 0
    for i in range(N):
        n = L + i; a = phi[n]
        for j in range(i + 1, N):
            m = L + j; b = phi[m]
            total += crt_min(a, n, b, m)

    return str(total)

if __name__ == '__main__':
    print(solve())
