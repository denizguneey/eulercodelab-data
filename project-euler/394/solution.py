import math

def expected_steps(x):
    return 7.0 / 9.0 + (2.0 / 3.0) * math.log(x) + 2.0 / (9.0 * x * x * x)

def solve():
    return "{:.10f}".format(expected_steps(40.0))

if __name__ == '__main__':
    print(solve())
