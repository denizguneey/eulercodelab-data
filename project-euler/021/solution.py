import sys

def proper_divisor_sum_via_factorization(n):
    if n <= 1:
        return 0
    
    remaining = n
    sigma = 1
    
    # Handle factor of 2
    exponent = 0
    while (remaining & 1) == 0:
        remaining >>= 1
        exponent += 1
    
    if exponent > 0:
        term = 1
        pow_val = 1
        for _ in range(exponent):
            pow_val <<= 1
            term += pow_val
        sigma *= term
    
    # Handle odd factors
    p = 3
    while p * p <= remaining:
        exponent = 0
        while remaining % p == 0:
            remaining //= p
            exponent += 1
        
        if exponent > 0:
            term = 1
            pow_val = 1
            for _ in range(exponent):
                pow_val *= p
                term += pow_val
            sigma *= term
        
        p += 2
    
    if remaining > 1:
        sigma *= (1 + remaining)
    
    return sigma - n

def proper_divisor_sums_up_to(limit):
    sums = [0] * limit
    for d in range(1, (limit - 1) // 2 + 1):
        for m in range(d * 2, limit, d):
            sums[m] += d
    return sums

def solve(limit):
    sums = proper_divisor_sums_up_to(limit)
    
    total = 0
    for a in range(2, limit):
        b = sums[a]
        if b == a or b <= 0:
            continue
        
        if b < limit:
            back_sum = sums[b]
        else:
            back_sum = proper_divisor_sum_via_factorization(b)
        
        if back_sum == a:
            total += a
    
    return total

def run_checkpoints():
    if proper_divisor_sum_via_factorization(220) != 284 or \
       proper_divisor_sum_via_factorization(284) != 220:
        print("Checkpoint failed for amicable pair (220, 284)", file=sys.stderr)
        return False
    
    if solve(300) != 504:
        print("Checkpoint failed for limit=300", file=sys.stderr)
        return False
    
    return True

def parse_arguments(args):
    options = {
        'limit': 10000,
        'run_checkpoints': True
    }
    
    i = 1
    while i < len(args):
        arg = args[i]
        if arg == '--skip-checkpoints':
            options['run_checkpoints'] = False
            i += 1
            continue
        
        if arg.startswith('--limit='):
            try:
                value_str = arg[8:]
                value = int(value_str)
                if value < 2:
                    return None
                options['limit'] = value
            except ValueError:
                print(f"Unknown argument: {arg}", file=sys.stderr)
                return None
        else:
            print(f"Unknown argument: {arg}", file=sys.stderr)
            return None
        
        i += 1
    
    if options['limit'] < 2:
        print("Limit must be at least 2", file=sys.stderr)
        return None
    
    return options

def main():
    args = sys.argv[1:]
    
    if not args:
        # Default case
        options = {'limit': 10000, 'run_checkpoints': True}
    else:
        options = parse_arguments(args)
        if options is None:
            sys.exit(1)
    
    if options['run_checkpoints'] and not run_checkpoints():
        sys.exit(2)
    
    print(solve(options['limit']))

if __name__ == '__main__':
    main()
