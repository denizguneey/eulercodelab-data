# Problem 631: Constrained Permutations

Let $(p\_1 p\_2 \\ldots p\_k)$ denote the permutation of the set ${1, ..., k}$ that maps $p\_i\\mapsto i$. Define the length of the permutation to be $k$; note that the empty permutation $()$ has length zero.

Define an occurrence of a permutation $p=(p\_1 p\_2 \\cdots p\_k)$ in a permutation $P=(P\_1 P\_2 \\cdots P\_n)$ to be a sequence $1\\leq t\_1 \\lt t\_2 \\lt \\cdots \\lt t\_k \\leq n$ such that $p\_i \\lt p\_j$ if and only if $P\_{t\_i} \\lt P\_{t\_j}$ for all $i,j \\in \\{1, \\dots, k\\}$.

For example, $(1243)$ occurs twice in the permutation $(314625)$: once as the 1st, 3rd, 4th and 6th elements $(3\\,\\,46\\,\\,5)$, and once as the 2nd, 3rd, 4th and 6th elements $(\\,\\,146\\,\\,5)$.

Let $f(n, m)$ be the number of permutations $P$ of length at most $n$ such that there is no occurrence of the permutation $1243$ in $P$ and there are at most $m$ occurrences of the permutation $21$ in $P$.

For example, $f(2,0) = 3$, with the permutations $()$, $(1)$, $(1,2)$ but not $(2,1)$.

You are also given that $f(4, 5) = 32$ and $f(10, 25) = 294\\,400$.

Find $f(10^{18}, 40)$ modulo $1\\,000\\,000\\,007$.
