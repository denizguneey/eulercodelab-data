# Problem 128: Hexagonal tile differences
# Find the 2000th tile in the hexagonal grid where PD(n) = 3.
from sympy import isprime

def solve():
    target = 2000
    values = [1, 2]
    k = 2
    while len(values) < target:
        # First cell of ring k: 3k(k-1)+2
        # Last cell of ring k: 3k(k+1)+1
        a = 6*k - 1
        if isprime(a) and isprime(6*k + 1) and isprime(12*k + 5):
            values.append(3*k*(k-1) + 2)
            if len(values) == target: break
        if isprime(a) and isprime(6*k + 5) and isprime(12*k - 7):
            values.append(3*k*(k+1) + 1)
            if len(values) == target: break
        k += 1
    print(values[target - 1])

solve()
