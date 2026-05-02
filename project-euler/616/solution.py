import math

def is_prime_int(x):
    if x < 2: return False
    if x % 2 == 0: return x == 2
    for d in range(3, math.isqrt(x) + 1, 2):
        if x % d == 0: return False
    return True

def sieve_primes(n):
    is_prime = bytearray(b'\x01' * (n + 1))
    if n >= 0: is_prime[0] = 0
    if n >= 1: is_prime[1] = 0
    for p in range(2, math.isqrt(n) + 1):
        if is_prime[p]:
            is_prime[p * p : n + 1 : p] = bytes((n - p * p) // p + 1)
    return [i for i, b in enumerate(is_prime) if b]

def pow_leq(a, e, limit):
    if a == 1:
        return 1 <= limit
    return (a ** e) <= limit

def pow_exact(a, e):
    return a ** e

def floor_root(n, e):
    lo = 1
    hi = 1000000 + 1
    while lo + 1 < hi:
        mid = lo + (hi - lo) // 2
        if pow_leq(mid, e, n):
            lo = mid
        else:
            hi = mid
    return lo

def solve():
    LIM = 1000000000000
    
    max_e = 1
    while pow_leq(2, max_e + 1, LIM):
        max_e += 1
        
    perfect = []
    for e in range(2, max_e + 1):
        max_a = floor_root(LIM, e)
        for a in range(2, max_a + 1):
            perfect.append(pow_exact(a, e))
            
    perfect = list(set(perfect))
    sum_perfect = sum(perfect)
    
    P_MAX = 1000000
    primes = sieve_primes(P_MAX)
    exp_primes = [e for e in range(2, max_e + 1) if is_prime_int(e)]
    
    sum_primeprime = 0
    for p in primes:
        for e in exp_primes:
            if not pow_leq(p, e, LIM): break
            sum_primeprime += pow_exact(p, e)
            
    ans = sum_perfect - sum_primeprime - 16
    return str(ans)

if __name__ == '__main__':
    print(solve())
