# Problem 924: Larger Digit Permutation II

Let $B(n)$ be the smallest number larger than $n$ that can be formed by rearranging digits of $n$, or $0$ if no such number exists. For example, $B(245) = 254$ and $B(542) = 0$.

Define $a\_0 = 0$ and $a\_n = a\_{n - 1}^2 + 2$ for $n>0$. Let $\\displaystyle U(N) = \\sum\_{n = 1}^N B(a\_n)$. You are given $U(10) \\equiv 543870437 \\pmod{10^9+7}$.

Find $U(10^{16})$. Give your answer modulo $10^9 + 7$.
