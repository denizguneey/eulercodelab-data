import math

def solve():
    P = 10000000
    L = P // 2

    def gen_triples(limit):
        tris = []
        mmax = int(limit**0.5) + 2
        for m in range(2, mmax+1):
            for nn in range(1, m):
                if (m - nn) % 2 == 0: continue
                if math.gcd(m, nn) != 1: continue
                a0 = m*m - nn*nn; b0 = 2*m*nn; c0 = m*m + nn*nn
                if c0 > limit: continue
                kmax = limit // c0
                for k in range(1, kmax+1):
                    a, t, s = k*a0, k*b0, k*c0
                    tris.append((a, t, s)); tris.append((t, a, s))
        return tris

    def gen_rects(limit):
        max_leg = 2*limit; rects = []
        mmax = int(max_leg**0.5) + 2
        for m in range(2, mmax+1):
            for nn in range(1, m):
                if (m-nn) % 2 == 0: continue
                if math.gcd(m, nn) != 1: continue
                a0 = m*m - nn*nn; b0 = 2*m*nn
                max0 = max(a0, b0)
                if max0 > max_leg: continue
                kmax = max_leg // max0
                for k in range(1, kmax+1):
                    x, y = k*a0, k*b0
                    if x % 2 == 0:
                        a, h = x//2, y
                        if 0 < a <= limit and 0 < h <= limit: rects.append((a, h))
                    if y % 2 == 0:
                        a, h = y//2, x
                        if 0 < a <= limit and 0 < h <= limit: rects.append((a, h))
        return rects

    tris = gen_triples(L)
    rects = gen_rects(L)

    # Group by 'a'
    from collections import defaultdict
    tri_by_a = defaultdict(list); rect_by_a = defaultdict(list)
    for a, t, s in tris: tri_by_a[a].append((t, s))
    for a, h in rects: rect_by_a[a].append(h)

    total = 0
    for a in range(1, L+1):
        if a not in tri_by_a or a not in rect_by_a: continue
        ts = sorted(tri_by_a[a], key=lambda x: x[0])
        rs = sorted(rect_by_a[a])
        t_set = set(t for t, s in ts)
        for h in rs:
            limit_s = L - a - h
            if limit_s <= 0: break
            for t, s in ts:
                if t >= h: break
                if s > limit_s: break
                u = h + t
                if u > L: continue
                if u in t_set:
                    total += 2 * (a + h + s)

    return str(total)

if __name__ == '__main__':
    print(solve())
