import math
import cmath

PI = math.pi

def abs_one_minus_q_pow(s, t, n):
    rn = s ** n
    ang = n * t
    qn = cmath.rect(rn, ang)
    return abs(1.0 - qn)

def equations(s, t):
    a1 = abs_one_minus_q_pow(s, t, 1)
    a7 = abs_one_minus_q_pow(s, t, 7)
    a8 = abs_one_minus_q_pow(s, t, 8)

    f7 = (1.0 + s) * a7 - (1.0 + s ** 7) * a1
    f8 = (1.0 + s) * a8 - (1.0 + s ** 8) * a1
    return f7, f8

def circular_triangle_area(r1, r2, r3):
    a = r2 + r3
    b = r1 + r3
    c = r1 + r2

    p = (a + b + c) / 2.0
    val = p * (p - a) * (p - b) * (p - c)
    tri = math.sqrt(val) if val > 0 else 0.0

    A1 = math.acos((b * b + c * c - a * a) / (2.0 * b * c))
    A2 = math.acos((a * a + c * c - b * b) / (2.0 * a * c))
    A3 = math.acos((a * a + b * b - c * c) / (2.0 * a * b))

    return tri - 0.5 * (r1 * r1 * A1 + r2 * r2 * A2 + r3 * r3 * A3)

def solve():
    s = 0.9
    t = 0.83

    for _ in range(80):
        f1, f2 = equations(s, t)

        h = 1e-10
        f1s, f2s = equations(s + h, t)
        f1t, f2t = equations(s, t + h)

        j11 = (f1s - f1) / h
        j21 = (f2s - f2) / h
        j12 = (f1t - f1) / h
        j22 = (f2t - f2) / h

        det = j11 * j22 - j12 * j21
        
        ds = (-f1 * j22 + f2 * j12) / det
        dt = (-j11 * f2 + j21 * f1) / det

        s += ds
        t += dt

        while t < 0:
            t += 2 * PI
        while t >= 2 * PI:
            t -= 2 * PI

        if abs(ds) + abs(dt) < 1e-15:
            break

    A = circular_triangle_area(1.0, s, s ** 8)
    B = circular_triangle_area(1.0, s ** 7, s ** 8)
    total = (A + B) / (1.0 - s * s)

    return f"{total:.10f}"

if __name__ == "__main__":
    print(solve())
