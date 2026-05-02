# Problem 913: Row-major vs Column-major

The numbers from $1$ to $12$ can be arranged into a $3 \\times 4$ matrix in either **row-major** or **column-major** order: $$R=\\begin{pmatrix} 1 & 2 & 3 & 4\\\\ 5 & 6 & 7 & 8\\\\ 9 & 10 & 11 & 12\\end{pmatrix}, C=\\begin{pmatrix} 1 & 4 & 7 & 10\\\\ 2 & 5 & 8 & 11\\\\ 3 & 6 & 9 & 12\\end{pmatrix}$$ By swapping two entries at a time, at least $8$ swaps are needed to transform $R$ to $C$.

Let $S(n, m)$ be the minimal number of swaps needed to transform an $n\\times m$ matrix of $1$ to $nm$ from row-major order to column-major order. Thus $S(3, 4) = 8$.

You are given that the sum of $S(n, m)$ for $2 \\leq n \\leq m \\leq 100$ is $12578833$.

Find the sum of $S(n^4, m^4)$ for $2 \\leq n \\leq m \\leq 100$.
