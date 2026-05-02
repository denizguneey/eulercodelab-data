# Problem 479: Roots on the Rise

Let $a\_k$, $b\_k$, and $c\_k$ represent the three solutions (real or complex numbers) to the equation $\\frac 1 x = (\\frac k x)^2(k+x^2)-k x$.

For instance, for $k=5$, we see that $\\{a\_5, b\_5, c\_5 \\}$ is approximately $\\{5.727244, -0.363622+2.057397i, -0.363622-2.057397i\\}$.

Let $\\displaystyle S(n) = \\sum\_{p=1}^n\\sum\_{k=1}^n(a\_k+b\_k)^p(b\_k+c\_k)^p(c\_k+a\_k)^p$.

Interestingly, $S(n)$ is always an integer. For example, $S(4) = 51160$.

Find $S(10^6)$ modulo $1\\,000\\,000\\,007$.
