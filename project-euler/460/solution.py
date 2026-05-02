import math

def solve():
    d = 10000
    window = 30
    radial_eps = 0.5
    w = d // 2
    h = w
    INF = float('inf')

    g = [[INF] * (w + 1) for _ in range(h + 1)]
    g[1][0] = 0.0

    log_y = [0.0] * (h + 1)
    for y in range(1, h + 1):
        log_y[y] = math.log(y)

    x_ref = [0] * (h + 1)
    for y in range(1, h + 1):
        inner = w * w - y * y
        x_ref[y] = w - int(math.sqrt(max(0, inner)))

    # Precompute source_y for each x0
    source_y = [[] for _ in range(w)]
    outer2 = (w + radial_eps) ** 2
    inner_r = max(0.0, w - radial_eps)
    inner2 = inner_r ** 2
    for x0 in range(w):
        dx = w - x0
        dx2 = dx * dx
        low = inner2 - dx2
        high = outer2 - dx2
        if high < 1.0: continue
        y_lo = max(1, math.ceil(math.sqrt(max(0.0, low))))
        y_hi = min(h, int(math.sqrt(max(0.0, high))))
        for y0 in range(y_lo, y_hi + 1):
            r = math.sqrt(dx2 + y0 * y0)
            if abs(r - w) <= radial_eps + 1e-12:
                source_y[x0].append(y0)

    best_half = INF
    for x0 in range(w):
        for y0 in source_y[x0]:
            base = g[y0][x0]
            if not math.isfinite(base): continue
            for y in range(y0, h + 1):
                dy = y - y0
                inv_v = (1.0 / y0) if dy == 0 else (log_y[y] - log_y[y0]) / dy
                xr = x_ref[y]
                lx = max(x0, xr - window)
                rx = min(w, xr + 1)
                for x in range(lx, rx + 1):
                    dxi = x - x0
                    length = math.sqrt(dxi * dxi + dy * dy) * inv_v
                    cand = base + length
                    if cand < g[y][x]:
                        g[y][x] = cand
                        if x == w and cand < best_half:
                            best_half = cand

    return f'{2.0 * best_half:.9f}'

if __name__ == '__main__':
    print(solve())
