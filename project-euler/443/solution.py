def solve():
    N = 10**15

    def smallest_prime_factor(n):
        if n % 2 == 0: return 2
        if n % 3 == 0: return 3
        d = 5
        while d * d <= n:
            if n % d == 0: return d
            if n % (d + 2) == 0: return d + 2
            d += 6
        return n

    if N <= 9:
        g = 13
        for k in range(5, N+1):
            from math import gcd
            g += gcd(k, g)
        return str(g)

    anchor = 9
    while anchor < N:
        p = smallest_prime_factor(2 * anchor - 1)
        next_anchor = anchor + (p - 1) // 2
        if next_anchor > N:
            return str(N + 2 * anchor)
        anchor = next_anchor

    return str(3 * N)

if __name__ == '__main__':
    print(solve())
