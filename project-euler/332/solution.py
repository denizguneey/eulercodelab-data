import math

def solve():
    def lattice_points_on_sphere(r):
        rr = r * r
        points = []
        for x in range(-r, r+1):
            x2 = x * x
            for y in range(-r, r+1):
                y2 = y * y
                z2 = rr - x2 - y2
                if z2 < 0:
                    continue
                z = round(math.sqrt(z2))
                if z * z != z2:
                    continue
                points.append((x, y, z))
                if z != 0:
                    points.append((x, y, -z))
        return points

    def dot(a, b):
        return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

    def abs_det(a, b, c):
        det = (a[0]*(b[1]*c[2]-b[2]*c[1]) -
               a[1]*(b[0]*c[2]-b[2]*c[0]) +
               a[2]*(b[0]*c[1]-b[1]*c[0]))
        return abs(det)

    def min_area(r):
        pts = lattice_points_on_sphere(r)
        n = len(pts)
        if n < 3:
            return 0.0
        dots = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                v = dot(pts[i], pts[j])
                dots[i][j] = v
                dots[j][i] = v

        best_det = None
        best_den = 1
        r2 = r * r

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    detv = abs_det(pts[i], pts[j], pts[k])
                    if detv == 0:
                        continue
                    sd = dots[i][j] + dots[i][k] + dots[j][k]
                    denv = r * r2 + r * sd
                    if denv <= 0:
                        continue
                    if best_det is None or detv * best_den < best_det * denv:
                        best_det = detv
                        best_den = denv

        if best_det is None:
            return 0.0
        omega = 2.0 * math.atan2(best_det, best_den)
        return r2 * omega

    total = 0.0
    for r in range(1, 51):
        total += min_area(r)
    return f"{total:.6f}"

if __name__ == '__main__':
    print(solve())
