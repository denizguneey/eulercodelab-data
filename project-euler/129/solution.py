# Problem 129: Repunit divisibility
# Find least n > 10^6 where A(n) > 10^6, where A(n) = smallest k with R(k) % n = 0.

from math import gcd

def solve():
    limit = 1000000
    for n in range(limit + 1, 10000000):
        if gcd(n, 10) != 1: continue
        rem = 1 % n
        k = 1
        while rem != 0 and k <= limit:
            rem = (rem * 10 + 1) % n
            k += 1
        if k > limit:
            print(n)
            return

solve()
