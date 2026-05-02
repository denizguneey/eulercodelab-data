# Problem 863: Different Dice

Using only a six-sided fair dice and a five-sided fair dice, we would like to emulate an $n$-sided fair dice.

For example, one way to emulate a 28-sided dice is to follow this procedure:

1.  Roll both dice, obtaining integers $1\\le p\\le 6$ and $1\\le q\\le 5$.
2.  Combine them using $r = 5(p-1) + q$ to obtain an integer $1\\le r\\le 30$.
3.  If $r\\le 28$, return the value $r$ and stop.
4.  Otherwise ($r$ being 29 or 30), roll both dice again, obtaining integers $1\\le s\\le 6$ and $1\\le t\\le 5$.
5.  Compute $u = 30(r-29) + 5(s-1) + t$ to obtain an integer $1\\le u\\le 60$.
6.  If $u>4$, return the value $((u-5)\\bmod 28) + 1$ and stop.
7.  Otherwise (with $1\\le u\\le 4$), roll the six-sided dice twice, obtaining integers $1\\le v\\le 6$ and $1\\le w\\le 6$.
8.  Compute $x = 36(u-1) + 6(v-1) + w$ to obtain an integer $1\\le x\\le 144$.
9.  If $x>4$, return the value $((x-5)\\bmod 28) + 1$ and stop.
10.  Otherwise (with $1\\le x\\le 4$), assign $u:=x$ and go back to step 7.

The expected number of dice rolls in following this procedure is 2.142476 (rounded to 6 decimal places). Note that rolling both dice at the same time is still counted as two dice rolls.

There exist other more complex procedures for emulating a 28-sided dice that entail a smaller average number of dice rolls. However, the above procedure has the attractive property that the sequence of dice rolled is predetermined: regardless of the outcome, it follows (D5,D6,D5,D6,D6,D6,D6,...), truncated wherever the process stops. In fact, amongst procedures for $n=28$ with this restriction, this one is optimal in the sense of minimising the expected number of rolls needed.

Different values of $n$ will in general use different predetermined sequences. For example, for $n=8$, the sequence (D5,D5,D5,...) gives an optimal procedure, taking 2.083333... dice rolls on average.

Define $R(n)$ to be the expected number of dice rolls for an optimal procedure for emulating an $n$-sided dice using only a five-sided and a six-sided dice, considering only those procedures where the sequence of dice rolled is predetermined. So, $R(8) \\approx 2.083333$ and $R(28) \\approx 2.142476$.

Let $S(n) = \\displaystyle\\sum\_{k=2}^n R(k)$. You are given that $S(30) \\approx 56.054622$.

Find $S(1000)$. Give your answer rounded to 6 decimal places.
