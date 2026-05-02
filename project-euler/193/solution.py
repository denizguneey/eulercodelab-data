# Problem 193: Squarefree Numbers
# Count squarefree numbers below 2^50 using Mobius function.

from math import isqrt

def solve():
    limit = 2**50
    max_k = isqrt(limit)
    # Linear sieve for Mobius function
    mu = [0]*(max_k+1)
    mu[1] = 1
    primes = []
    is_composite = bytearray(max_k+1)
    for i in range(2, max_k+1):
        if not is_composite[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i*p > max_k: break
            is_composite[i*p] = 1
            if i % p == 0:
                mu[i*p] = 0
                break
            mu[i*p] = -mu[i]
    count = 0
    for k in range(1, max_k+1):
        if mu[k] != 0:
            count += mu[k] * (limit // (k*k))
    print(count)

solve()
