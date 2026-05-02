# Problem 577: Counting Hexagons

An equilateral triangle with integer side length $n \\ge 3$ is divided into $n^2$ equilateral triangles with side length 1 as shown in the diagram below.  
The vertices of these triangles constitute a triangular lattice with $\\frac{(n+1)(n+2)} 2$ lattice points.

Let $H(n)$ be the number of all regular hexagons that can be found by connecting 6 of these points.

![0577\_counting\_hexagons.png](./png/001.png)

For example, $H(3)=1$, $H(6)=12$ and $H(20)=966$.

Find $\\displaystyle \\sum\_{n=3}^{12345} H(n)$.
