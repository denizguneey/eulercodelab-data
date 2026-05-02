# Problem 435: Polynomials of Fibonacci Numbers

The **Fibonacci numbers** $\\{f\_n, n \\ge 0\\}$ are defined recursively as $f\_n = f\_{n-1} + f\_{n-2}$ with base cases $f\_0 = 0$ and $f\_1 = 1$.

Define the polynomials $\\{F\_n, n \\ge 0\\}$ as $F\_n(x) = \\displaystyle{\\sum\_{i=0}^n f\_i x^i}$.

For example, $F\_7(x) = x + x^2 + 2x^3 + 3x^4 + 5x^5 + 8x^6 + 13x^7$, and $F\_7(11) = 268\\,357\\,683$.

Let $n = 10^{15}$. Find the sum $\\displaystyle{\\sum\_{x=0}^{100} F\_n(x)}$ and give your answer modulo $1\\,307\\,674\\,368\\,000 \\ (= 15!)$.
