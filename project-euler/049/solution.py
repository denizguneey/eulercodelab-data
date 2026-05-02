import sys
from collections import defaultdict

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

def sorted_digits(n):
    return ''.join(sorted(str(n)))

def solve():
    groups = defaultdict(list)
    
    for p in range(1000, 10000):
        if is_prime(p):
            groups[sorted_digits(p)].append(p)
    
    for key, values in groups.items():
        if len(values) < 3:
            continue
        
        values.sort()
        
        for i in range(len(values)):
            for j in range(i + 1, len(values)):
                a = values[i]
                b = values[j]
                c = 2 * b - a
                
                if c > 9999:
                    continue
                if c not in values:
                    continue
                if a == 1487 and b == 4817:
                    continue
                
                return int(str(a) + str(b) + str(c))
    
    return 0

def run_checkpoints():
    if not is_prime(1487) or not is_prime(4817) or not is_prime(8147):
        return False
    if sorted_digits(1487) != sorted_digits(4817) or sorted_digits(1487) != sorted_digits(8147):
        return False
    return True

def main():
    args = sys.argv[1:]
    run_checkpoints_flag = True
    
    for arg in args:
        if arg == "--skip-checkpoints":
            run_checkpoints_flag = False
        else:
            sys.stderr.write(f"Unknown argument: {arg}\n")
            sys.exit(1)
    
    if run_checkpoints_flag and not run_checkpoints():
        sys.exit(2)
    
    print(solve())

if __name__ == "__main__":
    main()
