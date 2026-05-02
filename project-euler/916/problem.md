# Problem 916: Restricted Permutations

Let $P(n)$ be the number of permutations of $\\{1,2,3,\\ldots,2n\\}$ such that:  
1\. There is no ascending subsequence with more than $n+1$ elements, and  
2\. There is no descending subsequence with more than two elements.

Note that subsequences need not be contiguous. For example, the permutation $(4,1,3,2)$ is not counted because it has a descending subsequence of three elements: $(4,3,2)$. You are given $P(2)=13$ and $P(10) \\equiv 45265702 \\pmod{10^9 + 7}$.

Find $P(10^8)$ and give your answer modulo $10^9 + 7$.
