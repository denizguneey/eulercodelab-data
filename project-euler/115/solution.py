# Problem 115: Counting block combinations II
# Find minimum n where count_ways(n, 50) exceeds 1 million.

def count_ways(length, min_block):
    dp = [0] * (length + 1)
    dp[0] = 1
    for n in range(1, length + 1):
        dp[n] = dp[n - 1]
        for block in range(min_block, n + 1):
            dp[n] += 1 if block == n else dp[n - block - 1]
    return dp[length]

def solve():
    n = 0
    while True:
        if count_ways(n, 50) > 1000000:
            print(n)
            return
        n += 1

solve()
