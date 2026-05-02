import math
import multiprocessing
import itertools

def isqrt(x):
    if x == 0: return 0
    return int(math.isqrt(x))

def pow_with_limit(base, exponent, limit):
    result = 1
    for _ in range(exponent):
        if result > limit // base:
            return limit + 1
        result *= base
    return result

def sieve_primes(limit):
    if limit < 2: return []
    is_prime = bytearray([1]) * (limit + 1)
    is_prime[0] = is_prime[1] = 0
    
    for p in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[p]:
            for m in range(p * p, limit + 1, p):
                is_prime[m] = 0
                
    return [p for p in range(2, limit + 1) if is_prime[p]]

def primes_1mod4_up_to(limit):
    return [p for p in sieve_primes(limit) if p % 4 == 1]

def build_spf(max_n):
    spf = bytearray(max_n + 1)
    # Use array of integers since max_n could be up to 10^7
    spf = [0] * (max_n + 1)
    primes = []
    
    for i in range(2, max_n + 1):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
        for p in primes:
            m = p * i
            if m > max_n:
                break
            spf[m] = p
            if p == spf[i]:
                break
    return spf

def tail_fits(ordered_exponents, next_pos, next_prime_idx, remaining_limit, primes_1mod4):
    idx = next_prime_idx
    for pos in range(next_pos, len(ordered_exponents)):
        if idx >= len(primes_1mod4):
            return False
        p = primes_1mod4[idx]
        pe = pow_with_limit(p, ordered_exponents[pos], remaining_limit)
        if pe > remaining_limit:
            return False
        remaining_limit //= pe
        idx += 1
    return True

def enumerate_core_for_order(ordered_exponents, pos, start_prime_idx, current_product, limit, primes_1mod4, out):
    if pos == len(ordered_exponents):
        out.append(current_product)
        return
        
    remaining_slots = len(ordered_exponents) - pos
    if start_prime_idx + remaining_slots > len(primes_1mod4):
        return
        
    head_limit = limit // current_product
    for i in range(start_prime_idx, len(primes_1mod4) - remaining_slots + 1):
        p = primes_1mod4[i]
        pe = pow_with_limit(p, ordered_exponents[pos], head_limit)
        if pe > head_limit:
            break
            
        next_product = current_product * pe
        if pos + 1 < len(ordered_exponents):
            if not tail_fits(ordered_exponents, pos + 1, i + 1, limit // next_product, primes_1mod4):
                break
                
        enumerate_core_for_order(ordered_exponents, pos + 1, i + 1, next_product, limit, primes_1mod4, out)

def enumerate_core_numbers(limit, primes_1mod4):
    exponent_patterns = [
        [52],
        [17, 1],
        [10, 2],
        [7, 3],
        [3, 2, 1],
    ]
    
    core_numbers = []
    for pattern in exponent_patterns:
        for perm in sorted(set(itertools.permutations(pattern))):
            enumerate_core_for_order(perm, 0, 0, 1, limit, primes_1mod4, core_numbers)
            
    return sorted(list(set(core_numbers)))

def build_allowed_multiplier_prefix(max_multiplier):
    prefix = [0] * (max_multiplier + 1)
    if max_multiplier == 0:
        return prefix
        
    spf = build_spf(max_multiplier)
    valid = bytearray(max_multiplier + 1)
    valid[1] = 1
    
    for n in range(2, max_multiplier + 1):
        p = spf[n]
        m = n // p
        allowed = (p == 2) or ((p % 4) == 3)
        valid[n] = 1 if (allowed and valid[m]) else 0
        
    running = 0
    for n in range(1, max_multiplier + 1):
        if valid[n]:
            running += n
        prefix[n] = running
        
    return prefix

def accumulate_range(args):
    core_numbers, begin, end, limit, allowed_prefix = args
    local_sum = 0
    for i in range(begin, end):
        core = core_numbers[i]
        max_mult = limit // core
        local_sum += core * allowed_prefix[max_mult]
    return local_sum

def solve_sum(limit, allow_multithreading=True):
    prime_bound = max(200, limit // 21125 + 100)
    primes_1mod4 = primes_1mod4_up_to(prime_bound)
    core_numbers = enumerate_core_numbers(limit, primes_1mod4)
    
    if not core_numbers:
        return 0
        
    min_core = core_numbers[0]
    max_multiplier = limit // min_core
    allowed_prefix = build_allowed_multiplier_prefix(max_multiplier)
    
    threads = multiprocessing.cpu_count() if allow_multithreading else 1
    threads = min(threads, max(1, len(core_numbers)))
    
    if threads == 1:
        return accumulate_range((core_numbers, 0, len(core_numbers), limit, allowed_prefix))
        
    pool_args = []
    for t in range(threads):
        begin = len(core_numbers) * t // threads
        end = len(core_numbers) * (t + 1) // threads
        pool_args.append((core_numbers, begin, end, limit, allowed_prefix))
        
    with multiprocessing.Pool(threads) as pool:
        results = pool.map(accumulate_range, pool_args)
        
    return sum(results)

def solve():
    return str(solve_sum(100000000000))

if __name__ == '__main__':
    print(solve())
