import sys

def int_pow(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result

def solve(power):
    digit_power = [int_pow(d, power) for d in range(10)]
    
    max_digit_term = digit_power[9]
    
    digits = 1
    pow10 = 1
    while pow10 <= digits * max_digit_term:
        digits += 1
        pow10 *= 10
    
    upper = (digits - 1) * max_digit_term
    
    total = 0
    for n in range(2, upper + 1):
        x = n
        s = 0
        while x > 0:
            s += digit_power[x % 10]
            x //= 10
        if s == n:
            total += n
    
    return total

def run_checkpoints():
    if solve(4) != 19316:
        return False
    return True

def main():
    power = 5
    run_checkpoints_flag = True
    
    args = sys.argv[1:]
    for arg in args:
        if arg == "--skip-checkpoints":
            run_checkpoints_flag = False
        elif arg.startswith("--power="):
            try:
                power = int(arg[8:])
            except ValueError:
                print(f"Invalid argument: {arg}", file=sys.stderr)
                sys.exit(1)
        else:
            print(f"Unknown argument: {arg}", file=sys.stderr)
            sys.exit(1)
    
    if power < 2:
        print("Power must be at least 2", file=sys.stderr)
        sys.exit(1)
    
    if run_checkpoints_flag and not run_checkpoints():
        print("Checkpoint failed for power=4", file=sys.stderr)
        sys.exit(2)
    
    print(solve(power))

if __name__ == "__main__":
    main()
