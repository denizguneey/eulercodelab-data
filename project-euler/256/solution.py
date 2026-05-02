import math
import multiprocessing

def is_tatami_tileable(a, b):
    if a > b:
        a, b = b, a
    if (a * b) % 2 != 0:
        return False
        
    groups = (b + a // 2) // a
    dist = abs(a * groups - b)
    return not (dist > groups + 1)

def build_primes_simple(n):
    if n < 2: return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(math.isqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
                
    return [i for i, p in enumerate(is_prime) if p]

def count_tatami_free_rooms(s, primes):
    factors = []
    x = s
    for p in primes:
        if p * p > x: break
        if x % p != 0: continue
        e = 0
        while x % p == 0:
            x //= p
            e += 1
        factors.append((p, e))
    if x > 1:
        factors.append((x, 1))
        
    root = math.isqrt(s)
    count = [0]
    
    def dfs(idx, current):
        if idx == len(factors):
            if current <= root:
                a = current
                b = s // a
                if not is_tatami_tileable(a, b):
                    count[0] += 1
            return
            
        p, e = factors[idx]
        val = current
        for i in range(e + 1):
            if val > root: break
            dfs(idx + 1, val)
            val *= p
            
    dfs(0, 1)
    return count[0]

def worker(args):
    start, end, step, target, primes = args
    for s in range(start, end, step):
        if s % 2 != 0: continue
        if count_tatami_free_rooms(s, primes) == target:
            return s
    return float('inf')

def solve(target=200):
    step = 55440
    start = max(step, ((2000000 + step - 1) // step) * step)
    fast_cap = 2000000000
    
    primes = build_primes_simple(math.isqrt(fast_cap) + 1)
    
    threads = max(1, multiprocessing.cpu_count())
    total_steps = (fast_cap - start) // step + 1
    chunk = (total_steps + threads - 1) // threads
    
    tasks = []
    for t in range(threads):
        c_start = start + t * chunk * step
        c_end = min(fast_cap + 1, start + (t + 1) * chunk * step)
        if c_start < c_end:
            tasks.append((c_start, c_end, step, target, primes))
            
    best = float('inf')
    if threads > 1 and len(tasks) > 1:
        with multiprocessing.Pool(threads) as pool:
            for s in pool.imap_unordered(worker, tasks):
                if s < best:
                    best = s
    else:
        for t in tasks:
            s = worker(t)
            if s < best:
                best = s
                
    if best != float('inf'):
        return str(best)
    return "-1"

if __name__ == '__main__':
    print(solve())
