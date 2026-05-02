import sys

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

def consecutive_prime_count(a, b):
    n = 0
    while True:
        value = n * n + a * n + b
        if not is_prime(value):
            break
        n += 1
    return n

def solve(abs_a, abs_b):
    best_a = 0
    best_b = 0
    best_count = -1

    for a in range(-abs_a, abs_a + 1):
        for b in range(-abs_b, abs_b + 1):
            if not is_prime(b):
                continue
            count = consecutive_prime_count(a, b)
            if count > best_count:
                best_count = count
                best_a = a
                best_b = b

    return best_a * best_b

def run_checkpoints():
    if consecutive_prime_count(1, 41) != 40:
        sys.stderr.write("Checkpoint failed for n^2+n+41\n")
        return False
    if consecutive_prime_count(-79, 1601) != 80:
        sys.stderr.write("Checkpoint failed for n^2-79n+1601\n")
        return False
    return True

def parse_int_after_prefix(arg, prefix):
    if not arg.startswith(prefix):
        return False, None
    tail = arg[len(prefix):]
    if not tail:
        return False, None
    try:
        value = int(tail)
        if value < 0:
            return False, None
        return True, value
    except ValueError:
        return False, None

def main():
    abs_a = 999
    abs_b = 999
    run_checkpoints_flag = True
    
    args = sys.argv[1:]
    for arg in args:
        if arg == "--skip-checkpoints":
            run_checkpoints_flag = False
        else:
            success, value = parse_int_after_prefix(arg, "--abs-a=")
            if success:
                abs_a = value
                continue
            success, value = parse_int_after_prefix(arg, "--abs-b=")
            if success:
                abs_b = value
                continue
            sys.stderr.write(f"Unknown argument: {arg}\n")
            return 1
    
    if abs_a < 0 or abs_b < 0:
        sys.stderr.write("Invalid arguments\n")
        return 1
    
    if run_checkpoints_flag and not run_checkpoints():
        return 2
    
    print(solve(abs_a, abs_b))

if __name__ == "__main__":
    main()
