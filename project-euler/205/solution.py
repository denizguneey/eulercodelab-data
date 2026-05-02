# Problem 205: Dice Game
# Pete has 9 four-sided dice, Colin has 6 six-sided dice.
# What is the probability that Pete beats Colin? (7 decimal places)

def solve():
    def distribution(dice, sides):
        dp = [0] * (dice * sides + 1)
        dp[0] = 1
        for _ in range(dice):
            nxt = [0] * (dice * sides + 1)
            for s in range(len(dp)):
                if dp[s] == 0: continue
                for f in range(1, sides+1):
                    if s + f < len(nxt):
                        nxt[s+f] += dp[s]
            dp = nxt
        return dp

    pete = distribution(9, 4)
    colin = distribution(6, 6)
    wins = 0
    total = 0
    for p in range(len(pete)):
        if pete[p] == 0: continue
        for c in range(len(colin)):
            if colin[c] == 0: continue
            ways = pete[p] * colin[c]
            total += ways
            if p > c:
                wins += ways
    print(f"{wins/total:.7f}")

solve()
