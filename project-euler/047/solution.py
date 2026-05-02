import sys

def distinct_prime_factor_count(n):
    count = 0
    
    if n % 2 == 0:
        count += 1
        while n % 2 == 0:
            n //= 2
    
    p = 3
    while p * p <= n:
        if n % p == 0:
            count += 1
            while n % p == 0:
                n //= p
        p += 2
    
    if n > 1:
        count += 1
    
    return count

def solve(consecutive, factors):
    run = 0
    run_start = 2
    
    n = 2
    while True:
        if distinct_prime_factor_count(n) == factors:
            if run == 0:
                run_start = n
            run += 1
            if run == consecutive:
                return run_start
        else:
            run = 0
        n += 1

def parse_int_after_prefix(arg, prefix):
    if not arg.startswith(prefix):
        return False, 0
    tail = arg[len(prefix):]
    if not tail:
        return False, 0
    
    try:
        parsed = int(tail)
        return True, parsed
    except ValueError:
        return False, 0

def parse_arguments(args):
    options = {
        'consecutive': 4,
        'factors': 4,
        'run_checkpoints': True
    }
    
    i = 1
    while i < len(args):
        arg = args[i]
        if arg == '--skip-checkpoints':
            options['run_checkpoints'] = False
            i += 1
            continue
        
        found, value = parse_int_after_prefix(arg, '--consecutive=')
        if found:
            options['consecutive'] = value
            i += 1
            continue
        
        found, value = parse_int_after_prefix(arg, '--factors=')
        if found:
            options['factors'] = value
            i += 1
            continue
        
        print(f"Unknown argument: {arg}", file=sys.stderr)
        return None
    
    if options['consecutive'] < 1 or options['factors'] < 1:
        return None
    
    return options

def run_checkpoints():
    if distinct_prime_factor_count(14) != 2:
        print("Checkpoint failed for factor count of 14", file=sys.stderr)
        return False
    if solve(2, 2) != 14:
        print("Checkpoint failed for consecutive=2 factors=2", file=sys.stderr)
        return False
    return True

def main():
    args = sys.argv
    
    options = parse_arguments(args)
    if options is None:
        sys.exit(1)
    
    if options['run_checkpoints'] and not run_checkpoints():
        sys.exit(2)
    
    result = solve(options['consecutive'], options['factors'])
    print(result)

if __name__ == "__main__":
    main()
