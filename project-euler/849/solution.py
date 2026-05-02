def solve():
    MOD = 1000000007
    n = 100
    S = 2*n*(n-1); V = 4*(n-1); W = S+1

    dp = [0]*((V+1)*W)
    for v in range(V+1): dp[v*W + v] = 1

    for i in range(2, n+1):
        ndp = [0]*((V+1)*W)
        low = 2*i*(i-1)
        for t in range(S+1):
            run = 0
            for v in range(V+1):
                run += dp[v*W + t]
                if run >= MOD: run -= MOD
                s = t + v
                if s <= S and s >= low:
                    ndp[v*W + s] = run
        dp = ndp

    ans = 0
    for v in range(V+1):
        ans += dp[v*W + S]
        if ans >= MOD: ans -= MOD
    return str(ans)

if __name__ == '__main__':
    print(solve())
