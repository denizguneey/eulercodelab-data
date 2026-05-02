# Problem 722: Slowly Converging Series

For a non-negative integer $k$, define $$ E\_k(q) = \\sum\\limits\_{n = 1}^\\infty \\sigma\_k(n)q^n $$ where $\\sigma\_k(n) = \\sum\_{d \\mid n} d^k$ is the sum of the $k$-th powers of the positive divisors of $n$.

It can be shown that, for every $k$, the series $E\_k(q)$ converges for any $0 < q < 1$.

For example,  
$E\_1(1 - \\frac{1}{2^4}) = 3.872155809243\\mathrm e2$  
$E\_3(1 - \\frac{1}{2^8}) = 2.767385314772\\mathrm e10$  
$E\_7(1 - \\frac{1}{2^{15}}) = 6.725803486744\\mathrm e39$  
All the above values are given in scientific notation rounded to twelve digits after the decimal point.

Find the value of $E\_{15}(1 - \\frac{1}{2^{25}})$.  
Give the answer in scientific notation rounded to twelve digits after the decimal point.
