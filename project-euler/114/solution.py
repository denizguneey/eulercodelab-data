# Problem 114: Counting block combinations I
# Row of 50 units, fill with red blocks (min length 3) separated by gaps.

def solve():
    length = 50
    dp = [0] * (length + 1)
    dp[0] = 1
    for n in range(1, length + 1):
        dp[n] = dp[n - 1]
        for block in range(3, n + 1):
            if block == n:
                dp[n] += 1
            else:
                dp[n] += dp[n - block - 1]
    print(dp[length])

solve()
