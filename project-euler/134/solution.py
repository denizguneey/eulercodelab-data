# Problem 134: Prime pair connection
# For consecutive primes p1, p2 (5 <= p1 <= 10^6), find S = smallest number
# ending in p1 that is divisible by p2. Sum all S values.

from sympy import sieve

def solve():
    limit = 1000000
    primes = list(sieve.primerange(5, limit + 200000))
    total = 0
    for i in range(len(primes) - 1):
        p1 = primes[i]
        p2 = primes[i + 1]
        if p1 >= limit: break
        mod = 1
        x = p1
        while x > 0: mod *= 10; x //= 10
        inv = pow(p2 % mod, -1, mod)
        k = (p1 * inv) % mod
        total += p2 * k
    print(total)

solve()
