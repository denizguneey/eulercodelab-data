import math

def solve():
    n = 100000000000000

    def isqrt(x):
        r = int(math.isqrt(x))
        while (r+1)*(r+1) <= x: r += 1
        while r*r > x: r -= 1
        return r

    def gauss_points(x):
        if x < 0: return 0
        r = isqrt(x); b = r; b2 = b*b; a2 = 0; s = 0
        for a in range(r+1):
            while a2 + b2 > x: b -= 1; b2 -= 2*b+1
            s += b; a2 += 2*a+1
        return 1 + 4*s

    limit = isqrt(n)
    # SPF sieve
    spf = list(range(limit+1))
    for p in range(2, int(limit**0.5)+1):
        if spf[p] == p:
            for j in range(p*p, limit+1, p):
                if spf[j] == j: spf[j] = p

    def local_g(p, exp):
        if p == 2: return -1 if exp == 1 else 0
        if p % 4 == 1: return -2 if exp == 1 else (1 if exp == 2 else 0)
        return -1 if exp == 2 else 0

    g = [0]*(limit+1); g[1] = 1
    for m in range(2, limit+1):
        p = spf[m]; t = m; exp = 0
        while t % p == 0: t //= p; exp += 1
        lg = local_g(p, exp)
        g[m] = 0 if lg == 0 or g[t] == 0 else lg * g[t]

    prefix = [0]*(limit+1)
    for i in range(1, limit+1): prefix[i] = prefix[i-1] + g[i]

    groups = []; m = 1
    while m <= limit:
        k = n // (m*m); mm = isqrt(n // k)
        groups.append((m, mm, k)); m = mm + 1

    total = 0
    for l, r, k in groups:
        sg = prefix[r] - prefix[l-1]
        total += sg * (gauss_points(k) - 1)

    return str(total // 4)

if __name__ == '__main__':
    print(solve())
