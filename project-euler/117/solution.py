# Problem 117: Red, green, and blue tiles
# Replace with tiles of sizes 2,3,4 (mixing allowed).

def solve():
    length = 50
    dp = [0] * (length + 1)
    dp[0] = 1
    for n in range(1, length + 1):
        dp[n] = dp[n - 1]
        if n >= 2: dp[n] += dp[n - 2]
        if n >= 3: dp[n] += dp[n - 3]
        if n >= 4: dp[n] += dp[n - 4]
    print(dp[length])

solve()
