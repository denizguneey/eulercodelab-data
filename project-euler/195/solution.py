# Problem 195: Inscribed circles of triangles with one angle of 60 degrees
# Count triangles with inscribed circle radius <= N = 1053779.

from math import gcd, isqrt

def solve():
    N = 1053779

    def floor_c_div_q_sqrt3(C, q):
        """floor(C / (q * sqrt(3))), i.e., max k such that 3*q*q*k*k <= C*C"""
        C2 = C * C
        est = isqrt(C2 // (3 * q * q))
        while (est + 1) * (est + 1) * 3 * q * q <= C2:
            est += 1
        while est > 0 and est * est * 3 * q * q > C2:
            est -= 1
        return est

    # Type B: q = n*(n+t) where t = m-n, gcd(n,t)=1, t%3 != 0
    # radius bound: k*sqrt(3)*q/2 <= N => k <= 2N/(q*sqrt(3))
    C_b = 2 * N
    q_limit_b = floor_c_div_q_sqrt3(C_b, 1)

    total = 0

    # Type B
    n = 1
    while n * (n + 1) <= q_limit_b:
        t_max = q_limit_b // n - n
        for t in range(1, t_max + 1):
            if t % 3 == 0: continue
            if gcd(n, t) != 1: continue
            q = n * (n + t)
            k = floor_c_div_q_sqrt3(C_b, q)
            total += k
        n += 1

    # Type A: q = t*(3n+t), gcd(n,t)=1, t%3 != 0
    # radius bound: k*sqrt(3)*q/6 <= N => k <= 6N/(q*sqrt(3))
    C_a = 6 * N
    q_limit_a = floor_c_div_q_sqrt3(C_a, 1)

    t = 1
    while t * (t + 3) <= q_limit_a:
        if t % 3 != 0:
            n_max = (q_limit_a // t - t) // 3
            for n in range(1, n_max + 1):
                if gcd(n, t) != 1: continue
                q = t * (3 * n + t)
                k = floor_c_div_q_sqrt3(C_a, q)
                total += k
        t += 1

    print(total)

solve()
