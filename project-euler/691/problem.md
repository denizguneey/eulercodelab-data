# Problem 691: Long Substring with Many Repetitions

Given a character string $s$, we define $L(k,s)$ to be the length of the longest substring of $s$ which appears at least $k$ times in $s$, or $0$ if such a substring does not exist. For example, $L(3,\\text{“bbabcabcabcacba”})=4$ because of the three occurrences of the substring $\\text{“abca”}$, and $L(2,\\text{“bbabcabcabcacba”})=7$ because of the repeated substring $\\text{“abcabca”}$. Note that the occurrences can overlap.

Let $a\_n$, $b\_n$ and $c\_n$ be the $0/1$ sequences defined by:

-   $a\_0 = 0$
-   $a\_{2n} = a\_{n}$
-   $a\_{2n+1} = 1-a\_{n}$
-   $b\_n = \\lfloor\\frac{n+1}{\\varphi}\\rfloor - \\lfloor\\frac{n}{\\varphi}\\rfloor$ (where $\\varphi$ is the golden ratio)
-   $c\_n = a\_n + b\_n - 2a\_nb\_n$

and $S\_n$ the character string $c\_0\\ldots c\_{n-1}$. You are given that $L(2,S\_{10})=5$, $L(3,S\_{10})=2$, $L(2,S\_{100})=14$, $L(4,S\_{100})=6$, $L(2,S\_{1000})=86$, $L(3,S\_{1000}) = 45$, $L(5,S\_{1000}) = 31$, and that the sum of non-zero $L(k,S\_{1000})$ for $k\\ge 1$ is $2460$.

Find the sum of non-zero $L(k,S\_{5000000})$ for $k\\ge 1$.
