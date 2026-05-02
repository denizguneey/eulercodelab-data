import sys

def parse_int_after_prefix(arg, prefix):
    if not arg.startswith(prefix):
        return False, 0
    tail = arg[len(prefix):]
    if not tail:
        return False, 0
    
    try:
        value = int(tail)
        if str(value) != tail:  # Check for leading zeros or invalid characters
            return False, 0
        return True, value
    except ValueError:
        return False, 0

def parse_arguments(args):
    options = {
        'limit': 1000000,
        'target_length': 60,
        'run_checkpoints': True
    }
    
    i = 1
    while i < len(args):
        arg = args[i]
        if arg == "--skip-checkpoints":
            options['run_checkpoints'] = False
            i += 1
            continue
        
        found, value = parse_int_after_prefix(arg, "--limit=")
        if found:
            options['limit'] = value
            i += 1
            continue
        
        found, value = parse_int_after_prefix(arg, "--target-length=")
        if found:
            options['target_length'] = value
            i += 1
            continue
        
        print(f"Unknown argument: {arg}", file=sys.stderr)
        return None
    
    if options['limit'] < 1 or options['target_length'] < 1:
        return None
    
    return options

def next_value(n, fac):
    total = 0
    while n > 0:
        total += fac[n % 10]
        n //= 10
    return total

def chain_length(start, fac, memo):
    order = []
    seen = {}
    
    n = start
    while True:
        if n in memo:
            length = memo[n]
            for i in range(len(order) - 1, -1, -1):
                length += 1
                memo[order[i]] = length
            return memo[start]
        
        if n in seen:
            loop_start = seen[n]
            loop_len = len(order) - loop_start
            
            for i in range(loop_start, len(order)):
                memo[order[i]] = loop_len
            
            length = loop_len
            for i in range(loop_start - 1, -1, -1):
                length += 1
                memo[order[i]] = length
            
            return memo[start]
        
        seen[n] = len(order)
        order.append(n)
        n = next_value(n, fac)

def run_checkpoints():
    fac = [1] * 10
    for d in range(1, 10):
        fac[d] = fac[d-1] * d
    
    memo = {}
    
    if chain_length(69, fac, memo) != 5:
        print("Checkpoint failed for start=69", file=sys.stderr)
        return False
    
    if chain_length(78, fac, memo) != 4:
        print("Checkpoint failed for start=78", file=sys.stderr)
        return False
    
    return True

def solve(limit, target_length):
    fac = [1] * 10
    for d in range(1, 10):
        fac[d] = fac[d-1] * d
    
    memo = {}
    
    count = 0
    for n in range(1, limit):
        if chain_length(n, fac, memo) == target_length:
            count += 1
    
    return count

def main():
    args = sys.argv[1:]
    
    options = parse_arguments(args)
    if options is None:
        sys.exit(1)
    
    if options['run_checkpoints'] and not run_checkpoints():
        sys.exit(2)
    
    result = solve(options['limit'], options['target_length'])
    print(result)

if __name__ == "__main__":
    main()
