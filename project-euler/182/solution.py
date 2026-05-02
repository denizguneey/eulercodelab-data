# Problem 182: RSA encryption — find the sum of e values that minimize unconcealed messages.
from math import gcd

def solve():
    p, q = 1009, 3643
    phi = (p-1)*(q-1)
    best = -1
    total = 0
    for e in range(2, phi):
        if gcd(e, phi) != 1: continue
        cnt = (gcd(e-1, p-1)+1) * (gcd(e-1, q-1)+1)
        if best < 0 or cnt < best:
            best = cnt
            total = e
        elif cnt == best:
            total += e
    print(total)

solve()
