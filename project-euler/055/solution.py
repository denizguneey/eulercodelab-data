import sys

def parse_int_after_prefix(arg, prefix):
    if not arg.startswith(prefix):
        return False, None
    tail = arg[len(prefix):]
    if not tail:
        return False, None
    
    try:
        value = int(tail)
        if str(value) != tail:  # Check for leading zeros or invalid characters
            return False, None
        return True, value
    except ValueError:
        return False, None

def parse_arguments(args):
    options = {
        'limit': 10000,
        'max_steps': 50,
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
        
        found, value = parse_int_after_prefix(arg, "--max-steps=")
        if found:
            options['max_steps'] = value
            i += 1
            continue
        
        print(f"Unknown argument: {arg}", file=sys.stderr)
        return None
    
    if options['limit'] < 1 or options['max_steps'] < 1:
        return None
    
    return options

def is_palindrome(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            return False
    return True

def add_decimal_strings(a, b):
    n = max(len(a), len(b))
    
    out = []
    carry = 0
    
    for i in range(n):
        total = carry
        if i < len(a):
            total += ord(a[len(a) - 1 - i]) - ord('0')
        if i < len(b):
            total += ord(b[len(b) - 1 - i]) - ord('0')
        
        out.append(str(total % 10))
        carry = total // 10
    
    while carry > 0:
        out.append(str(carry % 10))
        carry //= 10
    
    return ''.join(reversed(out))

def is_lychrel_candidate(n, max_steps):
    value = str(n)
    
    for step in range(max_steps):
        rev = value[::-1]
        value = add_decimal_strings(value, rev)
        if is_palindrome(value):
            return False
    
    return True

def solve(limit, max_steps):
    count = 0
    for n in range(1, limit):
        if is_lychrel_candidate(n, max_steps):
            count += 1
    return count

def run_checkpoints():
    if is_lychrel_candidate(47, 50):
        print("Checkpoint failed for 47", file=sys.stderr)
        return False
    if is_lychrel_candidate(349, 3):
        print("Checkpoint failed for 349", file=sys.stderr)
        return False
    return True

def main():
    args = sys.argv
    
    options = parse_arguments(args)
    if options is None:
        sys.exit(1)
    
    if options['run_checkpoints'] and not run_checkpoints():
        sys.exit(2)
    
    result = solve(options['limit'], options['max_steps'])
    print(result)

if __name__ == "__main__":
    main()
