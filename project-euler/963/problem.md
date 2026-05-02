# Problem 963: Removing Trits

**NOTE**: This problem is related to [Problem 882](problem=882). It is recommended to solve that problem before doing this one.

Two players are playing a game. When the game starts, each player holds a paper with two positive integers written on it.  
They make moves in turn. At a player's turn, the player can do one of the following:

-   pick a number on the player's own paper and change it by removing a $0$ from its **ternary expansionbase-$3$ expansion**;
-   pick a number on the opponent's paper and change it by removing a $1$ from its ternary expansion;
-   pick a number on either paper and change it by removing a $2$ from its ternary expansion.

The player that is unable to make a move loses.  
Leading zeros are not allowed in any ternary expansion; in particular nobody can make a move on the number $0$.

An initial setting is called fair if whichever player moves first will lose the game if both play optimally.

For example, if initially the integers on the paper of the first player are $1, 5$ and those on the paper of the second player are $2, 4$, then this is a fair initial setting, which we can denote as $(1, 5 \\mid 2, 4)$.  
Note that the order of the two integers on a paper does not matter, but the order of the two papers matter.  
Thus $(5, 1 \\mid 4, 2)$ is considered the same as $(1, 5 \\mid 2, 4)$, while $(2, 4 \\mid 1, 5)$ is a different initial setting.

Let $F(N)$ be the number of fair initial settings where each initial number does not exceed $N$.  
For example, $F(5) = 21$.

Find $F(10^5)$.
