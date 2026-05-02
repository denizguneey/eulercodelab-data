# Problem 703: Circular Logic II

Given an integer $n$, $n \\geq 3$, let $B=\\{\\mathrm{false},\\mathrm{true}\\}$ and let $B^n$ be the set of sequences of $n$ values from $B$. The function $f$ from $B^n$ to $B^n$ is defined by $f(b\_1 \\dots b\_n) = c\_1 \\dots c\_n$ where:

-   $c\_i = b\_{i+1}$ for $1 \\leq i < n$.
-   $c\_n = b\_1 \\;\\mathrm{AND}\\; (b\_2 \\;\\mathrm{XOR}\\; b\_3)$, where $\\mathrm{AND}$ and $\\mathrm{XOR}$ are the logical $\\mathrm{AND}$ and exclusive $\\mathrm{OR}$ operations.

Let $S(n)$ be the number of functions $T$ from $B^n$ to $B$ such that for all $x$ in $B^n$, $T(x) ~\\mathrm{AND}~ T(f(x)) = \\mathrm{false}$. You are given that $S(3) = 35$ and $S(4) = 2118$.

Find $S(20)$. Give your answer modulo $1\\,001\\,001\\,011$.
