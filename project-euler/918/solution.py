import sys

sys.setrecursionlimit(2000)

def pair_value(n):
    if n == 1:
        return 1, 2
    if (n & 1) == 0:
        x, y = pair_value(n >> 1)
        return 2 * x, x - 3 * y
    x, y = pair_value(n >> 1)
    return x - 3 * y, 2 * y

def a_value(n):
    return pair_value(n)[0]

def prefix_sum(n):
    if (n & 1) == 0:
        return 4 - a_value(n >> 1)
    return 4 - 3 * a_value((n + 1) >> 1)

def solve():
    return str(prefix_sum(1000000000000))

if __name__ == "__main__":
    print(solve())
