# Problem 537: Counting Tuples

Let $\\pi(x)$ be the prime counting function, i.e. the number of prime numbers less than or equal to $x$.  
For example,$\\pi(1)=0$, $\\pi(2)=1$, $\\pi(100)=25$.

Let $T(n, k)$ be the number of $k$-tuples $(x\_1, \\dots, x\_k)$ which satisfy:  
1\. every $x\_i$ is a positive integer;  
2\. $\\displaystyle \\sum\_{i=1}^k \\pi(x\_i)=n$

For example $T(3,3)=19$.  
The $19$ tuples are $(1,1,5)$, $(1,5,1)$, $(5,1,1)$, $(1,1,6)$, $(1,6,1)$, $(6,1,1)$, $(1,2,3)$, $(1,3,2)$, $(2,1,3)$, $(2,3,1)$, $(3,1,2)$, $(3,2,1)$, $(1,2,4)$, $(1,4,2)$, $(2,1,4)$, $(2,4,1)$, $(4,1,2)$, $(4,2,1)$, $(2,2,2)$.

You are given $T(10, 10) = 869\\,985$ and $T(10^3,10^3) \\equiv 578\\,270\\,566 \\pmod{1\\,004\\,535\\,809}$.

Find $T(20\\,000, 20\\,000) \\pmod{1\\,004\\,535\\,809}$.
