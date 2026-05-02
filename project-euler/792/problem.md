# Problem 792: Too Many Twos

We define $\\nu\_2(n)$ to be the largest integer $r$ such that $2^r$ divides $n$. For example, $\\nu\_2(24) = 3$.

Define $\\displaystyle S(n) = \\sum\_{k = 1}^n (-2)^k\\binom{2k}k$ and $u(n) = \\nu\_2\\Big(3S(n)+4\\Big)$.

For example, when $n = 4$ then $S(4) = 980$ and $3S(4) + 4 = 2944 = 2^7 \\cdot 23$, hence $u(4) = 7$.  
You are also given $u(20) = 24$.

Also define $\\displaystyle U(N) = \\sum\_{n = 1}^N u(n^3)$. You are given $U(5) = 241$.

Find $U(10^4)$.
