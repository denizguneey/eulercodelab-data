# Problem 967: $B$-Trivisible Numbers

A positive integer $n$ is considered _$B$-trivisible_ if the sum of all different prime factors of $n$ which are not larger than $B$ is divisible by $3$.

For example, $175 = 5^2 \\cdot 7$ is $10$-trivisible because $5 + 7 = 12$ which is divisible by $3$. Similarly, $175$ is $4$-trivisible because all primes dividing $175$ are larger than $4$, and the empty summation $0$ is divisible by $3$.  
On the other hand, $175$ is not $6$-trivisible because the sum of relevant primes is $5$ which is not divisible by $3$.

Let $F(N, B)$ be the number of $B$-trivisible integers not larger than $N$.

For example, $F(10, 4) = 5$, the $4$-trivisible numbers being $1,3,5,7,9$.  
You are also given $F(10, 10) = 3$ and $F(100, 10) = 41$.

Find $F(10^{18}, 120)$.
