# Problem 337: Totient Stairstep Sequences

Let $\\{a\_1, a\_2, \\dots, a\_n\\}$ be an integer sequence of length $n$ such that:

-   $a\_1 = 6$
-   for all $1 \\le i \\lt n$: $\\phi(a\_i) \\lt \\phi(a\_{i + 1}) \\lt a\_i \\lt a\_{i + 1}$.<sup>1</sup>

Let $S(N)$ be the number of such sequences with $a\_n \\le N$.  
For example, $S(10) = 4$: $\\{6\\}$, $\\{6, 8\\}$, $\\{6, 8, 9\\}$ and $\\{6, 10\\}$.  
We can verify that $S(100) = 482073668$ and $S(10\\,000) \\bmod 10^8 = 73808307$.

Find $S(20\\,000\\,000) \\bmod 10^8$.

<sup>1</sup> $\\phi$ denotes **Euler's totient function**.
