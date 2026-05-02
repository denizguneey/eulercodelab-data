import math

def solve():
    w, h = 4, 4; n = w*h
    xs = [0]*n; ys = [0]*n
    for y in range(h):
        for x in range(w):
            xs[y*w+x] = x; ys[y*w+x] = y

    between = [0]*(n*n)
    for i in range(n):
        for j in range(n):
            if i == j: continue
            dx = xs[j]-xs[i]; dy = ys[j]-ys[i]
            g = math.gcd(abs(dx), abs(dy))
            if g <= 1: continue
            sx, sy = dx//g, dy//g; mask = 0
            cx, cy = xs[i], ys[i]
            for t in range(1, g): cx += sx; cy += sy; mask |= 1<<(cy*w+cx)
            between[i*n+j] = mask

    memo = {}
    def dfs(used, last):
        key = (used, last)
        if key in memo: return memo[key]
        ans = 0; free = ((1<<n)-1) ^ used
        bit = 1
        for nxt in range(n):
            if free & bit:
                need = between[last*n+nxt]
                if (need & free) == 0:
                    ans += 1 + dfs(used|bit, nxt)
            bit <<= 1
        memo[key] = ans; return ans

    total = 0
    for s in range(n): total += dfs(1<<s, s)
    return str(total)

if __name__ == '__main__':
    print(solve())
