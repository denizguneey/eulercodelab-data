import math

def solve():
    n = 2500
    S = 290797
    pts = []
    for _ in range(n):
        S = S * S % 50515093
        x = S % 2000 - 1000
        S = S * S % 50515093
        y = S % 2000 - 1000
        pts.append((x, y))

    lines = set()
    for i in range(n):
        x1, y1 = pts[i]
        for j in range(i + 1, n):
            x2, y2 = pts[j]
            dx = x2 - x1
            dy = y2 - y1
            if dx == 0 and dy == 0: continue
            g = math.gcd(abs(dx), abs(dy))
            dx //= g; dy //= g
            A = dy; B = -dx
            C = A * x1 + B * y1
            if A < 0 or (A == 0 and B < 0):
                A, B, C = -A, -B, -C
            lines.add((A, B, C))

    lines_list = sorted(lines)
    M = len(lines_list)

    # Count parallel pairs (same slope = same (A, B))
    from itertools import groupby
    parallel2 = 0
    for _, group in groupby(lines_list, key=lambda l: (l[0], l[1])):
        m = sum(1 for _ in group)
        parallel2 += m * (m - 1)

    ans = M * (M - 1) - parallel2
    return str(ans)

if __name__ == '__main__':
    print(solve())
