# Problem 651: Patterned Cylinders

An infinitely long cylinder has its curved surface fully covered with different coloured but otherwise identical rectangular stickers, without overlapping. The stickers are aligned with the cylinder, so two of their edges are parallel with the cylinder's axis, with four stickers meeting at each corner.

Let $a>0$ and suppose that the colouring is periodic along the cylinder, with the pattern repeating every $a$ stickers. (The period is allowed to be any divisor of $a$.) Let $b$ be the number of stickers that fit round the circumference of the cylinder.

Let $f(m, a, b)$ be the number of different such periodic patterns that use _exactly_ $m$ distinct colours of stickers. Translations along the axis, reflections in any plane, rotations in any axis, (or combinations of such operations) applied to a pattern are to be counted as the same as the original pattern.

You are given that $f(2, 2, 3) = 11$, $f(3, 2, 3) = 56$, and $f(2, 3, 4) = 156$. Furthermore, $f(8, 13, 21) \\equiv 49718354 \\pmod{1\\,000\\,000\\,007}$, and $f(13, 144, 233) \\equiv 907081451 \\pmod{1\\,000\\,000\\,007}$.

Find $\\sum\_{i=4}^{40} f(i, F\_{i-1}, F\_i) \\bmod 1\\,000\\,000\\,007$, where $F\_i$ are the Fibonacci numbers starting at $F\_0=0$, $F\_1=1$.
