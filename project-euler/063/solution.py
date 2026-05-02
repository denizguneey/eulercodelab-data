import sys

def digit_count(x):
    return len(str(x))

def solve():
    total = 0
    
    for base in range(1, 10):
        value = 1
        power = 1
        while True:
            value *= base
            digits = digit_count(value)
            if digits == power:
                total += 1
            if digits < power:
                break
            power += 1
    
    return total

def run_checkpoints():
    value = 1
    for i in range(21):
        value *= 9
    if digit_count(value) != 21:
        print("Checkpoint failed for 9^21", file=sys.stderr)
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
    main()
