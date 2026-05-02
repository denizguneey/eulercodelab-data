import math
import sys

sys.setrecursionlimit(20000)

def isqrt_u64(n):
    if n == 0: return 0
    return math.isqrt(n)

def icbrt_u64(n):
    if n == 0: return 0
    r = int(math.floor(n**(1/3.0)))
    while (r + 1)**3 <= n:
        r += 1
    while r**3 > n:
        r -= 1
    return r

def iroot4_u64(n):
    if n == 0: return 0
    r = int(math.floor(n**(1/4.0)))
    while (r + 1)**4 <= n:
        r += 1
    while r**4 > n:
        r -= 1
    return r

class PrimeCounter:
    def __init__(self, sieve_limit=5000000):
        self.sieve_limit = sieve_limit
        is_comp = [False] * (sieve_limit + 1)
        self.pi_small = [0] * (sieve_limit + 1)
        self.primes = []
        
        for i in range(2, sieve_limit + 1):
            if not is_comp[i]:
                self.primes.append(i)
                for j in range(i * i, sieve_limit + 1, i):
                    is_comp[j] = True
            self.pi_small[i] = self.pi_small[i - 1] + (1 if not is_comp[i] else 0)
            
        self.pi_cache = {}
        self.phi_cache = {}
        
    def pi(self, n):
        if n <= self.sieve_limit:
            return self.pi_small[n]
        if n in self.pi_cache:
            return self.pi_cache[n]
            
        a = self.pi(iroot4_u64(n))
        b = self.pi(isqrt_u64(n))
        c = self.pi(icbrt_u64(n))
        
        ans = self.phi(n, a) + (b + a - 2) * (b - a + 1) // 2
        
        for i in range(a + 1, b + 1):
            w = n // self.primes[i - 1]
            ans -= self.pi(w)
            if i <= c:
                lim = self.pi(isqrt_u64(w))
                for j in range(i, lim + 1):
                    pj = self.primes[j - 1]
                    ans -= self.pi(w // pj) - (j - 1)
                    
        self.pi_cache[n] = ans
        return ans
        
    def phi(self, x, s):
        if s == 0: return x
        if s == 1: return x - x // 2
        if s == 2: return x - x // 2 - x // 3 + x // 6
        if s == 3: return x - x // 2 - x // 3 - x // 5 + x // 6 + x // 10 + x // 15 - x // 30
        if x <= self.sieve_limit and self.primes[s - 1] >= x:
            return 1
            
        key = (x << 6) ^ s
        if key in self.phi_cache:
            return self.phi_cache[key]
            
        ps = self.primes[s - 1]
        ans = self.phi(x, s - 1) - self.phi(x // ps, s - 1)
        self.phi_cache[key] = ans
        return ans

def S_of(n, pc):
    pi_n = pc.pi(n)
    pi_n_minus2 = pc.pi(n - 2) if n >= 2 else 0
    
    m = n // 2
    even_2prime = m - 1 if m >= 2 else 0
    odd_2prime = pi_n_minus2 - 1 if pi_n_minus2 >= 1 else 0
    
    sum_even_kge3 = (m - 1) * (m - 2) // 2 if m >= 3 else 0
    m2 = (n - 1) // 2 if n >= 1 else 0
    sum_odd_kge3 = (m2 - 1) * (m2 - 2) // 2 if m2 >= 3 else 0
    
    return pi_n + even_2prime + odd_2prime + sum_even_kge3 + sum_odd_kge3

def solve():
    pc = PrimeCounter(5000000)
    f0 = 0
    f1 = 1
    total = 0
    for k in range(2, 45):
        f = f0 + f1
        f0 = f1
        f1 = f
        if k >= 3:
            total += S_of(f, pc)
    return str(total)

if __name__ == '__main__':
    print(solve())
