import sys

def solve(size):
    total = 1
    for side in range(3, size + 1, 2):
        total += 4 * side * side - 6 * (side - 1)
    return total

def main():
    size = 1001
    run_checkpoints = True
    
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        arg = args[i]
        if arg == "--skip-checkpoints":
            run_checkpoints = False
            i += 1
            continue
        
        if arg.startswith("--size="):
            try:
                size = int(arg[7:])
                i += 1
                continue
            except ValueError:
                print(f"Unknown argument: {arg}", file=sys.stderr)
                sys.exit(1)
        
        print(f"Unknown argument: {arg}", file=sys.stderr)
        sys.exit(1)
    
    if size <= 0 or size % 2 == 0:
        print("Invalid size", file=sys.stderr)
        sys.exit(1)
    
    if run_checkpoints:
        if solve(5) != 101:
            print("Checkpoint failed for size=5", file=sys.stderr)
            sys.exit(2)
        if solve(7) != 261:
            print("Checkpoint failed for size=7", file=sys.stderr)
            sys.exit(2)
    
    print(solve(size))

if __name__ == "__main__":
    main()
