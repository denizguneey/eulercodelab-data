# Problem 127: abc-hits
# Sum c for abc-hits: a+b=c, gcd(a,b)=1, rad(a*b*c) < c.

from math import gcd

def solve():
    limit = 120000
    rad = [1] * limit
    is_prime = [True] * limit
    for p in range(2, limit):
        if not is_prime[p]: continue
        for m in range(p, limit, p):
            rad[m] *= p
            if m > p: is_prime[m] = False
    
    # Sort values by rad for efficient pruning
    by_rad = sorted(range(1, limit), key=lambda n: (rad[n], n))
    
    total = 0
    for c in range(3, limit):
        rc = rad[c]
        threshold = c // rc
        for a in by_rad:
            if rad[a] >= threshold: break
            if a >= c // 2 + 1: continue
            b = c - a
            if rad[a] * rad[b] * rc >= c: continue
            if gcd(a, b) != 1: continue
            total += c
    
    print(total)

solve()
