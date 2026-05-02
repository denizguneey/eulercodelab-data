# Problem 191: Prize Strings
# Count attendance strings of length 30 with at most 1 L and no 3 consecutive A's.

def solve():
    days = 30
    # dp[late_used][consecutive_absent]
    dp = [[0]*3 for _ in range(2)]
    dp[0][0] = 1
    for day in range(days):
        nxt = [[0]*3 for _ in range(2)]
        for late in range(2):
            for a in range(3):
                w = dp[late][a]
                if w == 0: continue
                nxt[late][0] += w  # On time
                if a < 2: nxt[late][a+1] += w  # Absent
                if late == 0: nxt[1][0] += w  # Late
        dp = nxt
    print(sum(dp[l][a] for l in range(2) for a in range(3)))

solve()
