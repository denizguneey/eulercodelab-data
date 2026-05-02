# Problem 396: Weak Goodstein Sequence

For any positive integer $n$, the **$n$th weak Goodstein sequence** $\\{g\_1, g\_2, g\_3, \\dots\\}$ is defined as:

-   $g\_1 = n$
-   for $k \\gt 1$, $g\_k$ is obtained by writing $g\_{k-1}$ in base $k$, interpreting it as a base $k + 1$ number, and subtracting $1$.

The sequence terminates when $g\_k$ becomes $0$.

For example, the $6$th weak Goodstein sequence is $\\{6, 11, 17, 25, \\dots\\}$:

-   $g\_1 = 6$.
-   $g\_2 = 11$ since $6 = 110\_2$, $110\_3 = 12$, and $12 - 1 = 11$.
-   $g\_3 = 17$ since $11 = 102\_3$, $102\_4 = 18$, and $18 - 1 = 17$.
-   $g\_4 = 25$ since $17 = 101\_4$, $101\_5 = 26$, and $26 - 1 = 25$.

and so on.

It can be shown that every weak Goodstein sequence terminates.

Let $G(n)$ be the number of nonzero elements in the $n$th weak Goodstein sequence.  
It can be verified that $G(2) = 3$, $G(4) = 21$ and $G(6) = 381$.  
It can also be verified that $\\sum G(n) = 2517$ for $1 \\le n \\lt 8$.

Find the last $9$ digits of $\\sum G(n)$ for $1 \\le n \\lt 16$.
