# Problem 902: Permutation Powers

A permutation $\\pi$ of $\\{1, \\dots, n\\}$ can be represented in **one-line notation** as $\\pi(1),\\ldots,\\pi(n) $. If all $n!$ permutations are written in lexicographic order then $\\textrm{rank}(\\pi)$ is the position of $\\pi$ in this 1-based list.

For example, $\\text{rank}(2,1,3) = 3$ because the six permutations of $\\{1, 2, 3\\}$ in lexicographic order are: $$1, 2, 3\\quad 1, 3, 2 \\quad 2, 1, 3 \\quad 2, 3, 1 \\quad 3, 1, 2 \\quad 3, 2, 1$$

For a positive integer $m$, we define the following permutation of $\\{1, \\dots, n\\}$ with $n = \\frac{m(m+1)}2$: $$ \\begin{align} \\sigma(i) &= \\begin{cases} \\frac{k(k-1)}2 + 1 & \\textrm{if } i = \\frac{k(k + 1)}2\\textrm{ for }k\\in\\{1, \\dots, m\\};\\\\i + 1 & \\textrm{otherwise};\\end{cases}\\\\ \\tau(i) &= ((10^9 + 7)i \\bmod n) + 1\\\\ \\pi(i) &= \\tau^{-1}(\\sigma(\\tau(i))) \\end{align} $$ where $\\tau^{-1}$ is the inverse permutation of $\\tau$.

Define $\\displaystyle P(m) = \\sum\_{k=1}^{m!} \\text{rank}(\\pi^k)$, where $\\pi^k$ is the permutation arising from applying $\\pi$ $k$ times.  
For example, $P(2) = 4$, $P(3) = 780$ and $P(4) = 38810300$.

Find $P(100)$. Give your answer modulo $(10^9 + 7)$.
