# Problem 118: Pandigital prime sets
# Count sets of pandigital (1-9) primes.

from sympy import isprime
from itertools import permutations

def solve():
    # Generate all primes using digits 1-9 (each exactly once)
    # Then count partitions
    entries = []
    
    def gen_primes(used_mask, value):
        if value > 0 and isprime(value):
            entries.append((value, used_mask))
        for d in range(1, 10):
            bit = 1 << (d - 1)
            if used_mask & bit: continue
            gen_primes(used_mask | bit, value * 10 + d)
    
    gen_primes(0, 0)
    entries = list(set(entries))
    entries.sort()
    
    full_mask = (1 << 9) - 1
    memo = {}
    
    def dfs(remaining):
        if remaining == 0: return 1
        if remaining in memo: return memo[remaining]
        anchor = remaining & (-remaining)
        total = 0
        for val, mask in entries:
            if not (mask & anchor): continue
            if (mask & remaining) != mask: continue
            total += dfs(remaining ^ mask)
        memo[remaining] = total
        return total
    
    print(dfs(full_mask))

solve()
