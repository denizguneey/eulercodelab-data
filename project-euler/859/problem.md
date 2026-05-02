# Problem 859: Cookie Game

Odd and Even are playing a game with $N$ cookies.

The game begins with the $N$ cookies divided into one or more piles, not necessarily of the same size. They then make moves in turn, starting with Odd.  
Odd's turn: Odd may choose any pile with an **odd** number of cookies, eat one and divide the remaining (if any) into two equal piles.  
Even's turn: Even may choose any pile with an **even** number of cookies, eat two of them and divide the remaining (if any) into two equal piles.  
The player that does not have a valid move loses the game.

Let $C(N)$ be the number of ways that $N$ cookies can be divided so that Even has a winning strategy.  
For example, $C(5) = 2$ because there are two winning configurations for Even: a single pile containing all five cookies; three piles containing one, two and two cookies.  
You are also given $C(16) = 64$.

Find $C(300)$.
