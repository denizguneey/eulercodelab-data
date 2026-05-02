import math

def H_value(p0, depth_limit):
    if p0 <= 0.0 or p0 >= 1.0:
        return 20.0

    ln2 = math.log(2.0)
    ln3 = math.log(3.0)
    log_odds0 = math.log(p0 / (1.0 - p0))

    n = depth_limit
    next_arr = [0.0] * (n + 1)
    base = log_odds0 - n * ln2
    
    for h in range(n + 1):
        z = base + h * ln3
        if z > 50.0:
            p = 1.0
        elif z < -50.0:
            p = 0.0
        else:
            o = math.exp(z)
            p = o / (1.0 + o)
            
        next_arr[h] = 70.0 * max(p, 1.0 - p) - 50.0

    for n in range(depth_limit - 1, -1, -1):
        cur = [0.0] * (n + 1)
        base_n = log_odds0 - n * ln2
        for h in range(n + 1):
            z = base_n + h * ln3
            if z > 50.0:
                p = 1.0
            elif z < -50.0:
                p = 0.0
            else:
                o = math.exp(z)
                p = o / (1.0 + o)

            stop = 70.0 * max(p, 1.0 - p) - 50.0
            qh = 0.5 + 0.25 * p
            cont = -1.0 + qh * next_arr[h + 1] + (1.0 - qh) * next_arr[h]
            cur[h] = max(stop, cont)
        next_arr = cur

    return next_arr[0]

def S_value(N, depth_limit):
    H = [[20.0] * (N + 1) for _ in range(N + 1)]
    for u in range(1, N + 1):
        for f in range(1, N + 1):
            H[u][f] = H_value(float(u) / float(u + f), depth_limit)

    V = [[0.0] * (N + 1) for _ in range(N + 1)]
    for u in range(1, N + 1):
        V[u][0] = 20.0 * u
    for f in range(1, N + 1):
        V[0][f] = 20.0 * f

    for u in range(1, N + 1):
        for f in range(1, N + 1):
            p = float(u) / float(u + f)
            V[u][f] = p * V[u - 1][f] + (1.0 - p) * V[u][f - 1] + H[u][f]

    return V[N][N]

def solve():
    depth_limit = 220
    ans = S_value(50, depth_limit)
    return f"{ans:.6f}"

if __name__ == "__main__":
    print(solve())
