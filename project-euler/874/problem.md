# Problem 874: Maximal Prime Score

Let $p(t)$ denote the $(t+1)$th prime number. So that $p(0) = 2$, $p(1) = 3$, etc.  
We define the prime score of a list of nonnegative integers $\[a\_1, \\dots, a\_n\]$ as the sum $\\sum\_{i = 1}^n p(a\_i)$.  
Let $M(k, n)$ be the maximal prime score among all lists $\[a\_1, \\dots, a\_n\]$ such that:

-   $0 \\leq a\_i < k$ for each $i$;
-   the sum $\\sum\_{i = 1}^n a\_i$ is a multiple of $k$.

For example, $M(2, 5) = 14$ as $\[0, 1, 1, 1, 1\]$ attains a maximal prime score of $14$.

Find $M(7000, p(7000))$.
