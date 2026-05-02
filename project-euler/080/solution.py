# Problem 80: Square root digital expansion
# For the first 100 natural numbers, find the total of the digital sums
# of the first 100 decimal digits for all irrational square roots.

from decimal import Decimal, getcontext

def solve():
    getcontext().prec = 110
    total = 0
    for n in range(1, 101):
        r = int(n**0.5)
        if r * r == n:
            continue
        s = Decimal(n).sqrt()
        digits = str(s).replace('.', '')[:100]
        total += sum(int(d) for d in digits)
    print(total)

solve()
