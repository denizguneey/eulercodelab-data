# Problem 774: Conjunctive Sequences

Let '$\\&$' denote the bitwise AND operation.  
For example, $10\\,\\&\\, 12 = 1010\_2\\,\\&\\, 1100\_2 = 1000\_2 = 8$.

We shall call a finite sequence of non-negative integers $(a\_1, a\_2, \\ldots, a\_n)$ conjunctive if $a\_i\\,\\&\\, a\_{i+1} \\neq 0$ for all $i=1\\ldots n-1$.

Define $c(n,b)$ to be the number of conjunctive sequences of length $n$ in which all terms are $\\le b$.

You are given that $c(3,4)=18$, $c(10,6)=2496120$, and $c(100,200) \\equiv 268159379 \\pmod {998244353}$.

Find $c(123,123456789)$. Give your answer modulo $998244353$.
