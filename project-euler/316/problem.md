# Problem 316: Numbers in Decimal Expansions

Let $p = p\_1 p\_2 p\_3 \\cdots$ be an infinite sequence of random digits, selected from $\\{0,1,2,3,4,5,6,7,8,9\\}$ with equal probability.  
It can be seen that $p$ corresponds to the real number $0.p\_1 p\_2 p\_3 \\cdots$  
It can also be seen that choosing a random real number from the interval $\[0,1)$ is equivalent to choosing an infinite sequence of random digits selected from $\\{0,1,2,3,4,5,6,7,8,9\\}$ with equal probability.

For any positive integer $n$ with $d$ decimal digits, let $k$ be the smallest index such that $p\_k, p\_{k + 1}, \\dots, p\_{k + d - 1}$ are the decimal digits of $n$, in the same order.  
Also, let $g(n)$ be the expected value of $k$; it can be proven that $g(n)$ is always finite and, interestingly, always an integer number.

For example, if $n = 535$, then  
for $p = 31415926\\mathbf{535}897\\cdots$, we get $k = 9$  
for $p = 35528714365004956000049084876408468\\mathbf{535}4\\cdots$, we get $k = 36$  
etc and we find that $g(535) = 1008$.

Given that $\\displaystyle\\sum\_{n = 2}^{999} g \\left(\\left\\lfloor\\frac{10^6} n \\right\\rfloor\\right) = 27280188$, find $\\displaystyle\\sum\_{n = 2}^{999999} g \\left(\\left\\lfloor\\frac{10^{16}} n \\right\\rfloor\\right)$.

_Note_: $\\lfloor x \\rfloor$ represents the floor function.
