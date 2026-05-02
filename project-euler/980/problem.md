# Problem 980: The Quaternion Group I

Starting from an empty string, we want to build a string with letters "x", "y", "z". At each step, one of the following operations is performed:

-   insert two consecutive identical letters "xx", "yy" or "zz" anywhere into the string;
-   replace one letter in the string with two consecutive letters, according to the rule: "x" $\\to$ "yz", "y" $\\to$ "zx", "z" $\\to$ "xy";
-   exchange two consecutive **different** letters in the string, e.g. "xy" $\\to$ "yx", "zx" $\\to$ "xz", etc.

A string is called neutral if it is possible to produce the string from the empty string after an **even** number of steps.

We define a sequence $(a\_n)\_{n \\ge 0}$: $a\_0=88\\,888\\,888$ and $a\_n=(8888\\cdot a\_{n-1})\\bmod 888\\,888\\,883$ for $n \\gt 0$.

Let $b\_n = a\_n \\bmod 3$. For each $i \\ge 0$, a string $c(i)$ of length $50$ is defined by translating the finite sequence $b\_{50i},b\_{50i+1},\\dots,b\_{50i+49}$ via the rule: $0 \\to$ "x", $1 \\to$ "y", $2 \\to$ "z".

Let $F(N)$ be the number of ordered pairs $(i, j)$ with $0 \\le i, j \\lt N$ such that the concatenated string $c(i)c(j)$ is neutral.  
For example, $F(10) = 13$ and $F(100) = 1224$.

Find $F(10^6)$.
