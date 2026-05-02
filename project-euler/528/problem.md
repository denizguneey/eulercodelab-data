# Problem 528: Constrained Sums

Let $S(n, k, b)$ represent the number of valid solutions to $x\_1 + x\_2 + \\cdots + x\_k \\le n$, where $0 \\le x\_m \\le b^m$ for all $1 \\le m \\le k$.

For example, $S(14,3,2) = 135$, $S(200,5,3) = 12949440$, and $S(1000,10,5) \\bmod 1\\,000\\,000\\,007 = 624839075$.

Find $(\\sum\_{10 \\le k \\le 15} S(10^k, k, k)) \\bmod 1\\,000\\,000\\,007$.
