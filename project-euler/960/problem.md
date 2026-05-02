# Problem 960: Stone Game Solitaire

There are $n$ distinct piles of stones, each of size $n-1$. Starting with an initial score of $0$, the following procedure is repeated:

1.  Choose any two piles and remove exactly $n$ stones in total from the two piles.
2.  If the number of stones removed from the two piles were $a$ and $b$, add $\\min(a,b)$ to the score.

If all piles are eventually emptied, the current score is confirmed as final. However, if one gets "stuck" and cannot empty all piles, the current score is discarded, resulting in a final score of $0$.

Three example sequences of turns are illustrated below for $n=4$, with each tuple representing pile sizes as one proceeds, and with additions to the score indicated above the arrows. $$ \\begin{align} &(3,3,3,3)\\xrightarrow{+1}(0,3,2,3)\\xrightarrow{+1}(0,3,1,0)\\xrightarrow{+1}(0,0,0,0)&:\\quad\\text{final score }=3\\\\ &(3,3,3,3)\\xrightarrow{+1}(3,0,3,2)\\xrightarrow{+2}(1,0,3,0)\\xrightarrow{+1}(0,0,0,0)&:\\quad\\text{final score }=4\\\\ &(3,3,3,3)\\xrightarrow{+2}(1,3,1,3)\\xrightarrow{+1}(1,2,1,0)\\rightarrow\\text{stuck!}&:\\quad\\text{final score }=0 \\end{align} $$

Define $F(n)$ to be the sum of the final scores achieved for every sequence of turns which successfully empty all piles.

You are given $F(3)=12$, $F(4)=360$, and $F(8)=16785941760$.

Find $F(100)$. Give your answer modulo $10^9+7$.
