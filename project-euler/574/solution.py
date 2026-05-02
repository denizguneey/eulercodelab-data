import math

def primes_up_to(n):
    is_prime = [True] * (n + 1)
    if n >= 0: is_prime[0] = False
    if n >= 1: is_prime[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(2, n + 1) if is_prime[i]]

def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def mod_inv(a, mod):
    _, x, _ = egcd(a, mod)
    return x % mod

class DivInfo:
    def __init__(self, D, E, invD_mod_E):
        self.D = D
        self.E = E
        self.invD_mod_E = invD_mod_E

def build_divisors_with_inverses(primes_lt_q):
    P = 1
    for r in primes_lt_q:
        P *= r
        
    divs = [1]
    for r in primes_lt_q:
        divs.extend([d * r for d in divs])
        
    out = []
    for D in divs:
        E = P // D
        invD = mod_inv(D % E, E) if E > 1 else 0
        out.append(DivInfo(D, E, invD))
    return out

def V_of_prime(p, q, primes_lt_q, divs):
    P = 1
    for r in primes_lt_q:
        P *= r
        
    best = float('inf')
    half = (p + 1) // 2
    
    for di in divs:
        D = di.D
        E = di.E
        
        if E == 1:
            A0 = 0
        else:
            t = (p % E) * di.invD_mod_E % E
            A0 = D * t
            
        As = A0
        if As < half:
            need = half - As
            k = (need + P - 1) // P
            As += k * P
        if As < p:
            if As < best: best = As
            
        A = A0
        if A <= p:
            k = (p - A) // P + 1
            A += k * P
        if A % p == 0:
            A += P
            
        if A < best: best = A
        
    return best

def solve():
    n = 3800
    primes = primes_up_to(n)
    all_primes = primes_up_to(5000)
    
    cache = {}
    
    def get_cache(q):
        if q in cache:
            return cache[q]
        
        primes_lt_q = []
        for r in all_primes:
            if r >= q: break
            primes_lt_q.append(r)
            
        divs = build_divisors_with_inverses(primes_lt_q)
        cache[q] = (primes_lt_q, divs)
        return cache[q]
        
    ans = 0
    for p in primes:
        q = next(r for r in all_primes if r * r > p)
        primes_lt_q, divs = get_cache(q)
        ans += V_of_prime(p, q, primes_lt_q, divs)
        
    return str(ans)

if __name__ == '__main__':
    print(solve())
