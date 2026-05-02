# Problem 555: McCarthy 91 Function

The McCarthy 91 function is defined as follows: $$ M\_{91}(n) = \\begin{cases} n - 10 & \\text{if } n > 100 \\\\ M\_{91}(M\_{91}(n+11)) & \\text{if } 0 \\leq n \\leq 100 \\end{cases} $$

We can generalize this definition by abstracting away the constants into new variables: $$ M\_{m,k,s}(n) = \\begin{cases} n - s & \\text{if } n > m \\\\ M\_{m,k,s}(M\_{m,k,s}(n+k)) & \\text{if } 0 \\leq n \\leq m \\end{cases} $$

This way, we have $M\_{91} = M\_{100,11,10}$.

Let $F\_{m,k,s}$ be the set of fixed points of $M\_{m,k,s}$. That is, $$F\_{m,k,s}= \\left\\{ n \\in \\mathbb{N} \\, | \\, M\_{m,k,s}(n) = n \\right\\}$$

For example, the only fixed point of $M\_{91}$ is $n = 91$. In other words, $F\_{100,11,10}= \\{91\\}$.

Now, define $SF(m,k,s)$ as the sum of the elements in $F\_{m,k,s}$ and let $S(p,m) = \\displaystyle \\sum\_{1 \\leq s < k \\leq p}{SF(m,k,s)}$.

For example, $S(10, 10) = 225$ and $S(1000, 1000)=208724467$.

Find $S(10^6, 10^6)$.
