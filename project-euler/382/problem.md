# Problem 382: Generating Polygons

A **polygon** is a flat shape consisting of straight line segments that are joined to form a closed chain or circuit. A polygon consists of at least three sides and does not self-intersect.

A set $S$ of positive numbers is said to generate a polygon $P$ if:

-   no two sides of $P$ are the same length,
-   the length of every side of $P$ is in $S$, and
-   $S$ contains no other value.

For example:  
The set $\\{3, 4, 5\\}$ generates a polygon with sides $3$, $4$, and $5$ (a triangle).  
The set $\\{6, 9, 11, 24\\}$ generates a polygon with sides $6$, $9$, $11$, and $24$ (a quadrilateral).  
The sets $\\{1, 2, 3\\}$ and $\\{2, 3, 4, 9\\}$ do not generate any polygon at all.  

Consider the sequence $s$, defined as follows:

-   $s\_1 = 1$, $s\_2 = 2$, $s\_3 = 3$
-   $s\_n = s\_{n-1} + s\_{n-3}$ for $n \\gt 3$.

Let $U\_n$ be the set $\\{s\_1, s\_2, \\dots, s\_n\\}$. For example, $U\_{10} = \\{1, 2, 3, 4, 6, 9, 13, 19, 28, 41\\}$.  
Let $f(n)$ be the number of subsets of $U\_n$ which generate at least one polygon.  
For example, $f(5) = 7$, $f(10) = 501$ and $f(25) = 18635853$.

Find the last $9$ digits of $f(10^{18})$.
