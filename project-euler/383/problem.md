# Problem 383: Divisibility Comparison Between Factorials

Let $f\_5(n)$ be the largest integer $x$ for which $5^x$ divides $n$.  
For example, $f\_5(625000) = 7$.

Let $T\_5(n)$ be the number of integers $i$ which satisfy $f\_5((2 \\cdot i - 1)!) \\lt 2 \\cdot f\_5(i!)$ and $1 \\le i \\le n$.  
It can be verified that $T\_5(10^3) = 68$ and $T\_5(10^9) = 2408210$.

Find $T\_5(10^{18})$.
