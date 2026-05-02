# Problem 494: Collatz Prefix Families

The Collatz sequence is defined as: $a\_{i+1} = \\left\\{ \\large{\\frac {a\_i} 2 \\atop 3 a\_i+1} {\\text{if }a\_i\\text{ is even} \\atop \\text{if }a\_i\\text{ is odd}} \\right.$.

The Collatz conjecture states that starting from any positive integer, the sequence eventually reaches the cycle $1,4,2,1, \\dots$.  
We shall define the sequence prefix $p(n)$ for the Collatz sequence starting with $a\_1 = n$ as the sub-sequence of all numbers not a power of $2$ ($2^0=1$ is considered a power of $2$ for this problem). For example:  
$p(13) = \\{13, 40, 20, 10, 5\\}$  
$p(8) = \\{\\}$  
Any number invalidating the conjecture would have an infinite length sequence prefix.

Let $S\_m$ be the set of all sequence prefixes of length $m$. Two sequences $\\{a\_1, a\_2, \\dots, a\_m\\}$ and $\\{b\_1, b\_2, \\dots, b\_m\\}$ in $S\_m$ are said to belong to the same prefix family if $a\_i \\lt a\_j$ if and only if $b\_i \\lt b\_j$ for all $1 \\le i,j \\le m$.

For example, in $S\_4$, $\\{6, 3, 10, 5\\}$ is in the same family as $\\{454, 227, 682, 341\\}$, but not $\\{113, 340, 170, 85\\}$.  
Let $f(m)$ be the number of distinct prefix families in $S\_m$.  
You are given $f(5) = 5$, $f(10) = 55$, $f(20) = 6771$.

Find $f(90)$.
