import math

def solve():
    n = 2000000
    x_mod, y_mod = 1248 % 32323, 8421 % 30103
    raw_dirs = []
    for _ in range(n):
        x = x_mod - 16161
        y = y_mod - 15051
        g = math.gcd(abs(x), abs(y))
        raw_dirs.append((x // g, y // g))
        x_mod = x_mod * 1248 % 32323
        y_mod = y_mod * 8421 % 30103

    raw_dirs.sort()
    unique = []
    for dx, dy in raw_dirs:
        if unique and unique[-1][0] == dx and unique[-1][1] == dy:
            unique[-1] = (dx, dy, unique[-1][2] + 1)
        else:
            unique.append((dx, dy, 1))

    W = S2 = S3 = 0
    for _, _, w in unique:
        W += w; S2 += w*w; S3 += w*w*w
    total_distinct = (W*W*W - 3*W*S2 + 2*S3) // 6

    # Boundary: collinear opposite pairs
    lookup = {}
    for i, (dx, dy, w) in enumerate(unique):
        lookup[(dx, dy)] = w

    boundary = 0
    for dx, dy, w in unique:
        ow = lookup.get((-dx, -dy), 0)
        if ow == 0: continue
        if (dx, dy) < (-dx, -dy):
            boundary += w * ow * (W - w - ow)

    # Angular sweep
    def half_plane(dx, dy):
        return 0 if (dy > 0 or (dy == 0 and dx > 0)) else 1

    by_angle = sorted(unique, key=lambda d: (half_plane(d[0], d[1]), -d[0]*1000000000+d[1]*1000000000))
    # Custom sort by angle
    def angle_key(d):
        h = half_plane(d[0], d[1])
        return (h, d)

    def angle_cmp_less(a, b):
        ha, hb = half_plane(a[0], a[1]), half_plane(b[0], b[1])
        if ha != hb: return ha < hb
        cross = a[0] * b[1] - a[1] * b[0]
        return cross > 0

    from functools import cmp_to_key
    by_angle = sorted(unique, key=cmp_to_key(lambda a, b: -1 if angle_cmp_less(a, b) else (1 if angle_cmp_less(b, a) else 0)))
    m = len(by_angle)

    weight2 = [d[2] for d in by_angle] * 2
    pref_w = [0] * (2*m+1)
    pref_w2 = [0] * (2*m+1)
    for i in range(2*m):
        pref_w[i+1] = pref_w[i] + weight2[i]
        pref_w2[i+1] = pref_w2[i] + weight2[i] * weight2[i]

    angle2 = by_angle * 2
    outside_open = 0
    j = 0
    for i in range(m):
        if j < i + 1: j = i + 1
        ax, ay = angle2[i][0], angle2[i][1]
        while j < i + m:
            bx, by_ = angle2[j][0], angle2[j][1]
            cross = ax * by_ - ay * bx
            if cross > 0: j += 1
            else: break
        S = pref_w[j] - pref_w[i+1]
        SS = pref_w2[j] - pref_w2[i+1]
        pair_weight = (S * S - SS) // 2
        outside_open += by_angle[i][2] * pair_weight

    return str(total_distinct - outside_open - boundary)

if __name__ == '__main__':
    print(solve())
