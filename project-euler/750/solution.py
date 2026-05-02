def solve():
    n = 976; mod = n + 1
    pos = [0]*(n+1); val = 1
    for i in range(1, n+1):
        val = 3*val % mod; pos[val] = i

    INF = 1 << 60
    dp = [[0]*(n+1) for _ in range(n+1)]
    for length in range(2, n+1):
        for l in range(1, n-length+2):
            r = l + length - 1; best = INF
            pr = pos[r]
            for m in range(l, r):
                cand = dp[l][m] + dp[m+1][r] + abs(pos[m] - pr)
                if cand < best: best = cand
            dp[l][r] = best

    return str(dp[1][n])

if __name__ == '__main__':
    print(solve())
