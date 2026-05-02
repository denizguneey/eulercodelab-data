# Problem 647: Linear Transformations of Polygonal Numbers

It is possible to find positive integers $A$ and $B$ such that given any triangular number, $T\_n$, then $AT\_n +B$ is always a triangular number. We define $F\_3(N)$ to be the sum of $(A+B)$ over all such possible pairs $(A,B)$ with $\\max(A,B)\\le N$. For example $F\_3(100) = 184$.

Polygonal numbers are generalisations of triangular numbers. Polygonal numbers with parameter $k$ we call $k$-gonal numbers. The formula for the $n$th $k$-gonal number is $\\frac 12n\\big(n(k-2)+4-k\\big)$ where $n \\ge 1$. For example when $k = 3$ we get $\\frac 12n(n+1)$ the formula for triangular numbers.

The statement above is true for pentagonal, heptagonal and in fact any $k$-gonal number with $k$ odd. For example when $k=5$ we get the pentagonal numbers and we can find positive integers $A$ and $B$ such that given any pentagonal number, $P\_n$, then $AP\_n+B$ is always a pentagonal number. We define $F\_5(N)$ to be the sum of $(A+B)$ over all such possible pairs $(A,B)$ with $\\max(A,B)\\le N$.

Similarly we define $F\_k(N)$ for odd $k$. You are given $\\sum\_{k} F\_k(10^3) = 14993$ where the sum is over all odd $k = 3,5,7,\\ldots$.

Find $\\sum\_{k} F\_k(10^{12})$ where the sum is over all odd $k = 3,5,7,\\ldots$
