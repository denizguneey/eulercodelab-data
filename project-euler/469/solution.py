import math

def solve():
    N = 10**18
    # For large n, E(n) = (1 + exp(-2))/2 with negligible error
    ans = 0.5 * (1.0 + math.exp(-2.0))
    return f"{ans:.14f}"

if __name__ == '__main__':
    print(solve())
