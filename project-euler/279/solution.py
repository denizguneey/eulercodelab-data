import math
import multiprocessing

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def gcd3(a, b, c):
    return gcd(a, gcd(b, c))

def count_90_range(limit, m_start, m_end, m_step):
    out = 0
    for m in range(m_start, m_end + 1, m_step):
        for n in range(1, m):
            if ((m - n) & 1) == 0 or gcd(m, n) != 1:
                continue
            primitive_perimeter = 2 * m * (m + n)
            out += limit // primitive_perimeter
    return out

def count_120_range(limit, m_start, m_end, m_step):
    out = 0
    for m in range(m_start, m_end + 1, m_step):
        for n in range(1, m):
            if gcd(m, n) != 1:
                continue
            mm = m * m
            nn = n * n
            a = mm - nn
            b = 2 * m * n + nn
            c = mm + m * n + nn
            if gcd3(a, b, c) != 1:
                continue
            primitive_perimeter = a + b + c
            out += limit // primitive_perimeter
    return out

def count_60_non_eq_range(limit, m_start, m_end, m_step):
    out = 0
    for m in range(m_start, m_end + 1, m_step):
        mm = m * m
        n_max = (m - 1) // 2
        for n in range(1, n_max + 1):
            if gcd(m, n) != 1:
                continue
            nn = n * n
            a = mm - nn
            c = mm - m * n + nn

            b_a = 2 * m * n - nn
            if gcd3(a, b_a, c) == 1:
                primitive_perimeter = a + b_a + c
                out += limit // primitive_perimeter

            b_b = mm - 2 * m * n
            if b_b > 0 and gcd3(a, b_b, c) == 1:
                primitive_perimeter = a + b_b + c
                out += limit // primitive_perimeter
    return out

def max_m_90(limit):
    m = 2
    while 2 * m * (m + 1) <= limit:
        m += 1
    return m - 1

def max_m_120(limit):
    m = 2
    while 2 * m * m + 3 * m + 1 <= limit:
        m += 1
    return m - 1

def max_m_60(limit):
    m = 2
    while True:
        mm = m * m
        min_perimeter_a = 2 * mm + m - 1
        min_perimeter_b = 3 * m * ((m + 1) // 2)
        if min_perimeter_a > limit and min_perimeter_b > limit:
            break
        m += 1
    return m - 1

def worker_main(args):
    limit, m_max_90, m_max_120, m_max_60, m_start, m_step = args
    c90 = count_90_range(limit, m_start, m_max_90, m_step)
    c120 = count_120_range(limit, m_start, m_max_120, m_step)
    c60 = count_60_non_eq_range(limit, m_start, m_max_60, m_step)
    return c90, c120, c60

def solve(limit=100000000):
    m_max_90 = max_m_90(limit)
    m_max_120 = max_m_120(limit)
    m_max_60 = max_m_60(limit)
    
    total_60 = limit // 3
    total_90 = 0
    total_120 = 0
    
    threads = max(1, multiprocessing.cpu_count())
    
    if threads <= 1:
        total_90 += count_90_range(limit, 2, m_max_90, 1)
        total_120 += count_120_range(limit, 2, m_max_120, 1)
        total_60 += count_60_non_eq_range(limit, 2, m_max_60, 1)
    else:
        args = []
        for t in range(threads):
            args.append((limit, m_max_90, m_max_120, m_max_60, 2 + t, threads))
            
        with multiprocessing.Pool(threads) as pool:
            results = pool.map(worker_main, args)
            
        for c90, c120, c60 in results:
            total_90 += c90
            total_120 += c120
            total_60 += c60
            
    return str(total_60 + total_90 + total_120)

if __name__ == '__main__':
    print(solve())
