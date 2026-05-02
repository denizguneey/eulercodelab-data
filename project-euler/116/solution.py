# Problem 116: Red, green or blue tiles
# Replace grey tiles with colored tiles (red=2, green=3, blue=4). No mixing.

def count_single_color(length, tile):
    dp = [0] * (length + 1)
    dp[0] = 1
    for n in range(1, length + 1):
        dp[n] = dp[n - 1]
        if n >= tile:
            dp[n] += dp[n - tile]
    return dp[length] - 1

def solve():
    print(count_single_color(50, 2) + count_single_color(50, 3) + count_single_color(50, 4))

solve()
