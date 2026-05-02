# Problem 164: Numbers for which no three consecutive digits have a sum > 9

def solve():
    length = 20
    # dp[a][b] = ways to form number ending in digits (a, b)
    dp = [[0]*10 for _ in range(10)]
    for d1 in range(1, 10):
        for d2 in range(10):
            dp[d1][d2] = 1
    for pos in range(3, length + 1):
        nxt = [[0]*10 for _ in range(10)]
        for a in range(10):
            for b in range(10):
                if dp[a][b] == 0: continue
                for c in range(10):
                    if a + b + c > 9: continue
                    nxt[b][c] += dp[a][b]
        dp = nxt
    print(sum(dp[a][b] for a in range(10) for b in range(10)))

solve()
