import sys
from itertools import permutations

def has_substring_divisibility(s: str) -> bool:
    divisors = [2, 3, 5, 7, 11, 13, 17]
    
    if len(s) != 10:
        return False
    if s[0] == '0':
        return False
    
    for i in range(7):
        value = int(s[i+1]) * 100 + int(s[i+2]) * 10 + int(s[i+3])
        if value % divisors[i] != 0:
            return False
    
    return True

def solve() -> int:
    digits = "0123456789"
    total = 0
    
    for perm in permutations(digits):
        s = ''.join(perm)
        if has_substring_divisibility(s):
            total += int(s)
    
    return total

def run_checkpoints() -> bool:
    if not has_substring_divisibility("1406357289"):
        print("Checkpoint failed for 1406357289", file=sys.stderr)
        return False
    if has_substring_divisibility("1234567890"):
        print("Checkpoint failed for invalid example", file=sys.stderr)
        return False
    return True

def main():
    args = sys.argv[1:]
    run_checkpoints_flag = True
    
    for arg in args:
        if arg == "--skip-checkpoints":
            run_checkpoints_flag = False
        else:
            print(f"Unknown argument: {arg}", file=sys.stderr)
            sys.exit(1)
    
    if run_checkpoints_flag and not run_checkpoints():
        sys.exit(2)
    
    print(solve())

if __name__ == "__main__":
    main()
