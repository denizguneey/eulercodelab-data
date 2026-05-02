# Problem 188: The hyperexponentiation of a number.
# Compute 1777↑↑1855 mod 10^8 using Euler's theorem.

from math import gcd

def solve():
    base = 1777
    height = 1855
    mod = 10**8

    def euler_phi(n):
        result = n
        p = 2
        while p*p <= n:
            if n % p == 0:
                while n % p == 0: n //= p
                result -= result // p
            p += 1
        if n > 1: result -= result // n
        return result

    def tetration_mod(b, h, m):
        if m == 1: return 0
        if h == 1: return b % m
        ph = euler_phi(m)
        exp = tetration_mod(b, h-1, ph)
        if gcd(b, m) != 1:
            exp += ph
        return pow(b, exp, m)

    print(tetration_mod(base, height, mod))

solve()
