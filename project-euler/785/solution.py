import math

def solve():
    N = 1000000000
    G = [1, 4, 16, 19, 64, 76, 304, 1216]
    lo_r = 5/3
    hi_r = (103 - 4*math.sqrt(19)) / 45

    def cidx(g):
        return {1:0, 4:1, 16:2, 19:3, 64:4, 76:5, 304:6, 1216:7}[g]

    def tz16(x):
        x &= 15
        if x == 0: return 4
        c = 0
        while (x & 1) == 0: x >>= 1; c += 1
        return c

    # Build residue table
    table = [[[] for _ in range(304)] for _ in range(8)]
    for vm in range(304):
        for um in range(304):
            m16 = (5*um - 3*vm) & 15; n16 = (3*um - 5*vm) & 15
            tz = min(tz16(m16), tz16(n16), 3)
            g2 = [1, 4, 16, 64][tz]
            m19 = (5*um - 3*vm) % 19
            e19 = m19 == 0
            g = g2 * (19 if e19 else 1)
            table[cidx(g)][vm].append(um)

    cmin = 32*hi_r*hi_r - 176*hi_r + 240
    ans = 0
    for ci in range(8):
        g = G[ci]; vmax = int(math.sqrt(N * g / cmin)) + 3
        for v in range(1, vmax+1):
            umin = int(math.floor(lo_r * v)) + 1
            umax = int(math.floor(hi_r * v))
            if umin > umax: continue
            for r in table[ci][v % 304]:
                delta = (r - umin % 304 + 304) % 304
                first = umin + delta
                for u in range(first, umax+1, 304):
                    if math.gcd(u, v) != 1: continue
                    z0 = 32*u*u - 176*u*v + 240*v*v
                    if z0 > N * g: continue
                    x0 = 15*u*u - 34*u*v + 15*v*v
                    y0 = 105*u*u - 446*u*v + 473*v*v
                    ans += x0//g + y0//g + z0//g

    return str(ans)

if __name__ == '__main__':
    print(solve())
