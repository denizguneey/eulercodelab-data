import math
import sys

def solve(limit):
    count = [0] * (limit + 1)
    
    m = 2
    while 2 * m * (m + 1) <= limit:
        n = 1
        while n < m:
            if ((m - n) & 1) == 0:
                n += 1
                continue
            if math.gcd(m, n) != 1:
                n += 1
                continue
            
            p0 = 2 * m * (m + n)
            p = p0
            while p <= limit:
                count[p] += 1
                p += p0
            
            n += 1
        m += 1
    
    total = sum(1 for p in range(limit + 1) if count[p] == 1)
    return total

def main():
    limit = 1500000
    run_checkpoints_flag = True
    
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        arg = args[i]
        if arg == "--skip-checkpoints":
            run_checkpoints_flag = False
        elif arg.startswith("--limit="):
            try:
                limit = int(arg[8:])
            except ValueError:
                sys.stderr.write("Invalid argument: " + arg + "\n")
                sys.exit(1)
        else:
            sys.stderr.write("Unknown argument: " + arg + "\n")
            sys.exit(1)
        i += 1
    
    if limit < 12:
        sys.stderr.write("Limit must be at least 12\n")
        sys.exit(1)
    
    if run_checkpoints_flag:
        if solve(150) != 16:
            sys.stderr.write("Checkpoint failed for limit=150\n")
            sys.exit(2)
    
    print(solve(limit))

if __name__ == "__main__":
    main()
