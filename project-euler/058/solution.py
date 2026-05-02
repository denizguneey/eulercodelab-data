import sys

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

def solve(threshold_percent):
    prime_count = 0
    diagonal_count = 1
    
    layer = 1
    while True:
        side = 2 * layer + 1
        square = side * side
        step = side - 1
        
        if is_prime(square - step):
            prime_count += 1
        if is_prime(square - 2 * step):
            prime_count += 1
        if is_prime(square - 3 * step):
            prime_count += 1
        
        diagonal_count += 4
        
        if prime_count * 100 < diagonal_count * threshold_percent:
            return side
        
        layer += 1

def parse_arguments(args):
    options = {
        'threshold_percent': 10,
        'run_checkpoints': True
    }
    
    i = 1
    while i < len(args):
        arg = args[i]
        if arg == '--skip-checkpoints':
            options['run_checkpoints'] = False
            i += 1
            continue
        
        if arg.startswith('--threshold-percent='):
            try:
                value_str = arg[len('--threshold-percent='):]
                if not value_str:
                    return None, "Invalid threshold percent argument"
                value = int(value_str)
                if not (1 <= value <= 100):
                    return None, "Threshold percent must be between 1 and 100"
                options['threshold_percent'] = value
                i += 1
                continue
            except ValueError:
                return None, "Invalid threshold percent value"
        
        return None, f"Unknown argument: {arg}"
    
    return options, None

def run_checkpoints():
    if solve(62) != 3:
        return False
    if solve(60) != 5:
        return False
    return True

def main():
    args = sys.argv[1:]
    
    options, error = parse_arguments(args)
    if error:
        print(error, file=sys.stderr)
        sys.exit(1)
    
    if options['run_checkpoints'] and not run_checkpoints():
        print("Checkpoint failed", file=sys.stderr)
        sys.exit(2)
    
    result = solve(options['threshold_percent'])
    print(result)

if __name__ == "__main__":
    main()
