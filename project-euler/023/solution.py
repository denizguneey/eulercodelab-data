import sys

def proper_divisor_sums(limit):
    sums = [0] * (limit + 1)
    for d in range(1, limit // 2 + 1):
        for m in range(d * 2, limit + 1, d):
            sums[m] += d
    return sums

def solve(limit):
    sums = proper_divisor_sums(limit)
    
    abundant = []
    for n in range(12, limit + 1):
        if sums[n] > n:
            abundant.append(n)
    
    is_abundant_sum = [False] * (limit + 1)
    n_abundant = len(abundant)
    for i in range(n_abundant):
        for j in range(i, n_abundant):
            value = abundant[i] + abundant[j]
            if value > limit:
                break
            is_abundant_sum[value] = True
    
    total = 0
    for n in range(1, limit + 1):
        if not is_abundant_sum[n]:
            total += n
    
    return total

def run_checkpoints():
    if solve(50) != 891:
        sys.stderr.write("Checkpoint failed for limit=50\n")
        return False
    if solve(100) != 2766:
        sys.stderr.write("Checkpoint failed for limit=100\n")
        return False
    return True

def parse_arguments(args):
    limit = 28123
    run_checkpoints_flag = True
    
    i = 1
    while i < len(args):
        arg = args[i]
        if arg == "--skip-checkpoints":
            run_checkpoints_flag = False
        elif arg.startswith("--limit="):
            try:
                value_str = arg[8:]
                if not value_str:
                    return None, None
                value = int(value_str)
                if value < 1:
                    return None, None
                limit = value
            except ValueError:
                return None, None
        else:
            sys.stderr.write(f"Unknown argument: {arg}\n")
            return None, None
        i += 1
    
    if limit < 1:
        return None, None
    
    return limit, run_checkpoints_flag

def main():
    args = sys.argv
    limit, run_checkpoints_flag = parse_arguments(args)
    
    if limit is None:
        sys.exit(1)
    
    if run_checkpoints_flag and not run_checkpoints():
        sys.exit(2)
    
    print(solve(limit))

if __name__ == "__main__":
    main()
