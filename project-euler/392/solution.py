import math

def f(x):
    inside = 1.0 - x * x
    return math.sqrt(max(0.0, inside))

def build_sequence(m, x1):
    x = [0.0] * (m + 2)
    x[0] = 0.0
    x[1] = x1

    if not (0.0 < x1 < 1.0):
        return None

    for k in range(1, m + 1):
        x_prev = x[k - 1]
        x_cur = x[k]
        y_prev = f(x_prev)
        y_cur = f(x_cur)

        if x_cur <= 0.0 or y_cur <= 0.0:
            return None

        x_next = x_cur + (y_prev - y_cur) * y_cur / x_cur
        if not math.isfinite(x_next):
            return None
        x[k + 1] = x_next
    return x

def shooting_residual(m, x1):
    x = build_sequence(m, x1)
    if x is None:
        return float('inf')
    return x[m + 1] - 1.0

def solve_breakpoints(n):
    m = n // 2
    lo = 1e-18
    hi = 0.999999999999

    for _ in range(260):
        mid = (lo + hi) / 2.0
        r = shooting_residual(m, mid)
        if r > 0.0:
            hi = mid
        else:
            lo = mid

    x1 = (lo + hi) / 2.0
    x = build_sequence(m, x1)
    x[m + 1] = 1.0
    return x

def minimal_red_area(n):
    m = n // 2
    x = solve_breakpoints(n)

    quadrant_area = 0.0
    for i in range(m + 1):
        width = x[i + 1] - x[i]
        quadrant_area += width * f(x[i])

    return 4.0 * quadrant_area

def solve():
    n = 400
    answer = minimal_red_area(n)
    return "{:.10f}".format(answer)

if __name__ == '__main__':
    print(solve())
