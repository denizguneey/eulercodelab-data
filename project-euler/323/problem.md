# Problem 323: Bitwise-OR Operations on Random Integers

Let $y\_0, y\_1, y\_2, \\dots$ be a sequence of random unsigned $32$-bit integers  
(i.e. $0 \\le y\_i \\lt 2^{32}$, every value equally likely).

For the sequence $x\_i$ the following recursion is given:  

-   $x\_0 = 0$ and
-   $x\_i = x\_{i - 1} \\boldsymbol \\mid y\_{i - 1}$, for $i \\gt 0$. ($\\boldsymbol \\mid$ is the bitwise-OR operator).

It can be seen that eventually there will be an index $N$ such that $x\_i = 2^{32} - 1$ (a bit-pattern of all ones) for all $i \\ge N$.

Find the expected value of $N$.  
Give your answer rounded to $10$ digits after the decimal point.
