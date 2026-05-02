import sys

def is_1_to_9_pandigital(s):
    if len(s) != 9:
        return False
    
    used = [False] * 10
    for c in s:
        d = ord(c) - ord('0')
        if d <= 0 or d >= 10 or used[d]:
            return False
        used[d] = True
    
    for d in range(1, 10):
        if not used[d]:
            return False
    
    return True

def concatenated_product(base, max_multiplier):
    out = []
    for n in range(1, max_multiplier + 1):
        out.append(str(base * n))
    return ''.join(out)

def solve():
    best = 0
    for base in range(1, 10000):
        concat = ""
        n = 1
        while len(concat) < 9:
            concat += str(base * n)
            if len(concat) == 9 and n >= 2 and is_1_to_9_pandigital(concat):
                best = max(best, int(concat))
            n += 1
    return best

def run_checkpoints():
    if concatenated_product(192, 3) != "192384576":
        print("Checkpoint failed for base=192", file=sys.stderr)
        return False
    if not is_1_to_9_pandigital("123456789"):
        print("Checkpoint failed for pandigital helper", file=sys.stderr)
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
            return 1
    
    if run_checkpoints_flag and not run_checkpoints():
        return 2
    
    print(solve())
    return 0

if __name__ == "__main__":
    sys.exit(main())
