import sys

def solve(limit):
    phi = list(range(limit + 1))
    
    for i in range(2, limit + 1):
        if phi[i] == i:
            for j in range(i, limit + 1, i):
                phi[j] -= phi[j] // i
    
    total = sum(phi[2:limit + 1])
    return total

def main():
    limit = 1000000
    run_checkpoints = True
    
    args = sys.argv[1:]
    for arg in args:
        if arg == "--skip-checkpoints":
            run_checkpoints = False
        elif arg.startswith("--limit="):
            try:
                limit = int(arg[8:])
                if limit < 2:
                    sys.exit(1)
            except ValueError:
                sys.stderr.write(f"Unknown argument: {arg}\n")
                sys.exit(1)
        else:
            sys.stderr.write(f"Unknown argument: {arg}\n")
            sys.exit(1)
    
    if run_checkpoints:
        if solve(8) != 21:
            sys.stderr.write("Checkpoint failed for limit=8\n")
            sys.exit(2)
    
    print(solve(limit))

if __name__ == "__main__":
    main()
