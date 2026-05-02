import sys

def coefficient_for_e(index):
    if index == 0:
        return 2
    if index % 3 == 2:
        return 2 * ((index + 1) // 3)
    return 1

def convergent_numerator(term):
    num_prev = 1
    num = coefficient_for_e(0)
    den_prev = 0
    den = 1

    if term == 1:
        return num

    for i in range(1, term):
        a = coefficient_for_e(i)
        next_num = a * num + num_prev
        next_den = a * den + den_prev
        num_prev, den_prev = num, den
        num, den = next_num, next_den

    return num

def digit_sum(x):
    s = str(x)
    return sum(int(c) for c in s)

def solve(term):
    return digit_sum(convergent_numerator(term))

def main():
    args = sys.argv[1:]
    
    term = 100
    run_checkpoints = True
    
    i = 0
    while i < len(args):
        arg = args[i]
        
        if arg == "--skip-checkpoints":
            run_checkpoints = False
            i += 1
            continue
            
        if arg.startswith("--term="):
            try:
                term = int(arg[7:])
                i += 1
                continue
            except ValueError:
                print(f"Invalid argument: {arg}", file=sys.stderr)
                sys.exit(1)
        
        print(f"Unknown argument: {arg}", file=sys.stderr)
        sys.exit(1)
    
    if term < 1:
        print("Invalid term value", file=sys.stderr)
        sys.exit(1)
    
    if run_checkpoints:
        if solve(10) != 17:
            print("Checkpoint failed for term=10", file=sys.stderr)
            sys.exit(2)
    
    print(solve(term))

if __name__ == "__main__":
    main()
