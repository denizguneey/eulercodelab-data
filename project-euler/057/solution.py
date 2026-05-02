import sys

def digit_count(x):
    return len(str(x))

def solve(expansions):
    num = 3  # first expansion numerator
    den = 2  # first expansion denominator
    
    count = 0
    
    for _ in range(1, expansions + 1):
        if digit_count(num) > digit_count(den):
            count += 1
        
        next_num = num + 2 * den
        next_den = num + den
        num, den = next_num, next_den
    
    return count

def main():
    expansions = 1000
    run_checkpoints = True
    
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        arg = args[i]
        if arg == "--skip-checkpoints":
            run_checkpoints = False
            i += 1
        elif arg.startswith("--expansions="):
            try:
                expansions = int(arg[len("--expansions="):])
                if expansions < 1:
                    sys.exit(1)
            except ValueError:
                sys.exit(1)
            i += 1
        else:
            print(f"Unknown argument: {arg}", file=sys.stderr)
            sys.exit(1)
    
    if run_checkpoints:
        if solve(8) != 1:
            print("Checkpoint failed for first 8 expansions", file=sys.stderr)
            sys.exit(2)
    
    print(solve(expansions))

if __name__ == "__main__":
    main()
