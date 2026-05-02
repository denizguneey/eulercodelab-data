# Problem 181: Investigating in how many ways objects of two different colours can be grouped.
# Partition (40 black, 60 white) into groups of (b,w) objects.

def solve():
    black, white = 40, 60
    # Group types: all (b,w) with b+w > 0
    types = [(b, w) for b in range(black+1) for w in range(white+1) if b+w > 0]
    dp = [[0]*(white+1) for _ in range(black+1)]
    dp[0][0] = 1
    for tb, tw in types:
        for b in range(black, -1, -1):
            for w in range(white, -1, -1):
                base = dp[b][w]
                if base == 0: continue
                if tb == 0: mr = (white-w)//tw if tw > 0 else 0
                elif tw == 0: mr = (black-b)//tb
                else: mr = min((black-b)//tb, (white-w)//tw)
                for k in range(1, mr+1):
                    dp[b+k*tb][w+k*tw] += base
    print(dp[black][white])

solve()
