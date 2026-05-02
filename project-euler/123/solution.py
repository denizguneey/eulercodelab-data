# Problem 123: Prime square remainders
# Find n where r_n = ((p_n-1)^n + (p_n+1)^n) mod p_n^2 > 10^10.
# For odd n: r_n = 2*n*p_n. Find smallest odd n where 2*n*p_n > 10^10.

from sympy import nextprime

def solve():
    limit = 10**10
    p = 2
    for n in range(1, 1000000):
        if n % 2 == 1:
            if 2 * n * p > limit:
                print(n)
                return
        p = nextprime(p)

solve()
