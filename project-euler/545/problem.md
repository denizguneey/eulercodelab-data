# Problem 545: Faulhaber's Formulas

The sum of the $k$<sup>th</sup> powers of the first $n$ positive integers can be expressed as a polynomial of degree $k+1$ with rational coefficients, the **Faulhaber's Formulas**:  
$1^k + 2^k + ... + n^k = \\sum\_{i=1}^n i^k = \\sum\_{i=1}^{k+1} a\_{i} n^i = a\_{1} n + a\_{2} n^2 + ... + a\_{k} n^k + a\_{k+1} n^{k + 1}$,  
where $a\_i$'s are rational coefficients that can be written as reduced fractions $p\_i/q\_i$ (if $a\_i = 0$, we shall consider $q\_i = 1$).

For example, $1^4 + 2^4 + ... + n^4 = -\\frac 1 {30} n + \\frac 1 3 n^3 + \\frac 1 2 n^4 + \\frac 1 5 n^5.$

Define $D(k)$ as the value of $q\_1$ for the sum of $k$<sup>th</sup> powers (i.e. the denominator of the reduced fraction $a\_1$).  
Define $F(m)$ as the $m$<sup>th</sup> value of $k \\ge 1$ for which $D(k) = 20010$.  
You are given $D(4) = 30$ (since $a\_1 = -1/30$), $D(308) = 20010$, $F(1) = 308$, $F(10) = 96404$.

Find $F(10^5)$.
