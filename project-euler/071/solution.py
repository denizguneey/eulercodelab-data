import math
import sys

def solve(limit):
    best_n = 0
    best_d = 1
    
    for d in range(2, limit + 1):
        n = (3 * d - 1) // 7
        if math.gcd(d, n) != 1:
            continue
        if n * best_d > best_n * d:
            best_n = n
            best_d = d
    
    return int(best_n)

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
            except ValueError:
                sys.stderr.write("Invalid limit value\n")
                sys.exit(1)
        else:
            sys.stderr.write(f"Unknown argument: {arg}\n")
            sys.exit(1)
    
    if limit < 2:
        sys.stderr.write("Limit must be at least 2\n")
        sys.exit(1)
    
    if run_checkpoints:
        if solve(8) != 2:
            sys.stderr.write("Checkpoint failed for limit=8\n")
            sys.exit(2)
    
    print(solve(limit))

if __name__ == "__main__":
    main()
