# Problem 183: Maximum product from partitions.
# D(N) = -N if N/k has terminating decimal, +N otherwise.
import math

def solve():
    total = 0
    for n in range(5, 10001):
        k = round(n / math.e)
        q = k // math.gcd(n, k)
        while q % 2 == 0: q //= 2
        while q % 5 == 0: q //= 5
        total += -n if q == 1 else n
    print(total)

solve()
