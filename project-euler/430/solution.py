import sys
import math
from multiprocessing import Pool, cpu_count

def r_value(n, i):
    nf = float(n)
    n2 = nf * nf
    a = float(i - 1)
    b = float(n - i)
    return (2.0 * (a * a + b * b) - n2) / n2

def expected_exact(n, m):
    ans = 0.0
    for i in range(1, n + 1):
        r = r_value(n, i)
        ans += 0.5 * (1.0 + math.pow(r, m))
    return ans

def edge_limit_by_rho(n, rho):
    lo = 0
    hi = n // 2
    while lo < hi:
        mid = lo + (hi - lo + 1) // 2
        if r_value(n, mid) > rho:
            lo = mid
        else:
            hi = mid - 1
    return lo

def edge_sum_chunk(n, m, begin, end):
    local = 0.0
    for i in range(begin, end + 1):
        r = r_value(n, i)
        local += math.pow(r, m)
    return local

def edge_sum_parallel(n, m, edge_count, num_threads):
    if edge_count == 0:
        return 0.0
    
    threads = min(num_threads, edge_count)
    if threads < 1: threads = 1
    
    tasks = []
    for t in range(threads):
        begin = edge_count * t // threads + 1
        end = edge_count * (t + 1) // threads
        tasks.append((n, m, begin, end))
        
    with Pool(threads) as pool:
        results = pool.starmap(edge_sum_chunk, tasks)
        
    return sum(results)

def expected_fast(n, m, threads=0):
    if m == 0:
        return float(n)
    if n <= 2000000:
        return expected_exact(n, m)
        
    if threads <= 0:
        threads = cpu_count()
        if threads <= 0: threads = 4
        
    eps = 1e-4
    rho = math.exp(math.log((2.0 * eps) / float(n)) / float(m))
    
    l = edge_limit_by_rho(n, rho)
    edge = edge_sum_parallel(n, m, l, threads)
    
    estimate = float(n) * 0.5 + edge
    
    omitted = n - 2 * l
    err_bound = 0.5 * float(omitted) * math.pow(rho, m)
    if err_bound >= 0.005:
        rho2 = rho * 0.99
        l2 = edge_limit_by_rho(n, rho2)
        edge2 = edge_sum_parallel(n, m, l2, threads)
        estimate = float(n) * 0.5 + edge2
        
    return estimate

def solve():
    n = 10000000000
    m = 4000
    ans = expected_fast(n, m)
    return f"{ans:.2f}"

if __name__ == '__main__':
    print(solve())
