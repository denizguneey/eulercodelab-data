import math

def p4(x):
    x2 = x * x
    return x2 * x2

def optimal_knots(n):
    m = n - 1
    x = [0.0] * (m + 1)
    for i in range(m + 1):
        x[i] = -1.0 + 2.0 * i / m
        
    omega = 0.5
    tol = 1e-15
    max_iter = 300000
    
    for _ in range(max_iter):
        max_delta = 0.0
        for i in range(1, m):
            a = x[i - 1]
            b = x[i + 1]
            val = (p4(b) - p4(a)) / (4.0 * (b - a))
            target = math.copysign(abs(val)**(1.0/3.0), val) if val != 0 else 0.0
            
            nx = x[i] + omega * (target - x[i])
            d = abs(nx - x[i])
            if d > max_delta:
                max_delta = d
            x[i] = nx
            
        if max_delta < tol:
            break
            
    return x

def polygon_area(x):
    m = len(x) - 1
    area = 0.0
    for i in range(m):
        dx = x[i + 1] - x[i]
        area += (2.0 - (p4(x[i]) + p4(x[i + 1]))) * dx * 0.5
    return area

def G(n):
    return polygon_area(optimal_knots(n))

def solve():
    return f"{G(101):.9f}"

if __name__ == "__main__":
    print(solve())
