# Problem 593: Fleeting Medians

We define two sequences $S = \\{S(1), S(2), ..., S(n)\\}$ and $S\_2 = \\{S\_2(1), S\_2(2), ..., S\_2(n)\\}$:

$S(k) = (p\_k)^k \\bmod 10007$ where $p\_k$ is the $k$th prime number.

$S\_2(k) = S(k) + S(\\lfloor\\frac{k}{10000}\\rfloor + 1)$ where $\\lfloor \\cdot \\rfloor$ denotes the floor function.

Then let $M(i, j)$ be the median of elements $S\_2(i)$ through $S\_2(j)$, inclusive. For example, $M(1, 10) = 2021.5$ and $M(10^2, 10^3) = 4715.0$.

Let $F(n, k) = \\sum\_{i=1}^{n-k+1} M(i, i + k - 1)$. For example, $F(100, 10) = 463628.5$ and $F(10^5, 10^4) = 675348207.5$.

Find $F(10^7, 10^5)$. If the sum is not an integer, use $.5$ to denote a half. Otherwise, use $.0$ instead.
