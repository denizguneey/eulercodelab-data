import math

def solve():
    n_val = 12

    L = 1
    for d in range(1, n_val + 1): L = L * d // math.gcd(L, d)

    coords = set()
    for d in range(1, n_val + 1):
        q = L // d
        for num in range(-d + 1, d):
            coords.add(num * q)
    coords = sorted(coords)

    L2 = L * L
    pts = []
    for x in coords:
        x2 = x * x
        for y in coords:
            y2 = y * y
            if x2 + y2 < L2:
                pts.append((x * L, y * L, x2 + y2 + L2))

    count = 0
    for i in range(len(pts) - 2):
        px, py, pz = pts[i]
        keys = []
        for j in range(i + 1, len(pts)):
            qx, qy, qz = pts[j]
            if px == 0:
                u = qx; v = pz * qy - py * qz
            else:
                u = py * qx - px * qy; v = pz * qx - px * qz
            g = math.gcd(abs(u), abs(v))
            if g == 0: g = 1
            u //= g; v //= g
            if u < 0 or (u == 0 and v < 0): u, v = -u, -v
            keys.append((u, v))
        keys.sort()
        s = 0
        while s < len(keys):
            t = s + 1
            while t < len(keys) and keys[t] == keys[s]: t += 1
            cnt = t - s; count += cnt * (cnt - 1) // 2; s = t

    return str(6 * count)

if __name__ == '__main__':
    print(solve())
