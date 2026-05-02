import math
import heapq

def solve():
    PI = math.pi

    def edge_risk(a, b, r):
        dot = a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
        c = dot / (r * r)
        c = max(-1.0, min(1.0, c))
        t = math.acos(c) / PI
        return t * t

    def generate_reduced_points(r):
        asin_pi = [math.asin(z / r) / PI for z in range(r + 1)]
        rr = r * r
        pts = []
        z0 = r
        x = 0
        while 3 * x * x < rr:
            y = x
            z = z0
            h = x*x + y*y + z*z - rr
            while h > 0:
                h -= 2*z - 1
                z -= 1
            z0 = z
            while y <= z:
                if h == 0:
                    if y == 0:
                        pts.append((0, 0, r))
                        pts.append((0, r, 0))
                    elif x == 0:
                        pts.append((0, y, z))
                        pts.append((0, z, y))
                        pts.append((y, z, 0))
                    elif y == z:
                        pts.append((x, y, y))
                        pts.append((y, y, x))
                    elif x == y:
                        pts.append((x, x, z))
                        pts.append((x, z, x))
                    else:
                        pts.append((x, y, z))
                        pts.append((x, z, y))
                        pts.append((y, z, x))
                h += 2*y + 1
                y += 1
                if h > 0:
                    h -= 2*z - 1
                    z -= 1
            x += 1
        pts.sort(key=lambda p: (-p[2], -p[1], -p[0]))
        seen = set()
        unique = []
        for p in pts:
            if p not in seen:
                seen.add(p)
                unique.append(p)
        return unique, asin_pi

    def dijkstra_pruned(pts, asin_pi, r, riskmax):
        n = len(pts)
        if n < 2: return float('inf')
        risk = [2.0] * n
        done = [False] * n
        cur = 0
        risk[0] = 0.0
        while True:
            done[cur] = True
            pc = pts[cur]
            rc = risk[cur]
            for j in range(n):
                if done[j]: continue
                pj = pts[j]
                if riskmax > 0:
                    dmax = riskmax - 2.0 * rc
                    f = asin_pi[pc[2]] - asin_pi[pj[2]]
                    if f*f > dmax:
                        if j > cur: break
                        continue
                nd = rc + edge_risk(pc, pj, r)
                if nd < risk[j]:
                    risk[j] = nd
            nxt = -1
            best = 2.0
            for j in range(n):
                if not done[j] and risk[j] < best:
                    best = risk[j]
                    nxt = j
            if nxt < 0: break
            cur = nxt
        ans = 2.0
        for i in range(n):
            e = 2.0 * asin_pi[pts[i][2]]
            cand = 2.0 * risk[i] + e * e
            if cand < ans: ans = cand
        return ans

    def minimal_risk_fast(r):
        pts, asin_pi = generate_reduced_points(r)
        if len(pts) < 2: return float('inf')
        d = 0.0
        for stride in [27, 9, 3, 1]:
            sample = pts[::stride] if stride > 1 else pts
            if len(sample) < 2: continue
            d = dijkstra_pruned(sample, asin_pi, r, d)
        return d

    total = 0.0
    for n in range(1, 16):
        r = (1 << n) - 1
        total += minimal_risk_fast(r)
    return f"{total:.10f}"

if __name__ == '__main__':
    print(solve())
