# Problem 854: Pisano Periods 2

For every positive integer $n$ the Fibonacci sequence modulo $n$ is periodic. The period depends on the value of $n$. This period is called the **Pisano period** for $n$, often shortened to $\\pi(n)$.

Define $M(p)$ as the largest integer $n$ such that $\\pi(n) = p$, and define $M(p) = 1$ if there is no such $n$.  
For example, there are three values of $n$ for which $\\pi(n)$ equals $18$: $19, 38, 76$. Therefore $M(18) = 76$.

Let the product function $P(n)$ be: $$P(n)=\\prod\_{p = 1}^{n}M(p).$$ You are given: $P(10)=264$.

Find $P(1\\,000\\,000)\\bmod 1\\,234\\,567\\,891$.
