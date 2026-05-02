# Problem 499: St. Petersburg Lottery

A gambler decides to participate in a special lottery. In this lottery the gambler plays a series of one or more games.  
Each game costs $m$ pounds to play and starts with an initial pot of $1$ pound. The gambler flips an unbiased coin. Every time a head appears, the pot is doubled and the gambler continues. When a tail appears, the game ends and the gambler collects the current value of the pot. The gambler is certain to win at least $1$ pound, the starting value of the pot, at the cost of $m$ pounds, the initial fee.

The game ends if the gambler's fortune falls below $m$ pounds. Let $p\_m(s)$ denote the probability that the gambler will never run out of money in this lottery given an initial fortune $s$ and the cost per game $m$.  
For example $p\_2(2) \\approx 0.2522$, $p\_2(5) \\approx 0.6873$ and $p\_6(10\\,000) \\approx 0.9952$ (note: $p\_m(s) = 0$ for $s \\lt m$).

Find $p\_{15}(10^9)$ and give your answer rounded to $7$ decimal places behind the decimal point in the form 0.abcdefg.
