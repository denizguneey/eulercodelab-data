# Problem 178: Step Numbers (numbers where consecutive digits differ by exactly 1
# and all digits 0-9 appear at least once)

def solve():
    max_digits = 40
    ALL = (1 << 10) - 1
    # dp[len][mask][last_digit] = count
    dp = [[[0]*10 for _ in range(1 << 10)] for _ in range(max_digits+1)]
    for d in range(1, 10):
        dp[1][1 << d][d] = 1
    for ln in range(1, max_digits):
        for mask in range(1 << 10):
            for d in range(10):
                w = dp[ln][mask][d]
                if w == 0: continue
                if d > 0:
                    dp[ln+1][mask | (1<<(d-1))][d-1] += w
                if d < 9:
                    dp[ln+1][mask | (1<<(d+1))][d+1] += w
    ans = 0
    for ln in range(1, max_digits+1):
        for d in range(10):
            ans += dp[ln][ALL][d]
    print(ans)

solve()
