# Problem 120: Square remainders
# For 3 <= a <= 1000, find max r = ((a-1)^n + (a+1)^n) mod a^2.
# r_max(a) = a*(a-2) if a even, a*(a-1) if a odd.

def solve():
    total = 0
    for a in range(3, 1001):
        if a % 2 == 0:
            total += a * (a - 2)
        else:
            total += a * (a - 1)
    print(total)

solve()
