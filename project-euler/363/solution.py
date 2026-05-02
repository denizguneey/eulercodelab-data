import math

def curve_speed(t, v):
    dx = 6.0 * (v - 1.0) * t + 3.0 * (2.0 - 3.0 * v) * t * t
    dy = 3.0 * v + 2.0 * (3.0 - 6.0 * v) * t + 3.0 * (3.0 * v - 2.0) * t * t
    return math.sqrt(dx * dx + dy * dy)

def adaptive_simpson(v, a, b, eps, whole, fa, fb, fm, depth):
    m = (a + b) * 0.5
    lm = (a + m) * 0.5
    rm = (m + b) * 0.5

    flm = curve_speed(lm, v)
    frm = curve_speed(rm, v)

    left = (m - a) * (fa + 4.0 * flm + fm) / 6.0
    right = (b - m) * (fm + 4.0 * frm + fb) / 6.0
    combined = left + right

    if depth <= 0 or abs(combined - whole) <= 15.0 * eps:
        return combined + (combined - whole) / 15.0

    return adaptive_simpson(v, a, m, eps * 0.5, left, fa, fm, flm, depth - 1) + \
           adaptive_simpson(v, m, b, eps * 0.5, right, fm, fb, frm, depth - 1)

def curve_length(v):
    a = 0.0
    b = 1.0
    fa = curve_speed(a, v)
    fb = curve_speed(b, v)
    m = 0.5
    fm = curve_speed(m, v)
    whole = (b - a) * (fa + 4.0 * fm + fb) / 6.0
    return adaptive_simpson(v, a, b, 1e-15, whole, fa, fb, fm, 30)

def solve_v():
    disc = 66.0 - 15.0 * math.acos(-1.0)
    return 2.0 - math.sqrt(disc) / 3.0

def solve():
    pi = math.acos(-1.0)
    v = solve_v()
    L = curve_length(v)
    percent = 100.0 * (L - pi / 2.0) / (pi / 2.0)
    return f"{percent:.10f}"

if __name__ == '__main__':
    print(solve())
