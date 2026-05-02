import sys
import math

PI = math.pi

def integral_distance(x, radius, simpson_n):
    a = 0.0
    b = 2.0 * PI
    h = (b - a) / float(simpson_n)
    
    acc = 0.0
    for i in range(simpson_n + 1):
        phi = a + h * i
        sinp = math.sin(phi)
        cosp = math.cos(phi)
        
        val = radius * radius - x * x * sinp * sinp
        rad = math.sqrt(max(0.0, val))
        
        s = -x * cosp + rad
        f = s * s * s
        
        coeff = 2
        if i == 0 or i == simpson_n:
            coeff = 1
        elif i % 2 == 1:
            coeff = 4
            
        acc += coeff * f
        
    return (h / 3.0) * acc / 3.0

def wasted_volume(x, radius, alpha_deg, simpson_n):
    tan_alpha = math.tan(alpha_deg * PI / 180.0)
    return tan_alpha * integral_distance(x, radius, simpson_n)

def solve_x_values(radius, alpha_deg, simpson_n):
    v0 = wasted_volume(0.0, radius, alpha_deg, simpson_n)
    vr = wasted_volume(radius, radius, alpha_deg, simpson_n)
    
    k_lo = int(math.ceil(math.sqrt(v0) - 1e-14))
    k_hi = int(math.floor(math.sqrt(vr) + 1e-14))
    
    xs = []
    for k in range(k_lo, k_hi + 1):
        target = float(k) * float(k)
        if target < v0 - 1e-12 or target > vr + 1e-12:
            continue
            
        lo = 0.0
        hi = radius
        for _ in range(120):
            mid = (lo + hi) * 0.5
            vm = wasted_volume(mid, radius, alpha_deg, simpson_n)
            if vm < target:
                lo = mid
            else:
                hi = mid
        xs.append((lo + hi) * 0.5)
        
    return xs

def solve():
    radius = 6.0
    alpha_deg = 40.0
    simpson_n = 4096
    
    xs = solve_x_values(radius, alpha_deg, simpson_n)
    ans = sum(xs)
    return f"{ans:.9f}"

if __name__ == '__main__':
    print(solve())
