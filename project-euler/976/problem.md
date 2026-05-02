# Problem 976: XO Game

Two players X and O play a game with $k$ strips of squares of lengths $n\_1,\\dots,n\_k$, originally all blank.

Starting with X, they make moves in turn. At X's turn, X draws an "X" symbol; at O's turn, O draws an "O" symbol.  
The symbol must be drawn in one blank square with either red or blue pen, subject to the following restrictions:

1.  two symbols in adjacent squares on one strip must be different symbols **and** must have different colour;
2.  if there is at least one blank strip, then one must draw on a blank strip.

Whoever does not have a valid move loses the game.

Let $P(K, N)$ be the number of tuples $(n\_1,\\dots,n\_k)$ such that $1 \\leq k \\leq K$, $1\\leq n\_1\\leq\\cdots\\leq n\_k\\leq N$ and that X has a winning strategy to the corresponding game.  
For example, $P(2, 4)=7$ and $P(5, 10) = 901$.

Find $P(10^7, 10^7)\\bmod 1234567891$.
