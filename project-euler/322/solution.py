import math
from multiprocessing import Pool, cpu_count

def to_base_digits(x, base):
    if x == 0:
        return [0]
    digits = []
    while x > 0:
        digits.append(x % base)
        x //= base
    return digits

def count_no_carry_prime(n, limit, p):
    if limit == 0:
        return 0
    max_value = limit - 1
    n_digits = to_base_digits(n, p)
    x_digits = to_base_digits(max_value, p)
    
    length = max(len(n_digits), len(x_digits))
    n_digits += [0] * (length - len(n_digits))
    x_digits += [0] * (length - len(x_digits))
    
    tight = 1
    loose = 0
    
    for pos in range(length - 1, -1, -1):
        allowed_max = p - 1 - n_digits[pos]
        bound_digit = x_digits[pos]
        
        next_tight = 0
        next_loose = 0
        
        if allowed_max >= 0:
            next_loose += loose * (allowed_max + 1)
            for d in range(min(allowed_max, bound_digit) + 1):
                if d < bound_digit:
                    next_loose += tight
                else:
                    next_tight += tight
                    
        tight = next_tight
        loose = next_loose
        
    return tight + loose

def generate_low_values_rec(allowed_digits, pos, split, current, place_value, out):
    if pos == split:
        out.append(current)
        return
    for d in range(allowed_digits[pos] + 1):
        generate_low_values_rec(allowed_digits, pos + 1, split, current + d * place_value, place_value * 5, out)

def generate_low_values(allowed_digits, split):
    out = []
    generate_low_values_rec(allowed_digits, 0, split, 0, 1, out)
    return out

def generate_high_values(allowed_digits, split, high_bound):
    bound_digits = to_base_digits(high_bound, 5)
    length = len(bound_digits)
    
    high_allowed = [4] * length
    for i in range(length):
        original_pos = i + split
        if original_pos < len(allowed_digits):
            high_allowed[i] = allowed_digits[original_pos]
            
    pow5 = [1] * (length + 1)
    for i in range(1, length + 1):
        pow5[i] = pow5[i - 1] * 5
        
    stack = [(0, True, 0)]
    out = []
    
    while stack:
        pos, tight, value = stack.pop()
        
        if pos == length:
            out.append(value)
            continue
            
        digit_index = length - 1 - pos
        limit_digit = bound_digits[digit_index] if tight else 4
        allowed_digit = high_allowed[digit_index]
        max_digit = min(limit_digit, allowed_digit)
        
        for d in range(max_digit, -1, -1):
            next_tight = tight and (d == limit_digit)
            next_value = value + d * pow5[digit_index]
            stack.append((pos + 1, next_tight, next_value))
            
    return out

def worker(args):
    lows, scaled_highs, n = args
    local = 0
    for low in lows:
        for scaled in scaled_highs:
            x = low + scaled
            if (x & n) == 0:
                local += 1
    return local

def count_overlap_coprime_10(n, limit):
    if limit == 0:
        return 0
    max_value = limit - 1
    n_digits = to_base_digits(n, 5)
    x_digits = to_base_digits(max_value, 5)
    
    length = max(len(n_digits), len(x_digits))
    n_digits += [0] * (length - len(n_digits))
    x_digits += [0] * (length - len(x_digits))
    
    allowed_digits = [4 - d for d in n_digits]
    
    split = 0
    while split < length and x_digits[split] == allowed_digits[split]:
        split += 1
        
    step = 5 ** split
    high_bound = max_value // step
    
    low_values = generate_low_values(allowed_digits, split)
    high_values = generate_high_values(allowed_digits, split, high_bound)
    
    scaled_high_values = [h * step for h in high_values]
    
    threads = cpu_count()
    chunk_size = max(1, len(low_values) // threads)
    chunks = []
    for i in range(0, len(low_values), chunk_size):
        chunks.append((low_values[i:i + chunk_size], scaled_high_values, n))
        
    with Pool(threads) as pool:
        results = pool.map(worker, chunks)
        
    return sum(results)

def solve_T(m, n):
    interval = m - n
    not_div_2 = count_no_carry_prime(n, interval, 2)
    not_div_5 = count_no_carry_prime(n, interval, 5)
    coprime_10 = count_overlap_coprime_10(n, interval)
    
    return interval - not_div_2 - not_div_5 + coprime_10

def solve():
    m = 1000000000000000000
    n = 1000000000000 - 10
    return str(solve_T(m, n))

if __name__ == '__main__':
    print(solve())
