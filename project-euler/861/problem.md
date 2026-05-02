# Problem 861: Products of Bi-Unitary Divisors

A _unitary divisor_ of a positive integer $n$ is a divisor $d$ of $n$ such that $\\gcd\\left(d,\\frac{n}{d}\\right)=1$.

A _bi-unitary divisor_ of $n$ is a divisor $d$ for which $1$ is the only unitary divisor of $d$ that is also a unitary divisor of $\\frac{n}{d}$.

For example, $2$ is a bi-unitary divisor of $8$, because the unitary divisors of $2$ are $\\{1,2\\}$, and the unitary divisors of $8/2$ are $\\{1,4\\}$, with $1$ being the only unitary divisor in common.

The bi-unitary divisors of $240$ are $\\{1,2,3,5,6,8,10,15,16,24,30,40,48,80,120,240\\}$.

Let $P(n)$ be the product of all bi-unitary divisors of $n$. Define $Q\_k(N)$ as the number of positive integers $1 \\lt n \\leq N$ such that $P(n)=n^k$. For example, $Q\_2\\left(10^2\\right)=51$ and $Q\_6\\left(10^6\\right)=6189$.

Find $\\sum\_{k=2}^{10}Q\_k\\left(10^{12}\\right)$.
