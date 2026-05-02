# Problem 546: The Floor's Revenge

Define $f\_k(n) = \\sum\_{i=0}^n f\_k(\\lfloor\\frac i k \\rfloor)$ where $f\_k(0) = 1$ and $\\lfloor x \\rfloor$ denotes the floor function.

For example, $f\_5(10) = 18$, $f\_7(100) = 1003$, and $f\_2(10^3) = 264830889564$.

Find $(\\sum\_{k=2}^{10} f\_k(10^{14})) \\bmod (10^9+7)$.
