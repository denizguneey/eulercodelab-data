# Problem 973: Random Dealings

A game is played with $n$ cards. At the start the cards are dealt out onto a table to get $n$ piles of size one.

Each round proceeds as follows:

1.  Select a pile at random and pick it up.
2.  Randomly choose a pile from the table and add the top card of the picked-up pile to it.
3.  Redistribute any remaining cards from the picked-up pile by dealing them into new single-card piles.

The game ends when all cards are in a single pile.

At the end of each round a score is obtained by bitwise-XORing the size of each pile. The score is summed across the rounds. Let $X(n)$ be the expected total score at the end of the game.

You are given $X(2) = 2$, $X(4) = 14$ and $X(10) = 1418$.

Find $X(10^4)$. Give your answer modulo $10^9+7$.
