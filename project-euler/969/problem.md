# Problem 969: Kangaroo Hopping

Starting at zero, a kangaroo hops along the real number line in the positive direction. Each successive hop takes the kangaroo forward a uniformly random distance between $0$ and $1$. Let $H(n)$ be the expected number of hops needed for the kangaroo to pass $n$ on the real line.

If we write $\\alpha = H(1)$, then for all positive integers $n$, $H(n)$ can be expressed as a polynomial function of $\\alpha$ with rational coefficients. For example $H(3)=\\alpha^3-2\\alpha^2+\\frac{1}{2}\\alpha$. Define $S(n)$ to be the sum of all **integer** coefficients in this polynomial form of $H(n)$. Therefore $S(1)=1$ and $S(3)=1+(-2)=-1$.  
You are also given $\\displaystyle \\sum\_{n=1}^{10} S(n)=43$.  
Find $\\displaystyle\\sum\_{n=1}^{10^{18}} S(n)$. Give your answer modulo $10^9+7$.
