import math

def distinct_prime_factors(n):
    factors = []
    if n % 2 == 0:
        factors.append(2)
        while n % 2 == 0:
            n //= 2
    p = 3
    while p * p <= n:
        if n % p == 0:
            factors.append(p)
            while n % p == 0:
                n //= p
        p += 2
    if n > 1:
        factors.append(n)
    return factors

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def mod_inverse(a, mod):
    g, x, y = extended_gcd(a, mod)
    if g != 1: return 0
    return x % mod

def crt_pair(a1, m1, a2, m2):
    inv = mod_inverse(m1 % m2, m2)
    t = (((a2 - (a1 % m2)) % m2 + m2) % m2 * inv) % m2
    return a1 + m1 * t

def solve_for_n(n):
    primes = distinct_prime_factors(n)
    roots_by_prime = []
    for p in primes:
        roots = []
        for x in range(1, p):
            if pow(x, 3, p) == 1:
                roots.append(x)
        roots_by_prime.append(roots)

    ans = 0
    def dfs(idx, residue, modulus):
        nonlocal ans
        if idx == len(primes):
            if 1 < residue < n:
                ans += residue
            return
            
        p = primes[idx]
        for root in roots_by_prime[idx]:
            next_residue = crt_pair(residue, modulus, root, p)
            dfs(idx + 1, next_residue, modulus * p)

    dfs(0, 0, 1)
    return ans

def solve():
    n = 13082761331670030
    ans = solve_for_n(n)
    return str(ans)

if __name__ == '__main__':
    print(solve())
