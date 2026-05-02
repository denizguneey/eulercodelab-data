# Problem 137: Fibonacci golden nuggets
# The n-th golden nugget is F(2n) * F(2n+1).

def solve():
    index = 15
    need = 2 * index + 1
    f0, f1 = 0, 1
    for _ in range(2, need + 1):
        f0, f1 = f1, f0 + f1
    print(f0 * f1)

solve()
