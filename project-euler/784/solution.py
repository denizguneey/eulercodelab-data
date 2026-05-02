def solve():
    n = 2000000
    spf = list(range(n+2))
    for i in range(2, int((n+1)**0.5)+1):
        if spf[i] == i:
            for j in range(i*i, n+2, i):
                if spf[j] == j: spf[j] = i

    def factorize(x):
        fac = []
        while x > 1:
            p = spf[x]; c = 0
            while x % p == 0: x //= p; c += 1
            fac.append((p, c))
        return fac

    ans = 0
    for r in range(2, n):
        m = min(r-1, n-r)
        if m <= 0: continue
        fa = factorize(r-1); fb = factorize(r+1)
        fac = dict(fa)
        for p, c in fb: fac[p] = fac.get(p, 0) + c
        factors = list(fac.items())
        sq1 = r*r - 1
        def dfs(idx, cur):
            nonlocal ans
            if idx == len(factors):
                if cur == 0 or cur > m: return
                d = cur; p_ = r + d; q_ = r + sq1 // d
                ans += p_ + q_; return
            pr, exp = factors[idx]; val = cur
            for e in range(exp+1):
                if val > m: break
                dfs(idx+1, val)
                if e == exp or val > m // pr: break
                val *= pr
        dfs(0, 1)

    return str(ans)

if __name__ == '__main__':
    print(solve())
