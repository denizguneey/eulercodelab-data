# Problem 794: Seventeen Points

This problem uses half open interval notation where $\[a,b)$ represents $a \\le x \\lt b$.

A real number, $x\_1$, is chosen in the interval $\[0,1)$.  
A second real number, $x\_2$, is chosen such that each of $\[0,\\frac{1}{2})$ and $\[\\frac{1}{2},1)$ contains exactly one of $(x\_1, x\_2)$.  
Continue such that on the $n$-th step a real number, $x\_n$, is chosen so that each of the intervals $\[\\frac{k-1}{n}, \\frac{k}{n})$ for $k \\in \\{1, \\dots, n\\}$ contains exactly one of $(x\_1, x\_2, \\dots, x\_n)$.

Define $F(n)$ to be the minimal value of the sum $x\_1 + x\_2 + \\cdots + x\_n$ of a tuple $(x\_1, x\_2, \\dots, x\_n)$ chosen by such a procedure. For example, $F(4) = 1.5$ obtained with $(x\_1, x\_2, x\_3, x\_4) = (0, 0.75, 0.5, 0.25)$.

Surprisingly, no more than $17$ points can be chosen by this procedure.

Find $F(17)$ and give your answer rounded to $12$ decimal places.
