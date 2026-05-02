import math

def solve():
    def gauss_legendre_01(n):
        x = [0.0] * n
        w = [0.0] * n
        m = (n + 1) // 2
        pi = math.pi
        for i in range(m):
            z = math.cos(pi * (i + 0.75) / (n + 0.5))
            for _ in range(100):
                p1, p2 = 1.0, 0.0
                for j in range(1, n + 1):
                    p3 = p2; p2 = p1
                    p1 = ((2*j - 1) * z * p2 - (j - 1) * p3) / j
                pp = n * (z * p1 - p2) / (z * z - 1.0)
                z1 = z
                z = z1 - p1 / pp
                if abs(z - z1) < 1e-18: break
            p1, p2 = 1.0, 0.0
            for j in range(1, n + 1):
                p3 = p2; p2 = p1
                p1 = ((2*j - 1) * z * p2 - (j - 1) * p3) / j
            pp = n * (z * p1 - p2) / (z * z - 1.0)
            ww = 2.0 / ((1.0 - z*z) * pp*pp)
            x[i] = -z; x[n-1-i] = z
            w[i] = ww; w[n-1-i] = ww
        for i in range(n):
            x[i] = 0.5 * (x[i] + 1.0)
            w[i] *= 0.5
        return x, w

    n = 1024
    xq, wq = gauss_legendre_01(n)
    pi = math.pi
    integral = 0.0
    for i in range(n):
        u = xq[i]; wu = wq[i]
        omu = 1.0 - u
        px = 40.0 * u
        jac = 1200.0 * omu
        for j in range(n):
            v = xq[j]; wv = wq[j]
            py = 30.0 * omu * v
            ux, uy = 40.0 - px, -py
            vx, vy = -px, 30.0 - py
            cross = ux * vy - uy * vx
            dot = ux * vx + uy * vy
            theta = math.atan2(abs(cross), dot)
            integral += wu * wv * theta * jac

    ans = integral / (1200.0 * pi)
    return f"{ans:.10f}"

if __name__ == '__main__':
    print(solve())
