# Problem 212: Combined Volume of Cuboids

An axis-aligned cuboid, specified by parameters $\\{(x\_0, y\_0, z\_0), (dx, dy, dz)\\}$, consists of all points $(X,Y,Z)$ such that $x\_0 \\le X \\le x\_0 + dx$, $y\_0 \\le Y \\le y\_0 + dy$ and $z\_0 \\le Z \\le z\_0 + dz$. The volume of the cuboid is the product, $dx \\times dy \\times dz$. The combined volume of a collection of cuboids is the volume of their union and will be less than the sum of the individual volumes if any cuboids overlap.

Let $C\_1, \\dots, C\_{50000}$ be a collection of $50000$ axis-aligned cuboids such that $C\_n$ has parameters

$$\\begin{align} x\_0 &= S\_{6n - 5} \\bmod 10000\\\\ y\_0 &= S\_{6n - 4} \\bmod 10000\\\\ z\_0 &= S\_{6n - 3} \\bmod 10000\\\\ dx &= 1 + (S\_{6n - 2} \\bmod 399)\\\\ dy &= 1 + (S\_{6n - 1} \\bmod 399)\\\\ dz &= 1 + (S\_{6n} \\bmod 399) \\end{align}$$

where $S\_1,\\dots,S\_{300000}$ come from the "Lagged Fibonacci Generator":

-   For $1 \\le k \\le 55$, $S\_k = \[100003 - 200003k + 300007k^3\] \\pmod{1000000}$.
-   For $56 \\le k$, $S\_k = \[S\_{k -24} + S\_{k - 55}\] \\pmod{1000000}$.

Thus, $C\_1$ has parameters $\\{(7,53,183),(94,369,56)\\}$, $C\_2$ has parameters $\\{(2383,3563,5079),(42,212,344)\\}$, and so on.

The combined volume of the first $100$ cuboids, $C\_1, \\dots, C\_{100}$, is $723581599$.

What is the combined volume of all $50000$ cuboids, $C\_1, \\dots, C\_{50000}$?
