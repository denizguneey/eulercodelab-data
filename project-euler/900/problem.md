# Problem 900: DistribuNim II

Two players play a game with at least two piles of stones. The players alternately take stones from one or more piles, subject to:

1.  the total number of stones taken is equal to the size of the smallest pile before the move;
2.  the move cannot take all the stones from a pile.

The player that is unable to move loses.

For example, if the piles are of sizes 2, 2 and 4 then there are four possible moves. $$ (2,2,4)\\xrightarrow{(1,1,0)}(1,1,4)\\quad (2,2,4)\\xrightarrow{(1,0,1)}(1,2,3)\\quad (2,2,4)\\xrightarrow{(0,1,1)}(2,1,3)\\quad (2,2,4)\\xrightarrow{(0,0,2)}(2,2,2)$$

Let $t(n)$ be the smallest nonnegative integer $k$ such that the position with $n$ piles of $n$ stones and a single pile of $n+k$ stones is losing for the first player assuming optimal play. For example, $t(1) = t(2) = 0$ and $t(3) = 2$.

Define $\\displaystyle S(N) = \\sum\_{n=1}^{2^N} t(n)$. You are given $S(10) = 361522$.

Find $S(10^4)$. Give your answer modulo $900497239$.
