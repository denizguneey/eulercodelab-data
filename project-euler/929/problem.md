# Problem 929: Odd-Run Compositions

A **composition** of $n$ is a sequence of positive integers which sum to $n$. Such a sequence can be split into _runs_, where a run is a maximal contiguous subsequence of equal terms.

For example, $2,2,1,1,1,3,2,2$ is a composition of $14$ consisting of four runs:

$2, 2\\quad 1, 1, 1\\quad 3 \\quad 2, 2$

Let $F(n)$ be the number of compositions of $n$ where every run has odd length.

For example, $F(5)=10$:

$$\\begin{align\*} & 5 &&4,1 && 3,2 &&2,3 &&2,1,2\\\\ &2,1,1,1 &&1,4 &&1,3,1 &&1,1,1,2 &&1,1,1,1,1 \\end{align\*}$$

Find $F(10^5)$. Give your answer modulo $1111124111$.
