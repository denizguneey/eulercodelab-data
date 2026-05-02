import math

def area_inside_square_and_circle(r):
    kSqrt2 = math.sqrt(2.0)
    if r <= kSqrt2:
        return 0.0
    t = math.sqrt(r * r - 1.0)
    pi = math.acos(-1.0)
    return r * r * (pi / 4.0 - math.asin(1.0 / r)) - t + 1.0

def solve(max_k=100000):
    expected = 0.0
    for k in range(1, max_k + 1):
        outer = area_inside_square_and_circle(k + 0.5)
        inner = area_inside_square_and_circle(k - 0.5)
        expected += (outer - inner) / float(k)
    return f"{expected:.5f}"

if __name__ == '__main__':
    print(solve())
