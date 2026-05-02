import sys

def sieve(limit):
    prime = [True] * (limit + 1)
    prime[0] = False
    prime[1] = False
    
    p = 2
    while p * p <= limit:
        if not prime[p]:
            p += 1
            continue
        q = p * p
        while q <= limit:
            prime[q] = False
            q += p
        p += 1
    
    return prime

def is_prime_trial(n):
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

def is_prime_fast(n, sieve_table):
    if n < len(sieve_table):
        return sieve_table[n]
    return is_prime_trial(n)

def solve(family_size, sieve_limit):
    sieve_table = sieve(sieve_limit)
    
    for p in range(11, sieve_limit + 1):
        if not sieve_table[p]:
            continue
        
        base = str(p)
        
        for target_digit in '0123456789':
            positions = []
            for i, ch in enumerate(base):
                if ch == target_digit:
                    positions.append(i)
            
            if not positions:
                continue
            
            subsets = 1 << len(positions)
            for mask in range(1, subsets):
                family_count = 0
                smallest_family_prime = float('inf')
                
                for replacement in '0123456789':
                    candidate = list(base)
                    for bit in range(len(positions)):
                        if (mask >> bit) & 1:
                            candidate[positions[bit]] = replacement
                    
                    if candidate[0] == '0':
                        continue
                    
                    value = int(''.join(candidate))
                    if is_prime_fast(value, sieve_table):
                        family_count += 1
                        if value < smallest_family_prime:
                            smallest_family_prime = value
                
                if family_count >= family_size and smallest_family_prime == p:
                    return p
    
    return 0

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--family-size', type=int, default=8)
    parser.add_argument('--sieve-limit', type=int, default=2000000)
    parser.add_argument('--skip-checkpoints', action='store_true')
    
    args = parser.parse_args()
    
    if not args.skip_checkpoints:
        # Checkpoint for family size 6
        if solve(6, 100000) != 13:
            sys.stderr.write("Checkpoint failed for family size 6\n")
            return 2
    
    result = solve(args.family_size, args.sieve_limit)
    print(result)
    return 0

if __name__ == "__main__":
    sys.exit(main())
