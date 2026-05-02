import math

def solve(h=100.0, v=20.0, g=9.81):
    a = h + (v * v) / (2.0 * g)
    b = g / (2.0 * v * v)
    ans = math.pi * a * a / (2.0 * b)
    return f"{ans:.4f}"

if __name__ == '__main__':
    print(solve())
