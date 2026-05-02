# Problem 438: Integer Part of Polynomial Equation's Solutions

For an $n$-tuple of integers $t = (a\_1, \\dots, a\_n)$, let $(x\_1, \\dots, x\_n)$ be the solutions of the polynomial equation $x^n + a\_1 x^{n-1} + a\_2 x^{n-2} + \\cdots + a\_{n-1}x + a\_n = 0$.

Consider the following two conditions:

-   $x\_1, \\dots, x\_n$ are all real.
-   If $x\_1, \\dots, x\_n$ are sorted, $\\lfloor x\_i\\rfloor = i$ for $1 \\leq i \\leq n$. ($\\lfloor \\cdot \\rfloor$: floor function.)

In the case of $n = 4$, there are $12$ $n$-tuples of integers which satisfy both conditions.  
We define $S(t)$ as the sum of the absolute values of the integers in $t$.  
For $n = 4$ we can verify that $\\sum S(t) = 2087$ for all $n$-tuples $t$ which satisfy both conditions.

Find $\\sum S(t)$ for $n = 7$.
