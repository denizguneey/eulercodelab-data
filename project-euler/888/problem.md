# Problem 888: 1249 Nim

Two players play a game with a number of piles of stones, alternating turns. Each turn a player can choose to remove 1, 2, 4, or 9 stones from a single pile; or alternatively they can choose to split a pile containing two or more stones into two non-empty piles. The winner is the player who removes the last stone.

A collection of piles is called a losing position if the player to move cannot force a win with optimal play. Define $S(N, m)$ to be the number of distinct losing positions arising from $m$ piles of stones where each pile contains from $1$ to $N$ stones. Two positions are considered equivalent if they consist of the same pile sizes. That is, the order of the piles does not matter.

You are given $S(12,4)=204$ and $S(124,9)=2259208528408$.

Find $S(12491249,1249)$. Give your answer modulo $912491249$.
