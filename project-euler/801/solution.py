import random
import math

MOD = 993353399

def is_prime_u64(n):
    if n < 2:
        return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if n == p:
            return True
        if n % p == 0:
            return False
            
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
        
    witnesses = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
    for a in witnesses:
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        comp = True
        for _ in range(1, s):
            x = (x * x) % n
            if x == n - 1:
                comp = False
                break
        if comp:
            return False
    return True

def pollard_rho(n):
    if n % 2 == 0:
        return 2
    while True:
        c = random.randint(2, n - 2)
        x = random.randint(2, n - 2)
        y = x
        d = 1
        
        f = lambda v: (v * v + c) % n
        
        while d == 1:
            x = f(x)
            y = f(f(y))
            diff = x - y if x > y else y - x
            d = math.gcd(diff, n)
            
        if d != n:
            return d

def factor_rec(n, out):
    if n == 1:
        return
    if is_prime_u64(n):
        out.append(n)
        return
    d = pollard_rho(n)
    factor_rec(d, out)
    factor_rec(n // d, out)

def f_prime_mod(p):
    n = p - 1
    fac = []
    factor_rec(n, fac)
    fac.sort()
    
    expo = {}
    for q in fac:
        expo[q] = expo.get(q, 0) + 1
        
    h = 1
    for q, e in expo.items():
        qm = q % MOD
        q_e_minus_1 = pow(qm, e - 1, MOD)
        q_e = pow(qm, e, MOD)
        q_e_plus_1 = pow(qm, e + 1, MOD)
        
        t = (q_e_plus_1 + q_e - 1) % MOD
        if t < 0:
            t += MOD
            
        term = (q_e_minus_1 * t) % MOD
        h = (h * term) % MOD
        
    nm = n % MOD
    n2 = (nm * nm) % MOD
    nh = (nm * h) % MOD
    
    f = (n2 + nh) % MOD
    if f < 0:
        f += MOD
    return f

def primes_in_range(lo, hi):
    out = []
    if hi < 2 or lo > hi:
        return out
    if lo <= 2 <= hi:
        out.append(2)
        
    start = 3 if lo <= 3 else lo
    if start % 2 == 0:
        start += 1
        
    for x in range(start, hi + 1, 2):
        if is_prime_u64(x):
            out.append(x)
    return out

def S_mod(M, N):
    primes = primes_in_range(M, N)
    ans = 0
    for p in primes:
        ans = (ans + f_prime_mod(p)) % MOD
    return ans

def solve():
    return str(S_mod(10000000000000000, 10000000000000000 + 1000000))

if __name__ == "__main__":
    random.seed(0xC0FFEE)
    print(solve())
