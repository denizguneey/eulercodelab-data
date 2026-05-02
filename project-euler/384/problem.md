# Problem 384: Rudin-Shapiro Sequence

Define the sequence $a(n)$ as the number of adjacent pairs of ones in the binary expansion of $n$ (possibly overlapping).  
E.g.: $a(5) = a(101\_2) = 0$, $a(6) = a(110\_2) = 1$, $a(7) = a(111\_2) = 2$.

Define the sequence $b(n) = (-1)^{a(n)}$.  
This sequence is called the **Rudin-Shapiro** sequence.

Also consider the summatory sequence of $b(n)$: $s(n) = \\sum \\limits\_{i = 0}^n b(i)$.

The first couple of values of these sequences are:

<table align="center"><tbody><tr><td align="center" width="30">$n$</td><td align="right" width="30">$0$</td><td align="right" width="30">$1$</td><td align="right" width="30">$2$</td><td align="right" width="30">$3$</td><td align="right" width="30">$4$</td><td align="right" width="30">$5$</td><td align="right" width="30">$6$</td><td align="right" width="30">$7$</td></tr><tr><td align="center" width="30">$a(n)$</td><td align="right" width="30">$0$</td><td align="right" width="30">$0$</td><td align="right" width="30">$0$</td><td align="right" width="30">$1$</td><td align="right" width="30">$0$</td><td align="right" width="30">$0$</td><td align="right" width="30">$1$</td><td align="right" width="30">$2$</td></tr><tr><td align="center" width="30">$b(n)$</td><td align="right" width="30">$1$</td><td align="right" width="30">$1$</td><td align="right" width="30">$1$</td><td align="right" width="30">$-1$</td><td align="right" width="30">$1$</td><td align="right" width="30">$1$</td><td align="right" width="30">$-1$</td><td align="right" width="30">$1$</td></tr><tr><td align="center" width="30">$s(n)$</td><td align="right" width="30">$1$</td><td align="right" width="30">$2$</td><td align="right" width="30">$3$</td><td align="right" width="30">$2$</td><td align="right" width="30">$3$</td><td align="right" width="30">$4$</td><td align="right" width="30">$3$</td><td align="right" width="30">$4$</td></tr></tbody></table>

The sequence $s(n)$ has the remarkable property that all elements are positive and every positive integer $k$ occurs exactly $k$ times.

Define $g(t,c)$, with $1 \\le c \\le t$, as the index in $s(n)$ for which $t$ occurs for the $c$'th time in $s(n)$.  
E.g.: $g(3,3) = 6$, $g(4,2) = 7$ and $g(54321,12345) = 1220847710$.

Let $F(n)$ be the Fibonacci sequence defined by:  
$F(0)=F(1)=1$ and  
$F(n)=F(n-1)+F(n-2)$ for $n \\gt 1$.

Define $GF(t)=g(F(t),F(t-1))$.

Find $\\sum GF(t)$ for $2 \\le t \\le 45$.
