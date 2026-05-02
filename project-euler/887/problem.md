# Problem 887: Bounded Binary Search

Consider the problem of determining a secret number from a set $\\{1, ..., N\\}$ by repeatedly choosing a number $y$ and asking "Is the secret number greater than $y$?".

If $N=1$ then no questions need to be asked. If $N=2$ then only one question needs to be asked. If $N=64$ then six questions need to be asked. However, in the latter case if the secret number is $1$ then six questions still need to be asked. We want to restrict the number of questions asked for small values.

Let $Q(N, d)$ be the least number of questions needed for a strategy that can find any secret number from the set $\\{1, ..., N\\}$ where no more than $x + d$ questions are needed to find the secret value $x$.

It can be proved that $Q(N, 0) = N - 1$. You are also given $Q(7, 1) = 3$ and $Q(777, 2) = 10$.

Find $\\displaystyle \\sum\_{d=0}^7 \\sum\_{N=1}^{7^{10}} Q(N, d)$.
