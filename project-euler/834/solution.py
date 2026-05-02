def solve():
    N = 1234567
    spf = list(range(N+1))
    for i in range(2, int(N**0.5)+1):
        if spf[i] == i:
            for j in range(i*i, N+1, i):
                if spf[j] == j: spf[j] = i

    def factor(x):
        fac = {}
        while x > 1:
            p = spf[x]; e = 0
            while x % p == 0: x //= p; e += 1
            fac[p] = fac.get(p, 0) + e
        return fac

    def T(n):
        a, b = n, n-1
        t = 0
        while a % 2 == 0: a >>= 1; t += 1
        while b % 2 == 0: b >>= 1; t += 1
        fac = {}
        for d in (factor(a), factor(b)):
            for p, e in d.items(): fac[p] = fac.get(p, 0) + e
        pf = list(fac.items())
        ans = 0
        def dfs(idx, cur):
            nonlocal ans
            if idx == len(pf):
                if cur > n: ans += cur - n
                d2 = cur << t
                if d2 > n: ans += d2 - n
                return
            p, e = pf[idx]; v = 1
            for _ in range(e+1):
                dfs(idx+1, cur*v); v *= p
        dfs(0, 1)
        return ans

    total = 0
    for n in range(3, N+1): total += T(n)
    return str(total)

if __name__ == '__main__':
    print(solve())
