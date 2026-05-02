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

def solve(target):
    primes = []
    
    n = 2
    while True:
        if is_prime(n):
            primes.append(n)
        
        ways = [0] * (n + 1)
        ways[0] = 1
        
        for p in primes:
            if p > n:
                break
            for s in range(p, n + 1):
                ways[s] += ways[s - p]
        
        if ways[n] > target:
            return n
        
        n += 1

def main():
    args = sys.argv[1:]
    
    target = 5000
    run_checkpoints = True
    
    i = 0
    while i < len(args):
        arg = args[i]
        if arg == "--skip-checkpoints":
            run_checkpoints = False
        elif arg.startswith("--target="):
            try:
                target = int(arg[9:])
            except ValueError:
                sys.stderr.write(f"Unknown argument: {arg}\n")
                sys.exit(1)
        else:
            sys.stderr.write(f"Unknown argument: {arg}\n")
            sys.exit(1)
        i += 1
    
    if target < 1:
        sys.exit(1)
    
    if run_checkpoints:
        if solve(5) != 11:
            sys.stderr.write("Checkpoint failed for target=5\n")
            sys.exit(2)
    
    print(solve(target))

if __name__ == "__main__":
    main()
