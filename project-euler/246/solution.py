import math
import multiprocessing

def isqrt_u128(x):
    if x < 0: return 0
    return math.isqrt(x)

class EllipseData:
    def __init__(self, a2, b2):
        self.a2 = a2
        self.b2 = b2
        self.r2_circle = a2 + b2
        self.ab2 = a2 * b2

def min_y_outside(x, e):
    lhs = e.b2 * x * x
    rhs = e.a2 * e.b2
    if lhs > rhs: return 0
    if lhs == rhs: return 1
    rem = rhs - lhs
    q = rem // e.a2
    y = isqrt_u128(q)
    while e.a2 * y * y <= rem:
        y += 1
    return y

def angle_ineq(x, u, e):
    x2 = x * x
    term1 = 4 * (e.b2 * x2 + e.a2 * u - e.ab2)
    t = e.a2 + e.b2 - x2 - u
    return term1 - t * t

def max_y_outside(x, e):
    x2 = x * x
    k = e.a2 + e.b2 - x2
    b = 4 * e.a2 + 2 * k
    c = 4 * (e.b2 * x2 - e.ab2) - k * k
    d = b * b + 4 * c
    if d <= 0: return -1
    
    sqrt_d = isqrt_u128(d)
    u_max = (b + sqrt_d) // 2
    if u_max < 0: return -1
    
    while u_max >= 0 and angle_ineq(x, u_max, e) <= 0:
        u_max -= 1
        
    if u_max < 0: return -1
    y = isqrt_u128(u_max)
    while y >= 0 and angle_ineq(x, y * y, e) <= 0:
        y -= 1
        
    return y

def qualifies(x, y, e):
    x2 = x * x
    y2 = y * y
    if e.b2 * x2 + e.a2 * y2 <= e.ab2:
        return False
    r2 = x2 + y2
    if r2 <= e.r2_circle:
        return True
    return angle_ineq(x, y2, e) > 0

def worker(args):
    start, end, e = args
    local = 0
    for x in range(start, end):
        y_min = min_y_outside(x, e)
        y_circle = -1
        x2 = x * x
        if x2 <= e.r2_circle:
            y_circle = isqrt_u128(e.r2_circle - x2)
            
        if y_circle >= y_min:
            local += y_circle - y_min + 1
            
        y_start = max(y_min, y_circle + 1)
        y_max = max_y_outside(x, e)
        
        if y_max >= y_start:
            local += y_max - y_start + 1
            
    return local

def solve():
    kMx = -2000
    kMy = 1500
    kGx = 8000
    kGy = 1500
    kRadius = 15000
    
    d = abs(kGx - kMx)
    a = kRadius // 2
    c = d // 2
    a2 = a * a
    b2 = a2 - c * c
    
    e = EllipseData(a2, b2)
    
    x_limit = isqrt_u128(e.a2 + 6 * e.b2) + 2
    y_limit = isqrt_u128(e.b2 + 6 * e.a2) + 2
    
    threads = max(1, multiprocessing.cpu_count())
    total_x = x_limit + 1
    chunk = (total_x + threads - 1) // threads
    
    tasks = []
    for t in range(threads):
        start = t * chunk
        end = min(start + chunk, total_x)
        if start >= end: break
        tasks.append((start, end, e))
        
    count_q1 = 0
    if threads > 1 and len(tasks) > 1:
        with multiprocessing.Pool(threads) as pool:
            results = pool.map(worker, tasks)
            count_q1 = sum(results)
    else:
        for t in tasks:
            count_q1 += worker(t)
            
    count_x_axis = sum(1 for x in range(x_limit + 1) if qualifies(x, 0, e))
    count_y_axis = sum(1 for y in range(y_limit + 1) if qualifies(0, y, e))
    origin = 1 if qualifies(0, 0, e) else 0
    
    ans = 4 * count_q1 - 2 * count_x_axis - 2 * count_y_axis + origin
    return str(ans)

if __name__ == '__main__':
    print(solve())
