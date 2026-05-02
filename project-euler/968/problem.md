# Problem 968: 5D Summation

Define $$P(X\_{a,b},X\_{a,c},X\_{a,d},X\_{a,e},X\_{b,c},X\_{b,d},X\_{b,e},X\_{c,d},X\_{c,e},X\_{d,e})$$ as the sum of $2^a3^b5^c7^d11^e$ over all quintuples of non-negative integers $(a, b, c, d, e)$ such that the sum of each two of the five variables is restricted by a given value. In other words, $a+b \\le X\_{a,b}$, $a+d \\le X\_{a,d}$, $b+e \\le X\_{b,e}$ etc.

For example, $P(2,2,2,2,2,2,2,2,2,2)=7120$ and $P(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) \\equiv 799809376 \\pmod{10^9 + 7}$.

Define a sequence $A$ as follows:

-   $A\_0 = 1$, $A\_1 = 7$;
-   $A\_n =(7A\_{n−1}+A\_{n-2}^2) \\bmod(10^9+7)$ for $n \\ge 2$.

Also define $Q(n) = P(A\_{10n}, A\_{10n+1}, A\_{10n+2}, \\dots , A\_{10n+9})$.

Find $\\displaystyle\\sum\_{0 \\le n \\lt 100}Q(n)$. Give your answer modulo $10^9+7$.
