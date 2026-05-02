import sys
from math import isqrt

def prime_sieve(limit):
    """Generate a boolean list where sieve[i] is True if i is prime."""
    sieve = [True] * (limit + 1)
    if limit >= 0:
        sieve[0] = False
    if limit >= 1:
        sieve[1] = False
    
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            for q in range(p * p, limit + 1, p):
                sieve[q] = False
    
    return sieve

def is_prime_trial(n):
    """Trial division primality test for large numbers."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    
    for p in range(3, isqrt(n) + 1, 2):
        if n % p == 0:
            return False
    return True

def is_circular_prime(n, sieve):
    """Check if all rotations of n are prime."""
    s = str(n)
    
    for _ in range(len(s)):
        # Rotate the string
        s = s[1:] + s[0]
        rot = int(s)
        
        # Check primality using sieve if possible, otherwise trial division
        if rot < len(sieve):
            prime = sieve[rot]
        else:
            prime = is_prime_trial(rot)
        
        if not prime:
            return False
    
    return True

def solve(limit):
    """Count circular primes below limit."""
    # Generate sieve with extra buffer for rotations
    sieve = prime_sieve(limit + 100)
    
    count = 0
    for n in range(2, limit):
        if not sieve[n]:
            continue
        if is_circular_prime(n, sieve):
            count += 1
    
    return count

def run_checkpoints():
    """Run verification checkpoints."""
    sieve = prime_sieve(1000)
    
    if not is_circular_prime(197, sieve):
        print("Checkpoint failed for 197", file=sys.stderr)
        return False
    
    if solve(100) != 13:
        print("Checkpoint failed for limit=100", file=sys.stderr)
        return False
    
    return True

def parse_arguments(args):
    """Parse command line arguments."""
    options = {
        'limit': 1000000,
        'run_checkpoints': True
    }
    
    i = 1
    while i < len(args):
        arg = args[i]
        
        if arg == '--skip-checkpoints':
            options['run_checkpoints'] = False
        elif arg.startswith('--limit='):
            try:
                value_str = arg[8:]
                if not value_str:
                    print("Unknown argument: " + arg, file=sys.stderr)
                    return None
                options['limit'] = int(value_str)
            except ValueError:
                print("Unknown argument: " + arg, file=sys.stderr)
                return None
        else:
            print("Unknown argument: " + arg, file=sys.stderr)
            return None
        
        i += 1
    
    if options['limit'] < 2:
        print("Limit must be at least 2", file=sys.stderr)
        return None
    
    return options

def main():
    """Main entry point."""
    args = sys.argv[1:]
    
    options = parse_arguments(args)
    if options is None:
        return 1
    
    if options['run_checkpoints'] and not run_checkpoints():
        return 2
    
    result = solve(options['limit'])
    print(result)

if __name__ == '__main__':
    main()
