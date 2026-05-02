# Problem 921: Golden Recurrence

Consider the following recurrence relation: $$\\begin{align} a\_0 &= \\frac{\\sqrt 5 + 1}2\\\\ a\_{n+1} &= \\dfrac{a\_n(a\_n^4 + 10a\_n^2 + 5)}{5a\_n^4 + 10a\_n^2 + 1} \\end{align}$$

Note that $a\_0$ is the **golden ratio**.

$a\_n$ can always be written in the form $\\dfrac{p\_n\\sqrt{5}+1}{q\_n}$, where $p\_n$ and $q\_n$ are positive integers.

Let $s(n)=p\_n^5+q\_n^5$. So, $s(0)=1^5+2^5=33$.

The **Fibonacci sequence** is defined as: $F\_1=1$, $F\_2=1$, $F\_n=F\_{n-1}+F\_{n-2}$ for $n > 2$.

Define $\\displaystyle S(m)=\\sum\_{i=2}^{m}s(F\_i)$.

Find $S(1618034)$. Submit your answer modulo $398874989$.
