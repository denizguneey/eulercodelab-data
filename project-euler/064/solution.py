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

def period_length(n):
    a0 = int(math.isqrt(n))
    if a0 * a0 == n:
        return 0
    
    m = 0
    d = 1
    a = a0
    period = 0
    
    while True:
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        period += 1
        if a == 2 * a0:
            break
    
    return period

def solve(limit):
    count = 0
    for n in range(2, limit + 1):
        if period_length(n) % 2 == 1:
            count += 1
    return count

def main():
    limit = 10000
    run_checkpoints = True
    
    args = sys.argv[1:]
    for arg in args:
        if arg == "--skip-checkpoints":
            run_checkpoints = False
        else:
            success, value = parse_int_after_prefix(arg, "--limit=")
            if success:
                limit = value
            else:
                print(f"Unknown argument: {arg}", file=sys.stderr)
                sys.exit(1)
    
    if limit < 2:
        print("Limit must be at least 2", file=sys.stderr)
        sys.exit(1)
    
    if run_checkpoints:
        if solve(13) != 4:
            print("Checkpoint failed for limit=13", file=sys.stderr)
            sys.exit(2)
    
    print(solve(limit))

if __name__ == "__main__":
    main()
