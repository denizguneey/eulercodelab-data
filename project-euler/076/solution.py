import sys

def solve(n):
    ways = [0] * (n + 1)
    ways[0] = 1
    
    for part in range(1, n):
        for s in range(part, n + 1):
            ways[s] += ways[s - part]
    
    return ways[n]

def main():
    n = 100
    run_checkpoints = True
    
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        arg = args[i]
        if arg == "--skip-checkpoints":
            run_checkpoints = False
            i += 1
            continue
        
        if arg.startswith("--n="):
            try:
                n = int(arg[4:])
                i += 1
                continue
            except ValueError:
                print(f"Invalid argument: {arg}", file=sys.stderr)
                sys.exit(1)
        
        print(f"Unknown argument: {arg}", file=sys.stderr)
        sys.exit(1)
    
    if n < 1:
        print("n must be >= 1", file=sys.stderr)
        sys.exit(1)
    
    if run_checkpoints:
        if solve(5) != 6:
            print("Checkpoint failed for n=5", file=sys.stderr)
            sys.exit(2)
    
    print(solve(n))

if __name__ == "__main__":
    main()
