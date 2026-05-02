import math
import multiprocessing

def isqrt(n):
    r = int(math.isqrt(n))
    while (r + 1) * (r + 1) <= n:
        r += 1
    while r > 0 and r * r > n:
        r -= 1
    return r

def worker_func(l, r):
    kMod = 999999937
    partial_sum = 0
    
    m = isqrt(l)
    if m * m < l:
        m += 1
    sq = m * m
    
    for a in range(l, r + 1):
        while sq < a:
            m += 1
            sq = m * m
            
        is_square = (sq == a)
        n = a * a
        a_mod = a % kMod
        
        base_x = m % kMod
        base_y = 1
        res_x = 1
        res_y = 0
        
        while n > 0:
            if n & 1:
                nx = (res_x * base_x + res_y * base_y * a_mod) % kMod
                ny = (res_x * base_y + res_y * base_x) % kMod
                res_x, res_y = nx, ny
            n >>= 1
            if n > 0:
                nx = (base_x * base_x + base_y * base_y * a_mod) % kMod
                ny = (2 * base_x * base_y) % kMod
                base_x, base_y = nx, ny
                
        val = (2 * res_x) % kMod
        if not is_square:
            val = (val + kMod - 1) % kMod
            
        partial_sum = (partial_sum + val) % kMod
        
    return partial_sum

def solve():
    kMod = 999999937
    limit = 5000000
    
    threads = max(1, multiprocessing.cpu_count())
    chunk = limit // threads
    rem = limit % threads
    
    ranges = []
    curr = 1
    for t in range(threads):
        length = chunk + (1 if t < rem else 0)
        if length > 0:
            ranges.append((curr, curr + length - 1))
        curr += length
        
    if threads <= 1:
        total = worker_func(1, limit)
    else:
        with multiprocessing.Pool(threads) as pool:
            results = pool.starmap(worker_func, ranges)
            total = sum(results) % kMod
            
    return str(total)

if __name__ == "__main__":
    print(solve())
