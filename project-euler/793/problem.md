# Problem 793: Median of Products

Let $S\_i$ be an integer sequence produced with the following pseudo-random number generator:

-   $S\_0 = 290797$
-   $S\_{i+1} = S\_i ^2 \\bmod 50515093$

Let $M(n)$ be the median of the pairwise products $ S\_i S\_j $ for $0 \\le i \\lt j \\lt n$.

You are given $M(3) = 3878983057768$ and $M(103) = 492700616748525$.

Find $M(1\\,000\\,003)$.
