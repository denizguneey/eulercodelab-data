import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(a, b):
    return math.hypot(a.x - b.x, a.y - b.y)

def circumcenter(p1, p2, p3):
    x1, y1 = p1.x, p1.y
    x2, y2 = p2.x, p2.y
    x3, y3 = p3.x, p3.y
    
    den = 2.0 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    
    n1 = x1 * x1 + y1 * y1
    n2 = x2 * x2 + y2 * y2
    n3 = x3 * x3 + y3 * y3
    
    ux = (n1 * (y2 - y3) + n2 * (y3 - y1) + n3 * (y1 - y2)) / den
    uy = (n1 * (x3 - x2) + n2 * (x1 - x3) + n3 * (x2 - x1)) / den
    
    return Point(ux, uy)

def d_value(ra, rb, rc):
    a = float(ra)
    b = float(rb)
    c = float(rc)
    
    A = Point(0.0, 0.0)
    B = Point(a + b, 0.0)
    
    cx = ((a + c) * (a + c) + (a + b) * (a + b) - (b + c) * (b + c)) / (2.0 * (a + b))
    cy = math.sqrt(max(0.0, (a + c) * (a + c) - cx * cx))
    C = Point(cx, cy)
    
    Pab = Point(a, 0.0)
    Pac = Point(a / (a + c) * cx, a / (a + c) * cy)
    Pbc = Point(B.x + b / (b + c) * (cx - B.x), b / (b + c) * cy)
    
    D = circumcenter(Pab, Pac, Pbc)
    
    k1 = 1.0 / a
    k2 = 1.0 / b
    k3 = 1.0 / c
    k4 = k1 + k2 + k3 + 2.0 * math.sqrt(k1 * k2 + k2 * k3 + k3 * k1)
    r = 1.0 / k4
    
    rhs_ab = (B.x * B.x + B.y * B.y) + (a + r) * (a + r) - (b + r) * (b + r)
    ex = rhs_ab / (2.0 * B.x)
    
    rhs_ac = (C.x * C.x + C.y * C.y) + (a + r) * (a + r) - (c + r) * (c + r)
    ey = (rhs_ac - 2.0 * C.x * ex) / (2.0 * C.y)
    E = Point(ex, ey)
    
    return distance(D, E)

def solve():
    total_sum = 0.0
    count = 0
    
    for a in range(1, 101):
        for b in range(a + 1, 101):
            for c in range(b + 1, 101):
                if math.gcd(a, math.gcd(b, c)) != 1:
                    continue
                total_sum += d_value(a, b, c)
                count += 1
                
    ans = total_sum / count
    return f"{ans:.8f}"

if __name__ == "__main__":
    print(solve())
