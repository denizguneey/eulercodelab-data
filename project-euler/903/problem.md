# Problem 903: Total Permutation Powers

A permutation $\\pi$ of $\\{1, \\dots, n\\}$ can be represented in **one-line notation** as $\\pi(1),\\ldots,\\pi(n) $. If all $n!$ permutations are written in lexicographic order then $\\textrm{rank}(\\pi)$ is the position of $\\pi$ in this 1-based list.

For example, $\\text{rank}(2,1,3) = 3$ because the six permutations of $\\{1, 2, 3\\}$ in lexicographic order are: $$1, 2, 3\\quad 1, 3, 2 \\quad 2, 1, 3 \\quad 2, 3, 1 \\quad 3, 1, 2 \\quad 3, 2, 1$$

Let $Q(n)$ be the sum $\\sum\_{\\pi}\\sum\_{i = 1}^{n!} \\text{rank}(\\pi^i)$, where $\\pi$ ranges over all permutations of $\\{1, \\dots, n\\}$, and $\\pi^i$ is the permutation arising from applying $\\pi$ $i$ times.

For example, $Q(2) = 5$, $Q(3) = 88$, $Q(6) = 133103808$ and $Q(10) \\equiv 468421536 \\pmod {10^9 + 7}$.

Find $Q(10^6)$. Give your answer modulo $(10^9 + 7)$.
