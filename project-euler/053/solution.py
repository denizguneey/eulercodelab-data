import sys

def solve(n_max, threshold):
    count = 0
    
    for n in range(1, n_max + 1):
        c = 1
        for r in range(1, n // 2 + 1):
            c = (c * (n - r + 1)) // r
            if c > threshold:
                count += (n + 1) - 2 * r
                break
    
    return count

def main():
    n_max = 100
    threshold = 1000000
    run_checkpoints = True
    
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        arg = args[i]
        if arg == "--skip-checkpoints":
            run_checkpoints = False
            i += 1
            continue
        
        if arg.startswith("--n-max="):
            try:
                n_max = int(arg[8:])
                i += 1
                continue
            except ValueError:
                sys.stderr.write(f"Unknown argument: {arg}\n")
                sys.exit(1)
        
        if arg.startswith("--threshold="):
            try:
                threshold = int(arg[12:])
                i += 1
                continue
            except ValueError:
                sys.stderr.write(f"Unknown argument: {arg}\n")
                sys.exit(1)
        
        sys.stderr.write(f"Unknown argument: {arg}\n")
        sys.exit(1)
    
    if n_max < 1 or threshold < 1:
        sys.stderr.write("Invalid arguments\n")
        sys.exit(1)
    
    if run_checkpoints:
        if solve(10, 10) != 25:
            sys.stderr.write("Checkpoint failed for n_max=10 threshold=10\n")
            sys.exit(2)
    
    print(solve(n_max, threshold))

if __name__ == "__main__":
    main()
