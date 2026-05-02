import sys

def solve(max_a, max_b):
    values = set()
    
    for a in range(2, max_a + 1):
        value = 1
        for b in range(1, max_b + 1):
            value *= a
            if b >= 2:
                values.add(value)
    
    return len(values)

def main():
    max_a = 100
    max_b = 100
    run_checkpoints = True
    
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        arg = args[i]
        if arg == "--skip-checkpoints":
            run_checkpoints = False
            i += 1
            continue
        
        if arg.startswith("--max-a="):
            try:
                max_a = int(arg[8:])
                i += 1
                continue
            except ValueError:
                pass
        
        if arg.startswith("--max-b="):
            try:
                max_b = int(arg[8:])
                i += 1
                continue
            except ValueError:
                pass
        
        print(f"Unknown argument: {arg}", file=sys.stderr)
        sys.exit(1)
    
    if max_a < 2 or max_b < 2:
        sys.exit(1)
    
    if run_checkpoints:
        if solve(5, 5) != 15:
            print("Checkpoint failed for range 2..5", file=sys.stderr)
            sys.exit(2)
        if solve(10, 10) != 69:
            print("Checkpoint failed for range 2..10", file=sys.stderr)
            sys.exit(2)
    
    print(solve(max_a, max_b))

if __name__ == "__main__":
    main()
