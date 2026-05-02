# Problem 899: DistribuNim I

Two players play a game with two piles of stones. The players alternately take stones from one or both piles, subject to:

1.  the total number of stones taken is equal to the size of the smallest pile before the move;
2.  the move cannot take all the stones from a pile.

The player that is unable to move loses.

For example, if the piles are of sizes 3 and 5 then there are three possible moves. $$(3,5) \\xrightarrow{(2,1)} (1,4)\\qquad\\qquad (3,5) \\xrightarrow{(1,2)} (2,3)\\qquad\\qquad (3,5) \\xrightarrow{(0,3)} (3,2)$$

Let $L(n)$ be the number of ordered pairs $(a,b)$ with $1 \\leq a,b \\leq n$ such that the initial game position with piles of sizes $a$ and $b$ is losing for the first player assuming optimal play.

You are given $L(7) = 21$ and $L(7^2) = 221$.

Find $L(7^{17})$.
