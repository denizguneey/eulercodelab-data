def solve():
    MOD = 998388889; SEED = 102022661
    n = 10000000

    # Generate a, b
    a = [0]*(n+1); b = [0]*(n+1)
    s = SEED; sum_a = 0; sum_b = 0
    for i in range(1, n+1):
        a[i] = s; sum_a += s
        s = s * s % MOD; b[i] = s; sum_b += s
        if i != n: s = s * s % MOD

    # Lower hull
    edge = n - 1
    if edge == 0: return str(sum_a + sum_b)
    hull = []
    for t in range(edge + 1):
        while len(hull) >= 2:
            t1, t2 = hull[-2], hull[-1]
            x1 = t2 - t1; y1 = b[t2+1] - b[t1+1]
            x2 = t - t1; y2 = b[t+1] - b[t1+1]
            if x1*y2 - y1*x2 <= 0: hull.pop()
            else: break
        hull.append(t)

    m = len(hull)
    tv = [hull[k] for k in range(m)]
    gv = [b[hull[k]+1] for k in range(m)]
    prev = [0]*m
    INF = float('inf')

    for i in range(1, edge+1):
        u = a[i] - a[i+1]
        pref = INF; cur = [0]*m
        for k in range(m):
            if prev[k] < pref: pref = prev[k]
            cur[k] = pref + u * tv[k] + gv[k]
        prev = cur

    best = min(prev)
    return str(sum_a + sum_b + edge * a[n] + best)

if __name__ == '__main__':
    print(solve())
