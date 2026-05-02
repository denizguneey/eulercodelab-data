import math
import sys

def pentagonal(n):
    return n * (3 * n - 1) // 2

def is_pentagonal(x):
    if x <= 0:
        return False
    disc = 1.0 + 24.0 * x
    root = math.isqrt(int(disc))
    # Check if disc is a perfect square
    if root * root != int(disc):
        return False
    # Calculate n = (1 + sqrt(1 + 24*x)) / 6
    n_val = (1 + root) / 6.0
    k = round(n_val)
    return pentagonal(k) == x

def solve(max_index):
    p = [0] * (max_index + 1)
    for i in range(1, max_index + 1):
        p[i] = pentagonal(i)
    
    best = float('inf')
    
    for j in range(2, max_index + 1):
        for k in range(j - 1, 0, -1):
            diff = p[j] - p[k]
            if diff >= best:
                break
            total_sum = p[j] + p[k]
            if is_pentagonal(diff) and is_pentagonal(total_sum):
                best = diff
    
    return best

def run_checkpoints():
    if not is_pentagonal(12) or not is_pentagonal(35) or is_pentagonal(36):
        return False
    if not is_pentagonal(40755):
        return False
    return True

def parse_arguments(args):
    max_index = 5000
    run_checkpoints_flag = True
    
    i = 1
    while i < len(args):
        arg = args[i]
        
        if arg == "--skip-checkpoints":
            run_checkpoints_flag = False
            i += 1
            continue
        
        if arg.startswith("--max-index="):
            try:
                max_index = int(arg[12:])
                if max_index < 10:
                    return None, None
            except ValueError:
                return None, None
        else:
            print(f"Unknown argument: {arg}", file=sys.stderr)
            return None, None
        
        i += 1
    
    return max_index, run_checkpoints_flag

def main():
    args = sys.argv[1:]
    
    max_index, run_checkpoints_flag = parse_arguments(args)
    if max_index is None:
        sys.exit(1)
    
    if run_checkpoints_flag and not run_checkpoints():
        sys.exit(2)
    
    result = solve(max_index)
    print(result)

if __name__ == "__main__":
    main()
