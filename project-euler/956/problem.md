# Problem 956: Super Duper Sum

The total number of prime factors of $n$, counted with multiplicity, is denoted $\\Omega(n)$.  
For example, $\\Omega(12)=3$, counting the factor $2$ twice, and the factor $3$ once.

Define $D(n, m)$ to be the sum of all divisors $d$ of $n$ where $\\Omega(d)$ is divisible by $m$.  
For example, $D(24, 3)=1+8+12=21$.

The **superfactorial** of $n$, often written as $n\\$$, is defined as the product of the first $n$ factorials: $$n\\$=1!\\times 2! \\times\\cdots\\times n!$$ The **superduperfactorial** of $n$, we write as $n\\bigstar$, is defined as the product of the first $n$ superfactorials: $$n\\bigstar=1\\$ \\times 2\\$ \\times\\cdots\\times n\\$ $$

You are given $D(6\\bigstar, 6)=6368195719791280$.

Find $D(1\\,000\\bigstar, 1\\,000)$. Give your answer modulo $999\\,999\\,001$.
