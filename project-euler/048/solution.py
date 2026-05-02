import sys

kMod = 10000000000

def mod_pow(base, exponent):
    result = 1
    base %= kMod
    
    while exponent > 0:
        if exponent & 1:
            result = (result * base) % kMod
        base = (base * base) % kMod
        exponent >>= 1
    
    return result

def solve(n):
    total = 0
    for k in range(1, n + 1):
        total = (total + mod_pow(k, k)) % kMod
    return total

def main():
    n = 1000
    run_checkpoints = True
    
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        arg = args[i]
        if arg == "--skip-checkpoints":
            run_checkpoints = False
            i += 1
            continue
        
        if arg.startswith("--n="):
            try:
                n = int(arg[4:])
                if n < 1:
                    sys.stderr.write("Invalid value for --n\n")
                    return 1
            except ValueError:
                sys.stderr.write("Invalid value for --n\n")
                return 1
            i += 1
            continue
        
        sys.stderr.write(f"Unknown argument: {arg}\n")
        return 1
    
    if run_checkpoints:
        if solve(10) != 405071317:
            sys.stderr.write("Checkpoint failed for n=10\n")
            return 2
    
    print(solve(n))

if __name__ == "__main__":
    main()
