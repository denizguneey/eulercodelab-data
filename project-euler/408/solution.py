import math

def solve():
    N = 10_000_000
    MOD = 1_000_000_007

    def mod_pow(base, exp, mod):
        result = 1
        cur = base % mod
        e = exp
        while e > 0:
            if e & 1: result = result * cur % mod
            cur = cur * cur % mod
            e >>= 1
        return result

    maxv = 2 * N
    fact = [1] * (maxv + 1)
    for i in range(1, maxv + 1):
        fact[i] = fact[i-1] * i % MOD
    inv_fact = [1] * (maxv + 1)
    inv_fact[maxv] = mod_pow(fact[maxv], MOD - 2, MOD)
    for i in range(maxv, 0, -1):
        inv_fact[i-1] = inv_fact[i] * i % MOD

    def nCr(n, r):
        if r < 0 or r > n: return 0
        return fact[n] * inv_fact[r] % MOD * inv_fact[n-r] % MOD

    # Find inadmissible points (a², b²) where a²+b² is a perfect square
    lim = int(math.isqrt(N))
    lim2 = int(math.isqrt(2 * N))
    is_sq = set(c*c for c in range(1, lim2+1))

    pts = set()
    for a in range(1, lim+1):
        a2 = a * a
        for b in range(1, lim+1):
            b2 = b * b
            if a2 + b2 in is_sq:
                pts.add((a2, b2))
    pts = sorted(pts)

    m = len(pts)
    ways = [0] * m
    for i in range(m):
        xi, yi = pts[i]
        w = nCr(xi + yi, xi)
        for j in range(i):
            xj, yj = pts[j]
            if xj <= xi and yj <= yi:
                paths = nCr((xi-xj)+(yi-yj), xi-xj)
                w = (w - ways[j] * paths) % MOD
        ways[i] = w % MOD

    ans = nCr(2*N, N)
    for i in range(m):
        x, y = pts[i]
        tail = nCr((N-x)+(N-y), N-x)
        ans = (ans - ways[i] * tail) % MOD

    return str(ans % MOD)

if __name__ == '__main__':
    print(solve())
