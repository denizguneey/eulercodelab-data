# Problem 215: Crack-free Walls
# Count ways to build a 32-wide, 10-high wall with 2x1 and 3x1 bricks
# such that no vertical crack extends through two consecutive rows.

def solve():
    width = 32
    height = 10

    # Generate all valid row layouts as bitmasks of internal crack positions
    rows = []
    def gen(pos, mask):
        if pos == width:
            rows.append(mask)
            return
        for brick in (2, 3):
            nxt = pos + brick
            if nxt > width:
                continue
            nmask = mask
            if nxt < width:
                nmask |= (1 << nxt)
            gen(nxt, nmask)
    gen(0, 0)

    n = len(rows)
    # Build compatibility: two rows are compatible if they share no internal cracks
    compatible = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if (rows[i] & rows[j]) == 0:
                compatible[i].append(j)

    # DP: dp[i] = number of ways to end with row pattern i
    dp = [1] * n
    for _ in range(1, height):
        nxt = [0] * n
        for i in range(n):
            s = 0
            for j in compatible[i]:
                s += dp[j]
            nxt[i] = s
        dp = nxt

    print(sum(dp))

solve()
