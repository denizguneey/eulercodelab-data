from math import gcd

def solve():
    num_segments = 5000
    s = [0] * (4 * num_segments + 1)
    s[0] = 290797
    for i in range(4 * num_segments):
        s[i + 1] = (s[i] * s[i]) % 50515093

    segs = []
    for i in range(num_segments):
        ax = s[4 * i + 1] % 500
        ay = s[4 * i + 2] % 500
        bx = s[4 * i + 3] % 500
        by = s[4 * i + 4] % 500
        segs.append((ax, ay, bx, by))

    def cross(ax, ay, bx, by, cx, cy):
        return (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)

    def sgn(x):
        return (x > 0) - (x < 0)

    def intersection_point(s1, s2):
        a1 = s1[3] - s1[1]
        b1 = s1[0] - s1[2]
        c1 = a1 * s1[0] + b1 * s1[1]
        a2 = s2[3] - s2[1]
        b2 = s2[0] - s2[2]
        c2 = a2 * s2[0] + b2 * s2[1]
        den = a1 * b2 - a2 * b1
        x_num = c1 * b2 - c2 * b1
        y_num = a1 * c2 - a2 * c1
        if den < 0:
            den = -den
            x_num = -x_num
            y_num = -y_num
        gx = gcd(abs(x_num), den)
        gy = gcd(abs(y_num), den)
        return (x_num // gx, den // gx, y_num // gy, den // gy)

    points = set()
    for i in range(len(segs)):
        si = segs[i]
        for j in range(i + 1, len(segs)):
            sj = segs[j]
            c1 = cross(si[0], si[1], si[2], si[3], sj[0], sj[1])
            c2 = cross(si[0], si[1], si[2], si[3], sj[2], sj[3])
            c3 = cross(sj[0], sj[1], sj[2], sj[3], si[0], si[1])
            c4 = cross(sj[0], sj[1], sj[2], sj[3], si[2], si[3])
            if sgn(c1) * sgn(c2) >= 0 or sgn(c3) * sgn(c4) >= 0:
                continue
            points.add(intersection_point(si, sj))

    return str(len(points))

if __name__ == '__main__':
    print(solve())
