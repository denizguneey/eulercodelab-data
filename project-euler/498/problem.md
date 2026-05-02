# Problem 498: Remainder of Polynomial Division

For positive integers $n$ and $m$, we define two polynomials $F\_n(x) = x^n$ and $G\_m(x) = (x-1)^m$.  
We also define a polynomial $R\_{n,m}(x)$ as the remainder of the division of $F\_n(x)$ by $G\_m(x)$.  
For example, $R\_{6,3}(x) = 15x^2 - 24x + 10$.

Let $C(n, m, d)$ be the absolute value of the coefficient of the $d$-th degree term of $R\_{n,m}(x)$.  
We can verify that $C(6, 3, 1) = 24$ and $C(100, 10, 4) = 227197811615775$.

Find $C(10^{13}, 10^{12}, 10^4) \\bmod 999999937$.
