import math

def solve():
    N = 3141592653589793

    def isqrt(x):
        r = int(math.isqrt(x))
        while (r+1)*(r+1) <= x: r += 1
        while r*r > x: r -= 1
        return r

    def icbrt(x):
        r = round(x ** (1/3))
        while (r+1)**3 <= x: r += 1
        while r**3 > x: r -= 1
        return r

    def helper(L):
        res = 0
        m0sq = 0.25 + (L-1)/2.0
        m0 = int(0.5 + math.sqrt(m0sq))
        K = m0 // 2
        res += K * K
        m = 2*K + 1
        n = isqrt(max(0, L - m*m))
        while True:
            z = max(0, L - m*m)
            if z == 0: break
            while n*n > z: n -= 1
            res += n // 2
            m += 1
            z = max(0, L - m*m)
            if z == 0: break
            while n*n > z: n -= 1
            res += (n+1) // 2
            m += 1
        return res

    L = icbrt(N)
    v = [0] * (L + 1)
    for x in range(1, L + 1):
        res = helper(x)
        c = icbrt(x)
        for g in range(3, c+1, 2):
            res -= v[x // (g*g)]
        prev_y = (isqrt(x) - 1) // 2
        z_end = c + (1 if x // (c*c) != c else 0)
        for z in range(1, z_end):
            y = (isqrt(x // (z+1)) - 1) // 2
            res -= (prev_y - y) * v[z]
            prev_y = y
        v[x] = res

    bigV = [0] * (L // 2 + 1)
    for a in range((L-1)//2, -1, -1):
        x = 2*a + 1
        k = N // (x*x)
        res = helper(k)
        c = icbrt(k)
        for b in range(1, (c-1)//2 + 1):
            g = 2*b + 1
            k_gg = k // (g*g)
            if k_gg <= L:
                res -= v[k_gg]
            else:
                idx = 2*a*b + a + b
                res -= bigV[idx]
        prev_y = (isqrt(k) - 1) // 2
        z_end = c + (1 if k // (c*c) != c else 0)
        for z in range(1, z_end):
            y = (isqrt(k // (z+1)) - 1) // 2
            res -= (prev_y - y) * v[z]
            prev_y = y
        bigV[a] = res

    return str(bigV[0])

if __name__ == '__main__':
    print(solve())
