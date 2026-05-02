# Problem 850: Fractions of Powers

Any positive real number $x$ can be decomposed into integer and fractional parts $\\lfloor x \\rfloor + \\{x\\}$, where $\\lfloor x \\rfloor$ (the floor function) is an integer, and $0\\le \\{x\\} < 1$.

For positive integers $k$ and $n$, define the function $$\\begin{align} f\_k(n) = \\sum\_{i=1}^{n}\\left\\{ \\frac{i^k}{n} \\right\\} \\end{align}$$ For example, $f\_5(10)=4.5$ and $f\_7(1234)=616.5$.

Let $$\\begin{align} S(N) = \\sum\_{\\substack{k=1 \\\\ k\\text{ odd}}}^{N} \\sum\_{n=1}^{N} f\_k(n) \\end{align}$$ You are given that $S(10)=100.5$ and $S(10^3)=123687804$.

Find $\\lfloor S(33557799775533) \\rfloor$. Give your answer modulo 977676779.
