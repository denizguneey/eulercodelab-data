# Problem 639: Summing a Multiplicative Function

A **multiplicative function** $f(x)$ is a function over positive integers satisfying $f(1)=1$ and $f(a b)=f(a) f(b)$ for any two coprime positive integers $a$ and $b$.

For integer $k$ let $f\_k(n)$ be a multiplicative function additionally satisfying $f\_k(p^e)=p^k$ for any prime $p$ and any integer $e>0$.  
For example, $f\_1(2)=2$, $f\_1(4)=2$, $f\_1(18)=6$ and $f\_2(18)=36$.

Let $\\displaystyle S\_k(n)=\\sum\_{i=1}^{n} f\_k(i)$. For example, $S\_1(10)=41$, $S\_1(100)=3512$, $S\_2(100)=208090$, $S\_1(10000)=35252550$ and $\\displaystyle \\sum\_{k=1}^{3} S\_k(10^{8}) \\equiv 338787512 \\pmod{ 1\\,000\\,000\\,007}$.

Find $\\displaystyle \\sum\_{k=1}^{50} S\_k(10^{12}) \\bmod 1\\,000\\,000\\,007$.
