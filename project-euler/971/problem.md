# Problem 971: Modular Polynomial Composition

Let $p$ be a prime of the form $5k-4$ and define $f\_p(x) = \\left(x^k+x\\right) \\bmod p$.

Let $C(p)$ be the number of values $0 \\le x \\lt p$ such that $f\_p^{(m)}(x) = x$ for some positive integer $m$, that is, $x$ can be obtained by iteratively applying $f\_p$ on itself starting at $x$.

For example, $C(11) = 7$, due to $x = 0, 1, 2, 3, 8, 9, 10$.

Let $S(N)$ be the sum of $C(p)$ for all primes of the form $5k-4$ not exceeding $N$. For example $S(100) = 127$.

Find $S(10^8)$.
