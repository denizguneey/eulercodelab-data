import math

def integrand_center_speed(a, b, t):
    s = math.sin(t)
    c = math.cos(t)
    num = a * b * math.sqrt(a * a * c * c + b * b * s * s)
    den = a * a * s * s + b * b * c * c
    return num / den

def simpson(fa, fm, fb, a, b):
    return (b - a) * (fa + 4 * fm + fb) / 6

def adaptive_simpson(a_param, b_param, a, b, eps, whole, fa, fm, fb, depth):
    m = (a + b) / 2
    l = (a + m) / 2
    r = (m + b) / 2
    
    fl = integrand_center_speed(a_param, b_param, l)
    fr = integrand_center_speed(a_param, b_param, r)
    
    left = simpson(fa, fl, fm, a, m)
    right = simpson(fm, fr, fb, m, b)
    delta = left + right - whole
    
    if depth <= 0 or abs(delta) <= 15 * eps:
        return left + right + delta / 15
        
    return adaptive_simpson(a_param, b_param, a, m, eps / 2, left, fa, fl, fm, depth - 1) + \
           adaptive_simpson(a_param, b_param, m, b, eps / 2, right, fm, fr, fb, depth - 1)

def integrate_center_curve_length(a, b):
    A = 0.0
    B = math.pi / 2
    fa = integrand_center_speed(a, b, A)
    fb = integrand_center_speed(a, b, B)
    m = (A + B) / 2
    fm = integrand_center_speed(a, b, m)
    whole = simpson(fa, fm, fb, A, B)
    eps = 1e-13
    quarter = adaptive_simpson(a, b, A, B, eps, whole, fa, fm, fb, 30)
    return 4 * quarter

def solve():
    c14 = integrate_center_curve_length(1.0, 4.0)
    c34 = integrate_center_curve_length(3.0, 4.0)
    ans = c14 + c34
    return f"{ans:.8f}"

if __name__ == '__main__':
    print(solve())
