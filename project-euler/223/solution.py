import math
import multiprocessing

def get_spf(limit):
    spf = [0] * (limit + 1)
    primes = []
    for i in range(2, limit + 1):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
        for p in primes:
            if p * i > limit or p > spf[i]:
                break
            spf[p * i] = p
    spf[1] = 1
    return spf

def factorize_int(x, spf):
    factors = []
    while x > 1:
        p = spf[x]
        e = 0
        while x > 1 and spf[x] == p:
            x //= p
            e += 1
        factors.append((p, e))
    return factors

def merge_factors(a, b):
    out = []
    i, j = 0, 0
    while i < len(a) or j < len(b):
        if j == len(b) or (i < len(a) and a[i][0] < b[j][0]):
            out.append(a[i])
            i += 1
        elif i == len(a) or b[j][0] < a[i][0]:
            out.append(b[j])
            j += 1
        else:
            out.append((a[i][0], a[i][1] + b[j][1]))
            i += 1
            j += 1
    return out

def get_divisors(factors, v_max):
    divisors = [1]
    for p, e in factors:
        base_size = len(divisors)
        mul = 1
        for _ in range(1, e + 1):
            mul *= p
            for i in range(base_size):
                candidate = divisors[i] * mul
                if candidate <= v_max:
                    divisors.append(candidate)
    return divisors

def worker(args):
    start_a, end_a, perimeter_limit, spf = args
    local_count = 0
    
    for a in range(start_a, end_a + 1):
        n = a * a - 1
        if n == 0: continue
        
        denom = perimeter_limit - a
        if denom <= 0: continue
        
        v_min = (n + denom - 1) // denom
        
        root = math.sqrt(2.0 * a * a - 1.0)
        v_max = int(math.floor(root - a))
        if v_max <= 0: continue
        
        while (v_max + 1) * (v_max + 1) + 2 * a * (v_max + 1) <= n:
            v_max += 1
        while v_max * v_max + 2 * a * v_max > n:
            v_max -= 1
            
        if v_max < v_min: continue
        
        left_factors = factorize_int(a - 1, spf)
        right_factors = factorize_int(a + 1, spf)
        merged_factors = merge_factors(left_factors, right_factors)
        
        divisors = get_divisors(merged_factors, v_max)
        
        for v in divisors:
            if v < v_min: continue
            u = n // v
            if (u - v) % 2 != 0: continue
            if u < v + 2 * a: continue
            if a + u > perimeter_limit: continue
            local_count += 1
            
    return local_count

def solve(perimeter_limit=25000000):
    if perimeter_limit < 3: return "0"
    
    a_max = perimeter_limit // 3
    a1_count = (perimeter_limit - 1) // 2
    
    threads = multiprocessing.cpu_count() or 1
    threads = min(threads, a_max)
    
    spf = get_spf(a_max + 1)
    
    chunk = 2048
    tasks = []
    start = 2
    while start <= a_max:
        end = min(a_max, start + chunk - 1)
        tasks.append((start, end, perimeter_limit, spf))
        start += chunk
        
    total = a1_count
    
    if threads > 1 and len(tasks) > 1:
        with multiprocessing.Pool(threads) as pool:
            results = pool.map(worker, tasks)
            total += sum(results)
    else:
        for t in tasks:
            total += worker(t)
            
    return str(total)

if __name__ == '__main__':
    print(solve())
