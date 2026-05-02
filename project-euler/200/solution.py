# Problem 200: Find the 200th prime-proof sqube containing "200".
# A sqube is p^2*q^3 or p^3*q^2 for distinct primes p,q.
# Prime-proof: replacing any digit doesn't produce a prime.

from math import isqrt

def solve():
    def sieve_primes(n):
        s = bytearray(b'\x01') * (n+1)
        s[0] = s[1] = 0
        for i in range(2, isqrt(n)+1):
            if s[i]:
                for j in range(i*i, n+1, i): s[j] = 0
        return [i for i in range(n+1) if s[i]]

    def is_prime(n):
        if n < 2: return False
        if n < 4: return True
        if n % 2 == 0 or n % 3 == 0: return False
        i = 5
        while i*i <= n:
            if n % i == 0 or n % (i+2) == 0: return False
            i += 6
        return True

    def contains_200(x):
        while x >= 200:
            if x % 1000 == 200: return True
            x //= 10
        return False

    def is_prime_proof(x):
        s = str(x)
        for i in range(len(s)):
            orig = int(s[i])
            for d in range(10):
                if d == orig: continue
                if i == 0 and d == 0: continue
                candidate = int(s[:i] + str(d) + s[i+1:])
                if is_prime(candidate): return False
        return True

    limit = 10**12
    primes = sieve_primes(isqrt(limit) + 10)
    squbes = set()
    for p in primes:
        p2 = p*p
        if p2 * 8 > limit: break
        for q in primes:
            if q == p: continue
            val = p2 * q * q * q
            if val > limit: break
            squbes.add(val)
    for p in primes:
        p3 = p*p*p
        if p3 * 4 > limit: break
        for q in primes:
            if q == p: continue
            val = p3 * q * q
            if val > limit: break
            squbes.add(val)

    squbes = sorted(squbes)
    count = 0
    for x in squbes:
        if not contains_200(x): continue
        if is_prime_proof(x):
            count += 1
            if count == 200:
                print(x)
                return

solve()
