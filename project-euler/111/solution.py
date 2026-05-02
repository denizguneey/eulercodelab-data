# Problem 111: Primes with runs
# Sum of all 10-digit primes with maximum repeated digits.

from sympy import isprime
from itertools import combinations

def solve():
    n = 10
    total = 0
    for d in range(10):
        for replacements in range(1, n + 1):
            primes = []
            positions = list(combinations(range(n), replacements))
            for pos in positions:
                digits = [d] * n
                def fill(idx, digs):
                    if idx == len(pos):
                        if digs[0] == 0: return
                        val = int(''.join(map(str, digs)))
                        if isprime(val):
                            primes.append(val)
                        return
                    for r in range(10):
                        if r == d: continue
                        digs[pos[idx]] = r
                        fill(idx + 1, digs)
                        digs[pos[idx]] = d
                fill(0, digits)
            if primes:
                total += sum(set(primes))
                break
    print(total)

solve()
