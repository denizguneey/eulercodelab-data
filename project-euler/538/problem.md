# Problem 538: Maximum Quadrilaterals

Consider a positive integer sequence $S = (s\_1, s\_2, \\dots, s\_n)$.

Let $f(S)$ be the perimeter of the maximum-area quadrilateral whose side lengths are $4$ elements $(s\_i, s\_j, s\_k, s\_l)$ of $S$ (all $i, j, k, l$ distinct). If there are many quadrilaterals with the same maximum area, then choose the one with the largest perimeter.

For example, if $S = (8, 9, 14, 9, 27)$, then we can take the elements $(9, 14, 9, 27)$ and form an **isosceles trapeziumAn isosceles trapezium (US: trapezoid) is a quadrilateral where one pair of opposite sides are parallel and of different lengths, and the other pair has the same length.** with parallel side lengths $14$ and $27$ and both leg lengths $9$. The area of this quadrilateral is $127.611470879\\cdots$ It can be shown that this is the largest area for any quadrilateral that can be formed using side lengths from $S$. Therefore, $f(S) = 9 + 14 + 9 + 27 = 59$.

Let $u\_n = 2^{B(3n)} + 3^{B(2n)} + B(n + 1)$, where $B(k)$ is the number of $1$ bits of $k$ in base $2$.  
For example, $B(6) = 2$, $B(10) = 2$ and $B(15) = 4$, and $u\_5 = 2^4 + 3^2 + 2 = 27$.

Also, let $U\_n$ be the sequence $(u\_1, u\_2, \\dots, u\_n)$.  
For example, $U\_{10} = (8, 9, 14, 9, 27, 16, 36, 9, 27, 28)$.

It can be shown that $f(U\_5) = 59$, $f(U\_{10}) = 118$, $f(U\_{150}) = 3223$.  
It can also be shown that $\\sum f(U\_n) = 234761$ for $4 \\le n \\le 150$.  
Find $\\sum f(U\_n)$ for $4 \\le n \\le 3\\,000\\,000$.
