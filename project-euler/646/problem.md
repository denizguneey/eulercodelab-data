# Problem 646: Bounded Divisors

Let $n$ be a natural number and $p\_1^{\\alpha\_1}\\cdot p\_2^{\\alpha\_2}\\cdots p\_k^{\\alpha\_k}$ its prime factorisation.  
Define the **Liouville function** $\\lambda(n)$ as $\\lambda(n) = (-1)^{\\sum\\limits\_{i=1}^{k}\\alpha\_i}$.  
(i.e. $-1$ if the sum of the exponents $\\alpha\_i$ is odd and $1$ if the sum of the exponents is even. )  
Let $S(n,L,H)$ be the sum $\\lambda(d) \\cdot d$ over all divisors $d$ of $n$ for which $L \\leq d \\leq H$.

You are given:

-   $S(10! , 100, 1000) = 1457$
-   $S(15!, 10^3, 10^5) = -107974$
-   $S(30!,10^8, 10^{12}) = 9766732243224$.

Find $S(70!,10^{20}, 10^{60})$ and give your answer modulo $1\\,000\\,000\\,007$.
