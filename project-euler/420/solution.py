import math

def solve():
    n = 10000000
    two_n = 2 * n

    def isqrt(x):
        r = int(math.isqrt(x))
        while (r+1)*(r+1) <= x: r += 1
        while r*r > x: r -= 1
        return r

    p_max = isqrt(two_n - 1)
    n_global = isqrt((two_n - 1) // 5)
    l_max = (n_global * n_global) // 4

    tau = [0] * (l_max + 1)
    for d in range(1, l_max + 1):
        for x in range(d, l_max + 1, d):
            tau[x] += 1

    total = 0
    for p in range(2, p_max + 1):
        p2 = p * p
        p_odd = p & 1
        for q in range(1, p):
            if math.gcd(p, q) != 1: continue
            pq2 = p2 + q * q
            n_max = isqrt((two_n - 1) // pq2)
            mixed = (p ^ q) & 1
            for nn in range(1, n_max + 1):
                if mixed and (nn & 1): continue
                m_max = (q * nn - 1) // p
                if m_max < 0: continue
                parity = (nn & 1) if (p_odd and (q & 1)) else 0
                m = -m_max
                if (m & 1) != parity: m += 1
                n2 = nn * nn
                while m <= m_max:
                    l_num = n2 - m * m
                    if l_num > 0:
                        l = l_num // 4
                        total += tau[l]
                    m += 2

    return str(total)

if __name__ == '__main__':
    print(solve())
