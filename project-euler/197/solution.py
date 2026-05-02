# Problem 197: Investigating the behaviour of a recursively defined sequence.
# f(x) = floor(2^(30.403243784-x^2)) * 10^-9
# u_n+1 = f(u_n), u_0 = -1. Find u_n + u_(n+1) for large n.

import math

def solve():
    def f(x):
        return math.floor(2**(30.403243784 - x*x)) * 1e-9
    u = -1.0
    for _ in range(1000):
        u = f(u)
    v = f(u)
    print(f"{u+v:.9f}")

solve()
