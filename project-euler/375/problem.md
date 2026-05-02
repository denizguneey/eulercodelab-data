# Problem 375: Minimum of Subsequences

Let $S\_n$ be an integer sequence produced with the following pseudo-random number generator:

$$\\begin{align} S\_0 & = 290797 \\\\ S\_{n+1} & = S\_n^2 \\bmod 50515093 \\end{align}$$

Let $A(i, j)$ be the minimum of the numbers $S\_i, S\_{i+1}, \\dots, S\_j$ for $i\\le j$.  
Let $M(N) = \\sum A(i, j)$ for $1 \\le i \\le j \\le N$.  
We can verify that $M(10) = 432256955$ and $M(10\\,000) = 3264567774119$.

Find $M(2\\,000\\,000\\,000)$.
