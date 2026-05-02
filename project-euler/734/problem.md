# Problem 734: A Bit of Prime

The **logical-OR** of two bits is $0$ if both bits are $0$, otherwise it is $1$.  
The **bitwise-OR** of two positive integers performs a logical-OR operation on each pair of corresponding bits in the binary expansion of its inputs.

For example, the bitwise-OR of $10$ and $6$ is $14$ because $10 = 1010\_2$, $6 = 0110\_2$ and $14 = 1110\_2$.

Let $T(n, k)$ be the number of $k$-tuples $(x\_1, x\_2,\\cdots,x\_k)$ such that

-   every $x\_i$ is a prime $\\leq n$
-   the bitwise-OR of the tuple is a prime $\\leq n$

For example, $T(5, 2)=5$. The five $2$-tuples are $(2, 2)$, $(2, 3)$, $(3, 2)$, $(3, 3)$ and $(5, 5)$.

You are given $T(100, 3) = 3355$ and $T(1000, 10) \\equiv 2071632 \\pmod{1\\,000\\,000\\,007}$.

Find $T(10^6,999983)$. Give your answer modulo $1\\,000\\,000\\,007$.
