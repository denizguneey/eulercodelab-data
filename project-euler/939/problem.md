# Problem 939: Partisan Nim

Two players A and B are playing a variant of Nim.  
At the beginning, there are several piles of stones. Each pile is either at the side of A or at the side of B. The piles are unordered.

They make moves in turn. At a player's turn, the player can

-   either choose a pile on the opponent's side and remove one stone from that pile;
-   or choose a pile on their own side and remove the whole pile.

The winner is the player who removes the last stone.

Let $E(N)$ be the number of initial settings with at most $N$ stones such that, whoever plays first, A always has a winning strategy.

For example $E(4) = 9$; the settings are:

<table class="grid center"><tbody><tr><th>Nr.</th><th>Piles at the side of A</th><th>Piles at the side of B</th></tr><tr><td>1</td><td>$4$</td><td>none</td></tr><tr><td>2</td><td>$1, 3$</td><td>none</td></tr><tr><td>3</td><td>$2, 2$</td><td>none</td></tr><tr><td>4</td><td>$1, 1, 2$</td><td>none</td></tr><tr><td>5</td><td>$3$</td><td>$1$</td></tr><tr><td>6</td><td>$1, 2$</td><td>$1$</td></tr><tr><td>7</td><td>$2$</td><td>$1, 1$</td></tr><tr><td>8</td><td>$3$</td><td>none</td></tr><tr><td>9</td><td>$2$</td><td>none</td></tr></tbody></table>

Find $E(5000) \\bmod 1234567891$.
