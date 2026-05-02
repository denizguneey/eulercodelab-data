# Problem 605: Pairwise Coin-Tossing Game

Consider an $n$-player game played in consecutive pairs: Round $1$ takes place between players $1$ and $2$, round $2$ takes place between players $2$ and $3$, and so on and so forth, all the way up to round $n$, which takes place between players $n$ and $1$. Then round $n+1$ takes place between players $1$ and $2$ as the entire cycle starts again.

In other words, during round $r$, player $((r-1) \\bmod n) + 1$ faces off against player $(r \\bmod n) + 1$.

During each round, a fair coin is tossed to decide which of the two players wins that round. If any given player wins both rounds $r$ and $r+1$, then that player wins the entire game.

Let $P\_n(k)$ be the probability that player $k$ wins in an $n$-player game, in the form of a reduced fraction. For example, $P\_3(1) = 12/49$ and $P\_6(2) = 368/1323$.

Let $M\_n(k)$ be the product of the reduced numerator and denominator of $P\_n(k)$. For example, $M\_3(1) = 588$ and $M\_6(2) = 486864$.

Find the last $8$ digits of $M\_{10^8+7}(10^4+7)$.
