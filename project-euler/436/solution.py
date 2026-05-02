import math

def solve():
    e = math.e
    ans = (1.0 + 14.0 * e - 5.0 * e * e) / 4.0
    return f"{ans:.10f}"

if __name__ == '__main__':
    print(solve())
