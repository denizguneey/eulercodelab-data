# Problem 684: Inverse Digit Sum

Define $s(n)$ to be the smallest number that has a digit sum of $n$. For example $s(10) = 19$.  
Let $\\displaystyle S(k) = \\sum\_{n=1}^k s(n)$. You are given $S(20) = 1074$.

Further let $f\_i$ be the Fibonacci sequence defined by $f\_0=0, f\_1=1$ and $f\_i=f\_{i-2}+f\_{i-1}$ for all $i \\ge 2$.

Find $\\displaystyle \\sum\_{i=2}^{90} S(f\_i)$. Give your answer modulo $1\\,000\\,000\\,007$.
