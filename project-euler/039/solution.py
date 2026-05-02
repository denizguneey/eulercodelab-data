import math
import sys

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
        'limit': 1000,
        'run_checkpoints': True
    }
    
    i = 1
    while i < len(args):
        arg = args[i]
        if arg == '--skip-checkpoints':
            options['run_checkpoints'] = False
            i += 1
            continue
        
        success, value = parse_int_after_prefix(arg, '--limit=')
        if success:
            options['limit'] = value
            i += 1
            continue
        
        print(f"Unknown argument: {arg}", file=sys.stderr)
        return None
    
    if options['limit'] < 12:
        return None
    return options

def solve(limit):
    solutions = [0] * (limit + 1)
    
    for a in range(1, limit // 3 + 1):
        for b in range(a, (limit - a) // 2 + 1):
            c2 = a * a + b * b
            c = int(math.isqrt(c2))
            if c * c != c2:
                continue
            p = a + b + c
            if p <= limit:
                solutions[p] += 1
    
    best_p = 0
    best_count = -1
    for p in range(limit + 1):
        if solutions[p] > best_count:
            best_count = solutions[p]
            best_p = p
    
    return best_p

def run_checkpoints():
    if solve(120) != 120:
        print("Checkpoint failed for limit=120", file=sys.stderr)
        return False
    return True

def main():
    args = sys.argv[1:]
    
    options = parse_arguments(args)
    if options is None:
        sys.exit(1)
    
    if options['run_checkpoints'] and not run_checkpoints():
        sys.exit(2)
    
    print(solve(options['limit']))

if __name__ == '__main__':
    main()
