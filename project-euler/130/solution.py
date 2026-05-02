# Problem 130: Composites with prime repunit property
# Find sum of first 25 composite n (coprime to 10) where (n-1) % A(n) = 0.

from sympy import isprime
from math import gcd

def A_of_n(n):
    rem = 1 % n
    k = 1
    while rem != 0:
        rem = (rem * 10 + 1) % n
        k += 1
    return k

def solve():
    found = 0
    total = 0
    n = 3
    while found < 25:
        if n % 5 != 0 and not isprime(n) and gcd(n, 10) == 1:
            a = A_of_n(n)
            if (n - 1) % a == 0:
                found += 1
                total += n
        n += 2
    print(total)

solve()
