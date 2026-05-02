import sys
import math
from typing import List, Tuple

def mul_mod(a: int, b: int, mod: int) -> int:
    return (a * b) % mod

def pow_mod(base: int, exp: int, mod: int) -> int:
    base %= mod
    result = 1 % mod
    while exp > 0:
        if (exp & 1) != 0:
            result = mul_mod(result, base, mod)
        base = mul_mod(base, base, mod)
        exp >>= 1
    return result

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for p in small_primes:
        if n == p:
            return True
        if n % p == 0:
            return False
    
    d = n - 1
    s = 0
    while (d & 1) == 0:
        d >>= 1
        s += 1
    
    bases = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
    
    for a in bases:
        if a % n == 0:
            continue
        x = pow_mod(a, d, n)
        if x == 1 or x == n - 1:
            continue
        witness = True
        for r in range(1, s):
            x = mul_mod(x, x, n)
            if x == n - 1:
                witness = False
                break
        if witness:
            return False
    return True

def sieve_primes(n: int) -> List[int]:
    if n < 2:
        return []
    is_prime_arr = [True] * (n + 1)
    is_prime_arr[0] = False
    if n >= 1:
        is_prime_arr[1] = False
    
    for p in range(2, int(math.isqrt(n)) + 1):
        if not is_prime_arr[p]:
            continue
        for q in range(p * p, n + 1, p):
            is_prime_arr[q] = False
    
    return [i for i in range(2, n + 1) if is_prime_arr[i]]

def build_filters(limit: int):
    kGood = [1, 3, 7, 9, 13, 27]
    primes = sieve_primes(limit)
    filters = []
    
    for p in primes:
        if p == 2 or p == 5:
            continue
        
        step = 10 % p
        bad = [False] * p
        
        for r in range(p):
            r2 = (r * r) % p
            is_bad = False
            for k in kGood:
                if (r2 + (k % p)) % p == 0:
                    is_bad = True
                    break
            bad[r] = is_bad
        
        filters.append({'p': p, 'step': step, 'bad': bad})
    
    return filters

def first_with_mod(start: int, mod: int, residue: int) -> int:
    current = start % mod
    if current <= residue:
        return start + (residue - current)
    return start + (mod - (current - residue))

def run_sequence(start: int, end: int, residue: int, filters, sum_ref):
    kGood = [1, 3, 7, 9, 13, 27]
    kBad = [5, 11, 15, 17, 19, 21, 23, 25]
    
    filter_threshold = 1000
    step = 70
    
    n = first_with_mod(start, step, residue)
    if n >= end:
        return
    
    square = n * n
    
    residues = [int(n % f['p']) for f in filters]
    step70 = [(f['step'] * 7) % f['p'] for f in filters]
    
    while n < end:
        if square % 3 != 0 and square % 13 != 0:
            ok = True
            if n >= filter_threshold:
                for i, f in enumerate(filters):
                    if f['bad'][residues[i]]:
                        ok = False
                        break
            
            if ok:
                for k in kGood:
                    if not is_prime(square + k):
                        ok = False
                        break
                
                if ok:
                    for k in kBad:
                        if is_prime(square + k):
                            ok = False
                            break
                
                if ok:
                    sum_ref[0] += n
        
        n += step
        square += 140 * (n - step) + 4900
        
        for i, f in enumerate(filters):
            p = f['p']
            next_val = residues[i] + step70[i]
            if next_val >= p:
                next_val -= p
            residues[i] = next_val

def worker(t, block, limit, filters, tasks_sum_arr):
    start = 10
    count = (limit - start + 9) // 10
    idx_start = t * block
    idx_end = min(count, idx_start + block)
    n_start = start + idx_start * 10
    n_end = start + idx_end * 10
    
    sum_ref = [0]
    run_sequence(n_start, n_end, 10, filters, sum_ref)
    run_sequence(n_start, n_end, 60, filters, sum_ref)
    tasks_sum_arr[t] = sum_ref[0]

def solve(limit: int, filters, allow_multithreading: bool, requested_threads: int) -> int:
    if not allow_multithreading:
        threads = 1
    elif requested_threads > 0:
        threads = requested_threads
    else:
        try:
            import os
            threads = os.cpu_count() or 1
        except:
            threads = 1
    
    if threads <= 1:
        sum_ref = [0]
        run_sequence(10, limit, 10, filters, sum_ref)
        run_sequence(10, limit, 60, filters, sum_ref)
        return sum_ref[0]
    
    start = 10
    count = (limit - start + 9) // 10
    block = (count + threads - 1) // threads
    
    import multiprocessing
    
    tasks_sum = multiprocessing.Array('L', threads)
    processes = []
    
    
    
    for t in range(threads):
        p = multiprocessing.Process(target=worker, args=(t, block, limit, filters, tasks_sum))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
    
    return sum(tasks_sum)

def run_checkpoints() -> bool:
    if not is_prime(2) or not is_prime(3) or is_prime(1) or is_prime(21):
        return False
    
    filters = build_filters(2000)
    result = solve(1000000, filters, False, 1)
    return result == 1242490

def main():
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--skip-checkpoints', action='store_true')
    parser.add_argument('--single-thread', action='store_true')
    parser.add_argument('--limit', type=int, default=150000000)
    parser.add_argument('--threads', type=int, default=0)
    
    args = parser.parse_args()
    
    if not args.skip_checkpoints:
        if not run_checkpoints():
            sys.exit(2)
    
    filters = build_filters(2000)
    result = solve(args.limit, filters, not args.single_thread, args.threads)
    print(result)

if __name__ == '__main__':
    main()
