import sys
from itertools import permutations

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

def solve():
    for n in range(9, 0, -1):
        digit_sum = n * (n + 1) // 2
        if digit_sum % 3 == 0:
            continue
        
        digits = list(range(n, 0, -1))
        
        while True:
            value = int(''.join(map(str, digits)))
            if is_prime(value):
                return value
            
            # Generate next permutation in descending order
            i = len(digits) - 2
            while i >= 0 and digits[i] <= digits[i + 1]:
                i -= 1
            
            if i < 0:
                break
                
            j = len(digits) - 1
            while digits[j] >= digits[i]:
                j -= 1
                
            digits[i], digits[j] = digits[j], digits[i]
            digits[i + 1:] = reversed(digits[i + 1:])
    
    return 0

def main():
    args = sys.argv[1:]
    run_checkpoints = True
    
    for arg in args:
        if arg == "--skip-checkpoints":
            run_checkpoints = False
        else:
            print(f"Unknown argument: {arg}", file=sys.stderr)
            sys.exit(1)
    
    if run_checkpoints:
        if not is_prime(2143):
            print("Checkpoint failed for prime 2143", file=sys.stderr)
            sys.exit(2)
        if is_prime(2145):
            print("Checkpoint failed for composite 2145", file=sys.stderr)
            sys.exit(2)
    
    print(solve())

if __name__ == "__main__":
    main()
