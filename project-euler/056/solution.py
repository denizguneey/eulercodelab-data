import sys

def parse_int_after_prefix(arg, prefix):
    if not arg.startswith(prefix):
        return False, None
    tail = arg[len(prefix):]
    if not tail:
        return False, None
    
    try:
        parsed = int(tail)
        return True, parsed
    except ValueError:
        return False, None

def parse_arguments(args):
    options = {
        'a_max': 99,
        'b_max': 99,
        'run_checkpoints': True
    }
    
    i = 1
    while i < len(args):
        arg = args[i]
        if arg == '--skip-checkpoints':
            options['run_checkpoints'] = False
            i += 1
            continue
        
        success, value = parse_int_after_prefix(arg, '--a-max=')
        if success:
            options['a_max'] = value
            i += 1
            continue
        
        success, value = parse_int_after_prefix(arg, '--b-max=')
        if success:
            options['b_max'] = value
            i += 1
            continue
        
        print(f"Unknown argument: {arg}", file=sys.stderr)
        return None
    
    if options['a_max'] < 1 or options['b_max'] < 1:
        return None
    
    return options

def multiply_small(digits, mul):
    carry = 0
    for i in range(len(digits)):
        value = digits[i] * mul + carry
        digits[i] = value % 10
        carry = value // 10
    
    while carry > 0:
        digits.append(carry % 10)
        carry //= 10

def digit_sum(digits):
    return sum(digits)

def solve(a_max, b_max):
    best = 0
    
    for a in range(1, a_max + 1):
        value = [1]
        for b in range(1, b_max + 1):
            multiply_small(value, a)
            current_sum = digit_sum(value)
            if current_sum > best:
                best = current_sum
    
    return best

def run_checkpoints():
    if solve(10, 10) != 45:
        print("Checkpoint failed for 10x10 range", file=sys.stderr)
        return False
    return True

def main():
    args = sys.argv
    
    options = parse_arguments(args)
    if options is None:
        sys.exit(1)
    
    if options['run_checkpoints'] and not run_checkpoints():
        sys.exit(2)
    
    result = solve(options['a_max'], options['b_max'])
    print(result)

if __name__ == '__main__':
    main()
