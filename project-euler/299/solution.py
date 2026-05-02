import math
from concurrent.futures import ProcessPoolExecutor
import multiprocessing

def count_x_eq_y_worker(lo, hi, limit, numerator):
    local = 0
    for m in range(lo, hi):
        m2 = m * m
        if m % 2 != 0:
            n = 1
            while True:
                s = m2 + 4 * m * n + 2 * n * n
                if s >= limit: break
                if math.gcd(m, n) == 1:
                    local += numerator // s
                n += 1
                
        n = 1
        while True:
            s = 2 * m2 + 4 * m * n + n * n
            if s >= limit: break
            if n % 2 != 0 and math.gcd(m, n) == 1:
                local += numerator // s
            n += 1
            
    return local

def count_family_x_eq_y(limit, threads):
    if limit <= 7: return 0
    numerator = limit - 1
    m_max = math.isqrt(limit) + 3
    
    if threads <= 1:
        return count_x_eq_y_worker(1, m_max + 1, limit, numerator)
        
    chunk = (m_max + threads) // threads
    ranges = [(max(1, i * chunk), min(m_max + 1, (i + 1) * chunk)) for i in range(threads)]
    
    total = 0
    with ProcessPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(count_x_eq_y_worker, r[0], r[1], limit, numerator) for r in ranges]
        for f in futures:
            total += f.result()
            
    return total

def count_u_eq_v_worker(lo, hi, limit, numerator):
    local = 0
    for idx in range(lo, hi):
        p = 2 * idx + 1
        p2 = p * p
        q = 1
        while True:
            s = p2 + 2 * p * q + 2 * q * q
            denom = 2 * s
            if denom >= limit: break
            if math.gcd(p, q) == 1:
                local += numerator // denom
            q += 1
            
    return local

def count_family_u_eq_v(limit, threads):
    if limit <= 13: return 0
    numerator = limit - 1
    p_max = math.isqrt(limit // 2) + 3
    odd_count = (p_max + 1) // 2
    
    if threads <= 1:
        return count_u_eq_v_worker(0, odd_count, limit, numerator)
        
    chunk = (odd_count + threads - 1) // threads
    ranges = [(i * chunk, min(odd_count, (i + 1) * chunk)) for i in range(threads)]
    
    total = 0
    with ProcessPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(count_u_eq_v_worker, r[0], r[1], limit, numerator) for r in ranges]
        for f in futures:
            total += f.result()
            
    return total

def count_triplets(limit):
    threads = multiprocessing.cpu_count()
    if threads == 0: threads = 1
    
    if limit < 1000000:
        threads = 1
        
    total_x = count_family_x_eq_y(limit, threads)
    total_u = count_family_u_eq_v(limit, threads)
    return total_x + total_u

def solve(limit=100000000):
    return str(count_triplets(limit))

if __name__ == '__main__':
    print(solve())
