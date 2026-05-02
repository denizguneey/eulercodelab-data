# Problem 100: Arranged probability
# Find the number of blue discs for the first arrangement with > 10^12 total discs
# such that P(two blue) = 1/2.

def solve():
    blue, total = 15, 21
    limit = 10**12
    while total <= limit:
        nb = 3 * blue + 2 * total - 2
        nt = 4 * blue + 3 * total - 3
        blue, total = nb, nt
    print(blue)

solve()
