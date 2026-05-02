import sys

def parse_int_after_prefix(arg, prefix):
    if not arg.startswith(prefix):
        return False, 0
    tail = arg[len(prefix):]
    if not tail:
        return False, 0
    
    try:
        value = int(tail)
        return True, value
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
        if arg == "--skip-checkpoints":
            options['run_checkpoints'] = False
            i += 1
            continue
            
        success, value = parse_int_after_prefix(arg, "--limit=")
        if success:
            options['limit'] = value
            i += 1
            continue
        
        print(f"Unknown argument: {arg}", file=sys.stderr)
        return None
    
    if options['limit'] <= 2:
        return None
    return options

def recurring_cycle_length(denominator):
    first_seen = [-1] * denominator
    
    remainder = 1 % denominator
    position = 0
    
    while remainder != 0 and first_seen[remainder] == -1:
        first_seen[remainder] = position
        remainder = (remainder * 10) % denominator
        position += 1
    
    if remainder == 0:
        return 0
    return position - first_seen[remainder]

def solve(limit):
    best_d = 2
    best_len = 0
    
    for d in range(2, limit):
        cycle = recurring_cycle_length(d)
        if cycle > best_len:
            best_len = cycle
            best_d = d
    
    return best_d

def run_checkpoints():
    if recurring_cycle_length(7) != 6:
        print("Checkpoint failed for denominator=7", file=sys.stderr)
        return False
    if solve(10) != 7:
        print("Checkpoint failed for limit=10", file=sys.stderr)
        return False
    return True

def main():
    args = sys.argv
    
    options = parse_arguments(args)
    if options is None:
        sys.exit(1)
    
    if options['run_checkpoints'] and not run_checkpoints():
        sys.exit(2)
    
    print(solve(options['limit']))

if __name__ == "__main__":
    main()
