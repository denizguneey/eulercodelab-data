# Problem 738: Counting Ordered Factorisations

Define $d(n,k)$ to be the number of ways to write $n$ as a product of $k$ ordered integers

$$ n = x\_1\\times x\_2\\times x\_3\\times \\ldots\\times x\_k\\qquad 1\\le x\_1\\le x\_2\\le\\ldots\\le x\_k $$

Further define $D(N,K)$ to be the sum of $d(n,k)$ for $1\\le n\\le N$ and $1\\le k\\le K$.

You are given that $D(10, 10) = 153$ and $D(100, 100) = 35384$.

Find $D(10^{10},10^{10})$ giving your answer modulo $1\\,000\\,000\\,007$.
