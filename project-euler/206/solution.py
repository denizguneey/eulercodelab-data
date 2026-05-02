# Problem 206: Concealed Square
# Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0

from math import isqrt

def solve():
    # Pattern: 1_2_3_4_5_6_7_8_9_0
    # Square ends in 0 so root ends in 0
    # Range: sqrt(1020304050607080900) to sqrt(1929394959697989990)
    low = isqrt(1020304050607080900)
    high = isqrt(1929394959697989990)
    # Root must end in 0, so step by 10. Actually ends in 30 or 70 mod 100.
    while low % 10 != 0:
        low += 1

    for base in range(low, high+1, 10):
        tail = base % 100
        if tail != 30 and tail != 70:
            continue
        sq = base * base
        # Check pattern: 1_2_3_4_5_6_7_8_9_0
        if sq % 10 != 0: continue
        sq //= 100
        ok = True
        for d in range(9, 0, -1):
            if sq % 10 != d:
                ok = False
                break
            sq //= 100
        if ok:
            print(base)
            return

solve()
