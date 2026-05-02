import math

def solve():
    limit = 100000000000000000
    # Fourth root bound of 4*limit
    def fourth_root_bound(n):
        target = 4 * n
        m = int(target ** 0.25) + 4
        while m > 0 and m**4 > target: m -= 1
        while (m+1)**4 <= target: m += 1
        return m + 2

    m_max = fourth_root_bound(limit)
    total = 0
    for m in range(2, m_max + 1):
        mm = m * m
        n_start = m // 2 + 1
        for n in range(n_start, m):
            if math.gcd(m, n) != 1: continue
            nn = n * n
            x_raw = mm - 4 * m * n - nn
            x_abs = abs(x_raw)
            y_abs = 2 * (mm + m * n - nn)
            w = mm + nn
            g = math.gcd(x_abs, math.gcd(y_abs, w))
            if g % 5 == 0: continue
            u = x_abs // g
            v = y_abs // g
            if u < v: u, v = v, u
            a_prim = (u * v) // 2
            if a_prim > limit: continue
            total += limit // a_prim
    return str(total)

if __name__ == '__main__':
    print(solve())
