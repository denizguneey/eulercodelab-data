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

def is_truncatable_prime(n):
    if n < 10 or not is_prime(n):
        return False
    
    s = str(n)
    for i in range(1, len(s)):
        left = int(s[i:])
        right = int(s[:len(s)-i])
        if not is_prime(left) or not is_prime(right):
            return False
    
    return True

def solve():
    count = 0
    total = 0
    n = 11
    
    while count < 11:
        if is_truncatable_prime(n):
            total += n
            count += 1
        n += 2
    
    return total

def run_checkpoints():
    if not is_truncatable_prime(3797):
        sys.stderr.write("Checkpoint failed for 3797\n")
        return False
    if is_truncatable_prime(47):
        sys.stderr.write("Checkpoint failed for 47\n")
        return False
    return True

def main():
    args = sys.argv[1:]
    skip_checkpoints = False
    
    for arg in args:
        if arg == "--skip-checkpoints":
            skip_checkpoints = True
        else:
            sys.stderr.write(f"Unknown argument: {arg}\n")
            return 1
    
    if not skip_checkpoints and not run_checkpoints():
        return 2
    
    print(solve())
    return 0

if __name__ == "__main__":
    sys.exit(main())
