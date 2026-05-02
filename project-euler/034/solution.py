import sys

def digit_factorials():
    f = [1] * 10
    for d in range(1, 10):
        f[d] = f[d - 1] * d
    return f

def is_curious(value, fact):
    x = value
    total_sum = 0
    while x > 0:
        total_sum += fact[x % 10]
        x //= 10
    return total_sum == value

def solve():
    fact = digit_factorials()
    nine_factorial = fact[9]
    
    digits = 1
    pow10 = 1
    while pow10 <= digits * nine_factorial:
        digits += 1
        pow10 *= 10
    upper = (digits - 1) * nine_factorial
    
    total = 0
    for n in range(10, upper + 1):
        if is_curious(n, fact):
            total += n
    return total

def main():
    args = sys.argv[1:]
    run_checkpoints_flag = True
    
    for arg in args:
        if arg == "--skip-checkpoints":
            run_checkpoints_flag = False
        else:
            print(f"Unknown argument: {arg}", file=sys.stderr)
            sys.exit(1)
    
    if run_checkpoints_flag:
        fact = digit_factorials()
        if not is_curious(145, fact):
            print("Checkpoint failed for 145", file=sys.stderr)
            sys.exit(2)
        if not is_curious(40585, fact):
            print("Checkpoint failed for 40585", file=sys.stderr)
            sys.exit(2)
    
    print(solve())

if __name__ == "__main__":
    main()
