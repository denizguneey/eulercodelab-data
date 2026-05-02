import math
import multiprocessing

def count_case_k2_a(args):
    y_start, y_end, perimeter_limit = args
    count = 0
    for y in range(y_start, y_end):
        x_max = math.isqrt(2 * y * y)
        for x in range(y + 1, x_max + 1):
            if x % 2 == 0 or math.gcd(x, y) != 1:
                continue
            base = (x + y) * (x + 2 * y)
            if base > perimeter_limit:
                continue
            count += perimeter_limit // base
    return count

def count_case_k2_b(args):
    x_start, x_end, perimeter_limit = args
    count = 0
    for x in range(x_start, x_end):
        r = math.isqrt(2 * x * x)
        y_min = r if r * r == 2 * x * x else r + 1
        y_max = 2 * x - 1
        for y in range(y_min, y_max + 1):
            if y % 2 == 0 or math.gcd(x, y) != 1:
                continue
            base = (x + y) * (2 * x + y)
            if base > perimeter_limit:
                continue
            count += perimeter_limit // base
    return count

def count_case_k3_a(args):
    y_start, y_end, perimeter_limit = args
    count = 0
    for y in range(y_start, y_end):
        x_max = math.isqrt(3 * y * y)
        for x in range(y + 1, x_max + 1):
            if x % 3 == 0 or math.gcd(x, y) != 1:
                continue
            base_num = (x + y) * (x + 3 * y)
            if base_num > 2 * perimeter_limit:
                continue
                
            g_max = (2 * perimeter_limit) // base_num
            odd_g_valid = ((x * (x + y)) % 2 == 0) and ((y * (x + 3 * y)) % 2 == 0)
            count += g_max if odd_g_valid else (g_max // 2)
    return count

def count_case_k3_b(args):
    x_start, x_end, perimeter_limit = args
    count = 0
    for x in range(x_start, x_end):
        r = math.isqrt(3 * x * x)
        y_min = r if r * r == 3 * x * x else r + 1
        y_max = 3 * x - 1
        for y in range(y_min, y_max + 1):
            if y % 3 == 0 or math.gcd(x, y) != 1:
                continue
            base_num = (x + y) * (3 * x + y)
            if base_num > 2 * perimeter_limit:
                continue
                
            g_max = (2 * perimeter_limit) // base_num
            odd_g_valid = ((x * (y + 3 * x)) % 2 == 0) and ((y * (x + y)) % 2 == 0)
            count += g_max if odd_g_valid else (g_max // 2)
    return count

def solve(perimeter_limit=100000000):
    max_var = math.isqrt(perimeter_limit) + 2
    count = perimeter_limit // 3
    
    threads = max(1, multiprocessing.cpu_count())
    
    y_chunk = (max_var + threads - 1) // threads
    tasks_k2_a = [(1 + t * y_chunk, min(max_var + 1, 1 + (t + 1) * y_chunk), perimeter_limit) for t in range(threads)]
    tasks_k2_b = [(1 + t * y_chunk, min(max_var + 1, 1 + (t + 1) * y_chunk), perimeter_limit) for t in range(threads)]
    tasks_k3_a = [(1 + t * y_chunk, min(max_var + 1, 1 + (t + 1) * y_chunk), perimeter_limit) for t in range(threads)]
    tasks_k3_b = [(1 + t * y_chunk, min(max_var + 1, 1 + (t + 1) * y_chunk), perimeter_limit) for t in range(threads)]
    
    if threads > 1:
        with multiprocessing.Pool(threads) as pool:
            count += sum(pool.map(count_case_k2_a, [t for t in tasks_k2_a if t[0] < t[1]]))
            count += sum(pool.map(count_case_k2_b, [t for t in tasks_k2_b if t[0] < t[1]]))
            count += sum(pool.map(count_case_k3_a, [t for t in tasks_k3_a if t[0] < t[1]]))
            count += sum(pool.map(count_case_k3_b, [t for t in tasks_k3_b if t[0] < t[1]]))
    else:
        count += sum(count_case_k2_a(t) for t in tasks_k2_a if t[0] < t[1])
        count += sum(count_case_k2_b(t) for t in tasks_k2_b if t[0] < t[1])
        count += sum(count_case_k3_a(t) for t in tasks_k3_a if t[0] < t[1])
        count += sum(count_case_k3_b(t) for t in tasks_k3_b if t[0] < t[1])
        
    return str(count)

if __name__ == '__main__':
    print(solve())
