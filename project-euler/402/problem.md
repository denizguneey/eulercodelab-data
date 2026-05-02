# Problem 402: Integer-valued Polynomials

It can be shown that the polynomial $n^4 + 4n^3 + 2n^2 + 5n$ is a multiple of $6$ for every integer $n$. It can also be shown that $6$ is the largest integer satisfying this property.

Define $M(a, b, c)$ as the maximum $m$ such that $n^4 + an^3 + bn^2 + cn$ is a multiple of $m$ for all integers $n$. For example, $M(4, 2, 5) = 6$.

Also, define $S(N)$ as the sum of $M(a, b, c)$ for all $0 \\lt a, b, c \\leq N$.

We can verify that $S(10) = 1972$ and $S(10000) = 2024258331114$.

Let $F\_k$ be the Fibonacci sequence:  
$F\_0 = 0$, $F\_1 = 1$ and  
$F\_k = F\_{k-1} + F\_{k-2}$ for $k \\geq 2$.

Find the last $9$ digits of $\\sum S(F\_k)$ for $2 \\leq k \\leq 1234567890123$.
