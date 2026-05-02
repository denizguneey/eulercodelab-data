import sys

def solve(max_power):
    targets = []
    
    t = 1
    for p in range(max_power + 1):
        targets.append(t)
        if t > sys.maxsize // 10:
            raise OverflowError("target overflow")
        t *= 10
    
    max_target = targets[-1]
    
    product = 1
    next_target_index = 0
    global_pos = 0
    
    n = 1
    while global_pos < max_target:
        s = str(n)
        for c in s:
            global_pos += 1
            if global_pos == targets[next_target_index]:
                product *= int(c)
                next_target_index += 1
                if next_target_index >= len(targets):
                    return product
        n += 1
    
    return product

def run_checkpoints():
    if solve(2) != 5:
        print("Checkpoint failed for max_power=2", file=sys.stderr)
        return False
    if solve(0) != 1:
        print("Checkpoint failed for max_power=0", file=sys.stderr)
        return False
    return True

def parse_arguments(args):
    options = {
        'max_power': 6,
        'run_checkpoints': True
    }
    
    i = 1
    while i < len(args):
        arg = args[i]
        if arg == '--skip-checkpoints':
            options['run_checkpoints'] = False
            i += 1
            continue
        
        if arg.startswith('--max-power='):
            try:
                value = int(arg[12:])
                if value < 0:
                    print("Unknown argument: " + arg, file=sys.stderr)
                    return None
                options['max_power'] = value
                i += 1
                continue
            except ValueError:
                print("Unknown argument: " + arg, file=sys.stderr)
                return None
        
        print("Unknown argument: " + arg, file=sys.stderr)
        return None
    
    if options['max_power'] < 0:
        print("Unknown argument: " + arg, file=sys.stderr)
        return None
    
    return options

def main():
    args = sys.argv
    options = parse_arguments(args)
    
    if options is None:
        sys.exit(1)
    
    if options['run_checkpoints'] and not run_checkpoints():
        sys.exit(2)
    
    try:
        result = solve(options['max_power'])
        print(result)
    except Exception as ex:
        print(str(ex), file=sys.stderr)
        sys.exit(3)

if __name__ == "__main__":
    main()
