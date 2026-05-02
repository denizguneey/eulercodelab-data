import sys

def solve(limit):
    # Sieve to generate primes up to 100
    is_prime = [True] * (limit + 1) if limit >= 2 else []
    is_prime[0:2] = [False, False]
    
    # Generate primes up to 100 (as in original code)
    max_sieve = 100
    is_prime = [True] * (max_sieve + 1)
    is_prime[0:2] = [False, False]
    
    for p in range(2, int(max_sieve ** 0.5) + 1):
        if is_prime[p]:
            for q in range(p * p, max_sieve + 1, p):
                is_prime[q] = False
    
    primes = [p for p in range(2, max_sieve + 1) if is_prime[p]]
    
    product = 1
    for p in primes:
        if product * p > limit:
            break
        product *= p
    
    return int(product)

def main():
    # Parse command line arguments
    limit = 1000000
    run_checkpoints = True
    
    args = sys.argv[1:]
    for arg in args:
        if arg == "--skip-checkpoints":
            run_checkpoints = False
        elif arg.startswith("--limit="):
            try:
                limit_val = int(arg[8:])
                if limit_val < 2:
                    sys.exit(1)
                limit = limit_val
            except ValueError:
                print(f"Unknown argument: {arg}", file=sys.stderr)
                sys.exit(1)
        else:
            print(f"Unknown argument: {arg}", file=sys.stderr)
            sys.exit(1)
    
    # Run checkpoints if enabled
    if run_checkpoints:
        if solve(10) != 6:
            print("Checkpoint failed for limit=10", file=sys.stderr)
            sys.exit(2)
    
    print(solve(limit))

if __name__ == "__main__":
    main()
