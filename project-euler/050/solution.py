import sys

def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False
    
    p = 2
    while p * p <= limit:
        if is_prime[p]:
            for q in range(p * p, limit + 1, p):
                is_prime[q] = False
        p += 1
    
    return is_prime

def solve(limit):
    is_prime = sieve(limit - 1)
    
    primes = [n for n in range(2, limit) if is_prime[n]]
    
    prefix = [0] * (len(primes) + 1)
    for i in range(len(primes)):
        prefix[i + 1] = prefix[i] + primes[i]
    
    best_prime = 0
    best_len = 0
    
    for i in range(len(primes)):
        j = i + best_len + 1
        while j <= len(primes):
            sum_val = prefix[j] - prefix[i]
            if sum_val >= limit:
                break
            if sum_val < len(is_prime) and is_prime[sum_val]:
                best_len = j - i
                best_prime = sum_val
            j += 1
    
    return best_prime

def run_checkpoints():
    if solve(100) != 41:
        sys.stderr.write("Checkpoint failed for limit=100\n")
        return False
    if solve(1000) != 953:
        sys.stderr.write("Checkpoint failed for limit=1000\n")
        return False
    return True

def parse_arguments(args):
    options = {
        'limit': 1000000,
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
                value = int(arg[8:])
                options['limit'] = value
                i += 1
            except ValueError:
                sys.stderr.write(f"Unknown argument: {arg}\n")
                return None
        else:
            sys.stderr.write(f"Unknown argument: {arg}\n")
            return None
    
    if options['limit'] < 3:
        sys.stderr.write("Limit must be at least 3\n")
        return None
    
    return options

def main():
    args = sys.argv[1:]
    
    options = parse_arguments(args)
    if options is None:
        return 1
    
    if options['run_checkpoints'] and not run_checkpoints():
        return 2
    
    result = solve(options['limit'])
    print(result)

if __name__ == '__main__':
    main()
