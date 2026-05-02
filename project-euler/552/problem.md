# Problem 552: Chinese Leftovers II

Let $A\_n$ be the smallest positive integer satisfying $A\_n \\bmod p\_i = i$ for all $1 \\le i \\le n$, where $p\_i$ is the $i$-th prime.  
For example $A\_2 = 5$, since this is the smallest positive solution of the system of equations

-   $A\_2 \\bmod 2 = 1$
-   $A\_2 \\bmod 3 = 2$

The system of equations for $A\_3$ adds another constraint. That is, $A\_3$ is the smallest positive solution of

-   $A\_3 \\bmod 2 = 1$
-   $A\_3 \\bmod 3 = 2$
-   $A\_3 \\bmod 5 = 3$

and hence $A\_3 = 23$. Similarly, one gets $A\_4 = 53$ and $A\_5 = 1523$.

Let $S(n)$ be the sum of all primes up to $n$ that divide at least one element in the sequence $A$.  
For example, $S(50) = 69 = 5 + 23 + 41$, since $5$ divides $A\_2$, $23$ divides $A\_3$ and $41$ divides $A\_{10} = 5765999453$. No other prime number up to $50$ divides an element in $A$.

Find $S(300000)$.
