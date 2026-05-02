# Problem 920: Tau Numbers

For a positive integer $n$ we define $\\tau(n)$ to be the count of the divisors of $n$. For example, the divisors of $12$ are $\\{1,2,3,4,6,12\\}$ and so $\\tau(12) = 6$.

A positive integer $n$ is a **tau number** if it is divisible by $\\tau(n)$. For example $\\tau(12)=6$ and $6$ divides $12$ so $12$ is a tau number.

Let $m(k)$ be the smallest tau number $x$ such that $\\tau(x) = k$. For example, $m(8) = 24$, $m(12)=60$ and $m(16)=384$.

Further define $M(n)$ to be the sum of all $m(k)$ whose values do not exceed $10^n$. You are given $M(3) = 3189$.

Find $M(16)$.
