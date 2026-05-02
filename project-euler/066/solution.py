import math
import sys

def minimal_x_for_pell(D):
    a0 = int(math.isqrt(D))
    if a0 * a0 == D:
        return 0
    
    m = 0
    d = 1
    a = a0
    
    num_prev = 1
    num = a
    den_prev = 0
    den = 1
    
    while num * num - D * den * den != 1:
        m = d * a - m
        d = (D - m * m) // d
        a = (a0 + m) // d
        
        next_num = a * num + num_prev
        next_den = a * den + den_prev
        num_prev, den_prev = num, den
        num, den = next_num, next_den
    
    return num

def solve(limit):
    best_D = 0
    best_x = 0
    
    for D in range(2, limit + 1):
        x = minimal_x_for_pell(D)
        if x > best_x:
            best_x = x
            best_D = D
    
    return best_D

def main():
    args = sys.argv[1:]
    
    limit = 1000
    run_checkpoints_flag = True
    
    i = 0
    while i < len(args):
        arg = args[i]
        if arg == "--skip-checkpoints":
            run_checkpoints_flag = False
            i += 1
            continue
        
        if arg.startswith("--limit="):
            try:
                limit = int(arg[8:])
                i += 1
                continue
            except ValueError:
                print(f"Invalid argument: {arg}", file=sys.stderr)
                sys.exit(1)
        
        print(f"Unknown argument: {arg}", file=sys.stderr)
        sys.exit(1)
    
    if limit < 2:
        print("Limit must be at least 2", file=sys.stderr)
        sys.exit(1)
    
    if run_checkpoints_flag:
        if solve(7) != 5:
            print("Checkpoint failed for limit=7", file=sys.stderr)
            sys.exit(2)
        if solve(13) != 13:
            print("Checkpoint failed for limit=13", file=sys.stderr)
            sys.exit(2)
    
    print(solve(limit))

if __name__ == "__main__":
    main()
