# Problem 180: Golden Triplets

For any integer $n$, consider the three functions

$$\\begin{align} f\_{1, n}(x, y, z) &= x^{n + 1} + y^{n + 1} - z^{n + 1}\\\\ f\_{2, n}(x, y, z) &= (xy + yz + zx) \\cdot (x^{n - 1} + y^{n - 1} - z^{n - 1})\\\\ f\_{3, n}(x, y, z) &= xyz \\cdot (x^{n - 2} + y^{n - 2} - z^{n - 2}) \\end{align}$$

and their combination $$f\_n(x, y, z) = f\_{1, n}(x, y, z) + f\_{2, n}(x, y, z) - f\_{3, n}(x, y, z).$$

We call $(x, y, z)$ a golden triple of order $k$ if $x$, $y$, and $z$ are all rational numbers of the form $a / b$ with $0 \\lt a \\lt b \\le k$ and there is (at least) one integer $n$, so that $f\_n(x, y, z) = 0$.

Let $s(x, y, z) = x + y + z$.  
Let $t = u / v$ be the sum of all distinct $s(x, y, z)$ for all golden triples $(x, y, z)$ of order $35$.  
All the $s(x, y, z)$ and $t$ must be in reduced form.

Find $u + v$.
