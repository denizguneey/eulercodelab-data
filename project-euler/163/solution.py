import math

def solve():
    SIZE = 36
    EPS = 1e-10
    h = math.sqrt(3.0) / 2.0

    a = (0.0, 0.0)
    b = (1.0, 0.0)
    c = (0.5, h)
    ab = ((a[0]+b[0])*0.5, (a[1]+b[1])*0.5)
    ac = ((a[0]+c[0])*0.5, (a[1]+c[1])*0.5)
    bc = ((b[0]+c[0])*0.5, (b[1]+c[1])*0.5)

    lines = []
    for i in range(SIZE):
        y = i * h
        lines.append((a[1]-0.0, b[0]-a[0], b[0]*a[1]-a[0]*0.0 + y*(b[0]-a[0])))
    # Rebuild properly using line equation ax+by=c from two points
    def make_line(p, q):
        a_l = p[1] - q[1]
        b_l = q[0] - p[0]
        c_l = q[0]*p[1] - p[0]*q[1]
        return (a_l, b_l, c_l)

    lines = []
    for i in range(SIZE):
        y = i * h
        lines.append(make_line((0.0, y), (1.0, y)))
    for i in range(SIZE):
        x = float(i)
        lines.append(make_line((x, 0.0), (bc[0]+x, bc[1])))
        if i > 0:
            lines.append(make_line((-x, 0.0), (bc[0]-x, bc[1])))
    for i in range(SIZE):
        x = float(i)
        lines.append(make_line((x, 0.0), (c[0]+x, c[1])))
    for i in range(SIZE):
        x = float(i)
        lines.append(make_line((x+1.0, 0.0), (c[0]+x, c[1])))
    for i in range(2*SIZE - 1):
        x = float(i)
        lines.append(make_line((x+1.0, 0.0), (ac[0]+x, ac[1])))
    for i in range(1, 2*SIZE):
        x = float(i) * c[0]
        lines.append(make_line((x, 0.0), (x, h)))

    n = len(lines)
    A = (0.0, 0.0)
    B = (float(SIZE), 0.0)
    C = (0.5*SIZE, h*SIZE)

    def intersect(l1, l2):
        det = l1[0]*l2[1] - l2[0]*l1[1]
        if abs(det) < EPS:
            return None
        x = (l1[2]*l2[1] - l2[2]*l1[1]) / det
        y = (l1[0]*l2[2] - l2[0]*l1[2]) / det
        return (x, y)

    def line_det(p, q, r):
        return (q[0]-p[0])*(r[1]-p[1]) - (q[1]-p[1])*(r[0]-p[0])

    def inside(p):
        if line_det(A, B, p) < -EPS: return False
        if line_det(B, C, p) < -EPS: return False
        if line_det(C, A, p) < -EPS: return False
        return True

    pair_data = [[None]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            pt = intersect(lines[i], lines[j])
            if pt and inside(pt):
                pair_data[i][j] = pt

    count = 0
    for i in range(n):
        for j in range(i+1, n):
            ij = pair_data[i][j]
            if ij is None:
                continue
            for k in range(j+1, n):
                ik = pair_data[i][k]
                jk = pair_data[j][k]
                if ik is None or jk is None:
                    continue
                if abs(ij[0]-ik[0]) < EPS and abs(ij[1]-ik[1]) < EPS:
                    continue
                if abs(ij[0]-jk[0]) < EPS and abs(ij[1]-jk[1]) < EPS:
                    continue
                if abs(ik[0]-jk[0]) < EPS and abs(ik[1]-jk[1]) < EPS:
                    continue
                count += 1

    return str(count)

if __name__ == '__main__':
    print(solve())
