# Problem 197: A Recursively Defined Sequence

Given is the function $f(x) = \\lfloor 2^{30.403243784 - x^2}\\rfloor \\times 10^{-9}$ ($\\lfloor \\, \\rfloor$ is the floor-function),  
the sequence $u\_n$ is defined by $u\_0 = -1$ and $u\_{n + 1} = f(u\_n)$.

Find $u\_n + u\_{n + 1}$ for $n = 10^{12}$.  
Give your answer with $9$ digits after the decimal point.
