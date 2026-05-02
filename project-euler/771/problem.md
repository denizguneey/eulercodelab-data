# Problem 771: Pseudo Geometric Sequences

We define a pseudo-geometric sequence to be a finite sequence $a\_0, a\_1, \\dotsc, a\_n$ of positive integers, satisfying the following conditions:

-   $n \\geq 4$, i.e. the sequence has at least $5$ terms.
-   $0 \\lt a\_0 \\lt a\_1 \\lt \\cdots \\lt a\_n$, i.e. the sequence is strictly increasing.
-   $| a\_i^2 - a\_{i - 1}a\_{i + 1} | \\le 2$ for $1 \\le i \\le n-1$.

Let $G(N)$ be the number of different pseudo-geometric sequences whose terms do not exceed $N$.  
For example, $G(6) = 4$, as the following $4$ sequences give a complete list:

$1, 2, 3, 4, 5 \\qquad 1, 2, 3, 4, 6 \\qquad 2, 3, 4, 5, 6 \\qquad 1, 2, 3, 4, 5, 6$

Also, $G(10) = 26$, $G(100) = 4710$ and $G(1000) = 496805$.

Find $G(10^{18})$. Give your answer modulo $1\\,000\\,000\\,007$.
