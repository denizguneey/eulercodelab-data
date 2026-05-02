# Problem 121: Disc game prize fund
# DP on probability of blue wins over 15 turns.

from fractions import Fraction

def solve():
    turns = 15
    # dp[b] = probability of getting exactly b blue discs
    dp = [Fraction(0)] * (turns + 1)
    dp[0] = Fraction(1)
    for t in range(1, turns + 1):
        new_dp = [Fraction(0)] * (turns + 1)
        p_blue = Fraction(1, t + 1)
        p_red = Fraction(t, t + 1)
        for b in range(t + 1):
            if dp[b] == 0: continue
            new_dp[b] += dp[b] * p_red
            if b + 1 <= turns:
                new_dp[b + 1] += dp[b] * p_blue
        dp = new_dp
    win_prob = sum(dp[b] for b in range(turns // 2 + 1, turns + 1))
    print(int(1 / win_prob))

solve()
