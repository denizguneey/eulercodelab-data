from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def solve(n=20):
    value = 1
    for k in range(2, n + 1):
        value = lcm(value, k)
    return value

if __name__ == "__main__":
    assert solve(10) == 2520, "Checkpoint failed for n=10"
    print(solve())
