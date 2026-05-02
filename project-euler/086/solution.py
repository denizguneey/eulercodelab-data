# Problem 86: Cuboid route
# Find the least value of M such that the number of cuboid routes exceeds 1 million.

import math

def solve():
    target = 1000000
    total = 0
    for m in range(1, 2000):
        for s in range(2, 2 * m + 1):
            val = m * m + s * s
            r = int(math.isqrt(val))
            if r * r != val:
                continue
            lo = max(1, s - m)
            hi = min(m, s // 2)
            if hi >= lo:
                total += hi - lo + 1
        if total > target:
            print(m)
            return

solve()
