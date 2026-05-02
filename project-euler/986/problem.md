# Problem 986: Another Infinite Game

Peter is playing another game on an infinite row of squares, each square of which can hold an unlimited number of tokens.

Initially, every square contains a token.  
Given positive integers $c$ and $d$, each move of the game consists of the following steps:

1.  Choose two tokens $X$ and $Y$ such that $Y$ is $c$ squares to the right of $X$.
2.  Move both $X$ and $Y$ to the square that is $d$ squares to the right of $Y$.

Peter's goal is to move as many tokens as possible into one square. For example, with $c = 2$ and $d = 1$, it is possible to move $7$ tokens into one square, following these steps (where red color marks the chosen tokens):

... 1 1 1 1 1 1 1 1 ...  
... 1 1 1 1 0 1 0 3 ...  
... 1 1 1 0 0 0 2 3 ...  
... 0 1 0 2 0 0 2 3 ...  
... 0 0 0 1 2 0 2 3 ...  
... 0 0 0 1 1 0 1 5 ...  
... 0 0 0 1 0 0 0 7 ...

However, it is not possible to move $8$ tokens into one square.

Let $G(c, d)$ be the maximum number of tokens Peter can move into one square. For example, $G(2, 1) = 7$. You are also given that $G(1, 2) = 7$, $G(3, 1) = 11$, $G(2, 2) = 3$ and $G(1, 3) = 15$.

Find the sum of $G(c, d)$ for all pairs of $c, d$ with $1 \\leq c, d \\leq 160$.
