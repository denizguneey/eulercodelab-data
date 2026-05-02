# Problem 715: Sextuplet Norms

Let $f(n)$ be the number of $6$-tuples $(x\_1,x\_2,x\_3,x\_4,x\_5,x\_6)$ such that:

-   All $x\_i$ are integers with $0 \\leq x\_i < n$
-   $\\gcd(x\_1^2+x\_2^2+x\_3^2+x\_4^2+x\_5^2+x\_6^2,\\ n^2)=1$

Let $\\displaystyle G(n)=\\displaystyle\\sum\_{k=1}^n \\frac{f(k)}{k^2\\varphi(k)}$  
where $\\varphi(n)$ is Euler's totient function.

For example, $G(10)=3053$ and $G(10^5) \\equiv 157612967 \\pmod{1\\,000\\,000\\,007}$.

Find $G(10^{12})\\bmod 1\\,000\\,000\\,007$.
