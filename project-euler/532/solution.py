import math
import sys

sys.setrecursionlimit(20000)

def simpson(fa, fm, fb, a, b):
    return (b - a) * (fa + 4 * fm + fb) / 6.0

def integrand_u(u, s):
    uu = u * u
    su = s * u
    return math.sqrt(1.0 - su * su) / (1.0 - uu)

def adaptive_simpson(s, a, b, eps, whole, fa, fm, fb, depth):
    m = (a + b) / 2.0
    l = (a + m) / 2.0
    r = (m + b) / 2.0
    fl = integrand_u(l, s)
    fr = integrand_u(r, s)

    left = simpson(fa, fl, fm, a, m)
    right = simpson(fm, fr, fb, m, b)
    delta = left + right - whole
    
    if depth <= 0 or abs(delta) <= 15.0 * eps:
        return left + right + delta / 15.0
        
    return (adaptive_simpson(s, a, m, eps / 2.0, left, fa, fl, fm, depth - 1) +
            adaptive_simpson(s, m, b, eps / 2.0, right, fm, fr, fb, depth - 1))

def length_per_bot(n):
    s = math.sin(math.pi / n)
    u0 = 0.999
    
    a = 0.0
    b = u0
    m = (a + b) / 2.0
    fa = integrand_u(a, s)
    fb = integrand_u(b, s)
    fm = integrand_u(m, s)
    whole = simpson(fa, fm, fb, a, b)
    eps = 1e-13
    
    I = adaptive_simpson(s, a, b, eps, whole, fa, fm, fb, 30)
    return I / s

def solve():
    lo = 3
    hi = 3
    while length_per_bot(hi) <= 1000.0:
        hi *= 2
        
    while lo + 1 < hi:
        mid = lo + (hi - lo) // 2
        if length_per_bot(mid) > 1000.0:
            hi = mid
        else:
            lo = mid
            
    n = hi
    per = length_per_bot(n)
    total = n * per
    return f"{total:.2f}"

if __name__ == '__main__':
    print(solve())
