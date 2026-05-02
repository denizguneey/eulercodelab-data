# Problem 851: SOP and POS

Let $n$ be a positive integer and let $E\_n$ be the set of $n$-tuples of strictly positive integers.

For $u = (u\_1, \\cdots, u\_n)$ and $v = (v\_1, \\cdots, v\_n)$ two elements of $E\_n$, we define:

-   the Sum Of Products of $u$ and $v$, denoted by $\\langle u, v\\rangle$, as the sum $\\displaystyle\\sum\_{i = 1}^n u\_i v\_i$;
-   the Product Of Sums of $u$ and $v$, denoted by $u \\star v$, as the product $\\displaystyle\\prod\_{i = 1}^n (u\_i + v\_i)$.

Let $R\_n(M)$ be the sum of $u \\star v$ over all ordered pairs $(u, v)$ in $E\_n$ such that $\\langle u, v\\rangle = M$.  
For example: $R\_1(10) = 36$, $R\_2(100) = 1873044$, $R\_2(100!) \\equiv 446575636 \\bmod 10^9 + 7$.

Find $R\_6(10000!)$. Give your answer modulo $10^9+7$.
