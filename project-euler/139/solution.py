# Problem 139: Pythagorean tiles
# Count primitive Pythagorean triples with perimeter < 10^8 where c % |a-b| == 0.

from math import gcd

def solve():
    limit = 100000000
    count = 0
    for m in range(2, limit):
        if 2 * m * (m + 1) >= limit: break
        for n in range(1, m):
            if (m - n) % 2 == 0: continue
            if gcd(m, n) != 1: continue
            a = m*m - n*n
            b = 2*m*n
            c = m*m + n*n
            diff = abs(a - b)
            if c % diff != 0: continue
            perimeter = a + b + c
            count += (limit - 1) // perimeter
    print(count)

solve()
