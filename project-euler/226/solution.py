import math
import multiprocessing

def prefix_popcount(n):
    total = 0
    for bit in range(63):
        half = 1 << bit
        if half >= n:
            break
        cycle = half << 1
        full = n // cycle
        rem = n % cycle
        total += full * half
        if rem > half:
            total += rem - half
    return total

def overlap_height(x, curve_y):
    dx = x - 0.25
    inside = 0.0625 - dx * dx
    if inside <= 0.0:
        return 0.0
    
    dy = math.sqrt(inside)
    circle_low = 0.5 - dy
    circle_high = 0.5 + dy
    lo = max(0.0, circle_low)
    hi = min(circle_high, curve_y)
    return hi - lo if hi > lo else 0.0

def integrate_chunk(args):
    level, begin, end = args
    if begin >= end:
        return 0.0, 0.0
        
    inv_denom = 1.0 / (1 << level)
    numer = level * begin - 2 * prefix_popcount(begin)
    
    odd_sum = 0.0
    even_sum = 0.0
    
    for i in range(begin, end):
        x = i * inv_denom
        curve_y = numer * inv_denom
        fx = overlap_height(x, curve_y)
        
        if i & 1:
            odd_sum += fx
        else:
            even_sum += fx
            
        numer += level - 2 * i.bit_count()
        
    return odd_sum, even_sum

def simpson_level(level, threads):
    denom = 1 << level
    steps = denom >> 1
    if steps < 2: return 0.0
    
    interior = steps - 1
    if interior == 0: return 0.0
    
    threads = min(threads, interior)
    chunk = (interior + threads - 1) // threads
    
    tasks = []
    for t in range(threads):
        begin = 1 + t * chunk
        end = min(steps, begin + chunk)
        if begin < end:
            tasks.append((level, begin, end))
            
    odd_sum = 0.0
    even_sum = 0.0
    
    if threads > 1 and len(tasks) > 1:
        with multiprocessing.Pool(threads) as pool:
            results = pool.map(integrate_chunk, tasks)
            for os, es in results:
                odd_sum += os
                even_sum += es
    else:
        for t in tasks:
            os, es = integrate_chunk(t)
            odd_sum += os
            even_sum += es
            
    h = 1.0 / denom
    f0 = 0.0
    fn = overlap_height(0.5, 0.5)
    return h * (f0 + fn + 4.0 * odd_sum + 2.0 * even_sum) / 3.0

def solve(eps=2e-9, min_level=22, max_level=28):
    threads = multiprocessing.cpu_count() or 1
    
    previous = simpson_level(min_level, threads)
    for level in range(min_level + 1, max_level + 1):
        current = simpson_level(level, threads)
        if abs(current - previous) < eps:
            return f"{current:.8f}"
        previous = current
    return f"{previous:.8f}"

if __name__ == '__main__':
    print(solve())
