# Problem 889: Rational Blancmange

Recall the blancmange function from [Problem 226](problem=226): $T(x) = \\sum\\limits\_{n = 0}^\\infty\\dfrac{s(2^nx)}{2^n}$, where $s(x)$ is the distance from $x$ to the nearest integer.

For positive integers $k, t, r$, we write $$F(k, t, r) = (2^{2k} - 1)T\\left(\\frac{(2^t + 1)^r}{2^k + 1}\\right).$$ It can be shown that $F(k, t, r)$ is always an integer.  
For example, $F(3, 1, 1) = 42$, $F(13, 3, 3) = 23093880$ and $F(103, 13, 6) \\equiv 878922518\\pmod {1\\,000\\,062\\,031}$.

Find $F(10^{18} + 31, 10^{14} + 31, 62)$. Give your answer modulo $1\\,000\\,062\\,031$.
