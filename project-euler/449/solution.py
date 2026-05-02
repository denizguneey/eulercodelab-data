import math

def integrand(theta, a, b):
    s = math.sin(theta)
    c = math.cos(theta)
    aa = a * a
    bb = b * b
    e = math.sqrt((s * s) / aa + (c * c) / bb)
    
    r = s * (a + 1.0 / (a * e))
    minus_z_prime = s * (b + 1.0 / (b * e) + (c * c / b) * (1.0 / aa - 1.0 / bb) / (e * e * e))
    return r * r * minus_z_prime

def simpson(l, r, a, b):
    m = (l + r) * 0.5
    return (r - l) * (integrand(l, a, b) + 4.0 * integrand(m, a, b) + integrand(r, a, b)) / 6.0

def adaptive_simpson(l, r, eps, whole, depth, a, b):
    m = (l + r) * 0.5
    left = simpson(l, m, a, b)
    right = simpson(m, r, a, b)
    delta = left + right - whole
    
    if depth <= 0 or abs(delta) <= 15.0 * eps:
        return left + right + delta / 15.0
    return adaptive_simpson(l, m, eps * 0.5, left, depth - 1, a, b) + \
           adaptive_simpson(m, r, eps * 0.5, right, depth - 1, a, b)

def compute_chocolate_volume(a, b):
    pi = 3.141592653589793238462643383279502884
    half_pi = pi * 0.5
    whole = simpson(0.0, half_pi, a, b)
    integral = adaptive_simpson(0.0, half_pi, 1e-14, whole, 24, a, b)
    
    outer = 2.0 * pi * integral
    inner = 4.0 * pi * a * a * b / 3.0
    return outer - inner

def solve():
    ans = compute_chocolate_volume(3.0, 1.0)
    return f"{ans:.8f}"

if __name__ == '__main__':
    print(solve())
