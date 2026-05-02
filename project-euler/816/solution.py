import math
from sortedcontainers import SortedList

def solve():
    K = 2_000_000
    MOD = 50515093

    s = 290797
    pts = []
    for _ in range(K):
        x = s
        s = s * s % MOD
        y = s
        s = s * s % MOD
        pts.append((x, y))

    pts.sort()
    best2 = (pts[0][0] - pts[1][0])**2 + (pts[0][1] - pts[1][1])**2

    active = SortedList(key=lambda t: (t[1], t[0], t[2]))
    active.add((pts[0][0], pts[0][1], 0))
    left = 0

    for i in range(1, K):
        d = math.sqrt(float(best2))
        while left < i:
            dx = pts[i][0] - pts[left][0]
            if float(dx) <= d: break
            active.remove((pts[left][0], pts[left][1], left))
            left += 1

        y_lo = pts[i][1] - int(d) - 1
        y_hi = pts[i][1] + int(d) + 1

        idx_lo = active.bisect_left((0, y_lo, -1))
        idx_hi = active.bisect_right((10**9, y_hi, 10**9))

        for j in range(idx_lo, min(idx_hi, len(active))):
            item = active[j]
            if item[1] > y_hi: break
            dx = pts[i][0] - item[0]
            dy = pts[i][1] - item[1]
            dd = dx*dx + dy*dy
            if dd < best2:
                best2 = dd

        active.add((pts[i][0], pts[i][1], i))

    ans = math.sqrt(float(best2))
    return f"{ans:.9f}"

if __name__ == '__main__':
    print(solve())
