import math
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

def can_be_written(n):
    s = 1
    while 2 * s * s < n:
        candidate = n - 2 * s * s
        if is_prime(candidate):
            return True
        s += 1
    return False

def solve():
    n = 9
    while True:
        if not is_prime(n):
            if not can_be_written(n):
                return n
        n += 2

def main():
    args = sys.argv[1:]
    run_checkpoints_flag = True
    for arg in args:
        if arg == "--skip-checkpoints":
            run_checkpoints_flag = False
        else:
            sys.stderr.write(f"Unknown argument: {arg}\n")
            sys.exit(1)
    
    if run_checkpoints_flag:
        if not can_be_written(33):
            sys.stderr.write("Checkpoint failed for 33\n")
            sys.exit(2)
        if not can_be_written(45):
            sys.stderr.write("Checkpoint failed for 45\n")
            sys.exit(2)
    
    print(solve())

if __name__ == "__main__":
    main()
