# Problem 113: Non-bouncy numbers below 10^100
# Count = C(n+9,9) - 1 + C(n+10,10) - (n+1) - 9n

from math import comb

def solve():
    n = 100
    increasing = comb(n + 9, 9) - 1
    decreasing = comb(n + 10, 10) - (n + 1)
    flat_overlap = 9 * n
    print(increasing + decreasing - flat_overlap)

solve()
