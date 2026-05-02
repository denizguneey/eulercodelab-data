import sys
import multiprocessing
import multiprocessing.pool
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_prime(n):
    if n < 2: return False
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for p in small_primes:
        if n == p: return True
        if n % p == 0: return False
        
    d = n - 1
    s = 0
    while (d & 1) == 0:
        d >>= 1
        s += 1
        
    def witness(a):
        if a % n == 0: return False
        x = pow(a, d, n)
        if x == 1 or x == n - 1: return False
        for _ in range(1, s):
            x = (x * x) % n
            if x == n - 1: return False
        return True
        
    bases = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
    for a in bases:
        if witness(a): return False
    return True

import random

def pollard_rho(n):
    if n & 1 == 0: return 2
    if n % 3 == 0: return 3
    
    while True:
        c = random.randint(1, n - 1)
        x = random.randint(0, n - 1)
        y = x
        d = 1
        
        def f(v):
            return (v * v + c) % n
            
        while d == 1:
            x = f(x)
            y = f(f(y))
            d = gcd(abs(x - y), n)
            
        if d != n: return d

def factor(n, fac):
    if n == 1: return
    if is_prime(n):
        fac.append(n)
        return
    d = pollard_rho(n)
    factor(d, fac)
    factor(n // d, fac)

class FactorCache:
    def __init__(self):
        self.mp = {}
        
    def get(self, n):
        if n in self.mp: return self.mp[n]
        f = []
        if n > 1:
            tmp = []
            factor(n, tmp)
            f = sorted(list(set(tmp)))
        self.mp[n] = f
        return f

def v3(x):
    c = 0
    while x % 3 == 0:
        x //= 3
        c += 1
    return c

def sigma_prime_power(p, e, p_pow):
    next_pow = p_pow * p
    return (next_pow - 1) // (p - 1)

class SolverA:
    def __init__(self, A, limit, maxv3, validate=False):
        self.A = A
        self.limit = limit
        self.maxv3 = maxv3
        self.validate = validate
        self.sum_m = 0
        self.visited_m = set()
        self.cache = FactorCache()
        self.used = []
        
    def dfs(self, m, num, den, v3sig, sigma_m):
        if m > self.limit: return
        if m in self.visited_m: return
        self.visited_m.add(m)
        
        if den == 1 and v3sig <= self.maxv3:
            self.sum_m += m
            
        cand = self.cache.get(num)[:]
        cand.append(2)
        cand = sorted(list(set(cand)))
        
        for p in cand:
            if p == 3: continue
            if p in self.used: continue
            
            p_pow = p
            e = 1
            while True:
                if m * p_pow > self.limit: break
                
                sig = sigma_prime_power(p, e, p_pow)
                v3f = v3(sig)
                if v3sig + v3f <= self.maxv3:
                    denom_factor = p_pow
                    sig_factor = sig
                    
                    num1 = num
                    den1 = den
                    
                    g1 = gcd(num1, denom_factor)
                    num1 //= g1
                    denom_factor //= g1
                    
                    g2 = gcd(sig_factor, den1)
                    sig_factor //= g2
                    den1 //= g2
                    
                    new_num = num1 * sig_factor
                    new_den = den1 * denom_factor
                    
                    new_m = m * p_pow
                    new_sigma_m = sigma_m * sig
                    
                    self.used.append(p)
                    self.dfs(new_m, new_num, new_den, v3sig + v3f, new_sigma_m)
                    self.used.pop()
                    
                if p_pow > self.limit // p: break
                p_pow *= p
                e += 1

def solve_one(args):
    a, p3, N = args
    limit = N // p3
    t = p3 * 3 - 1
    A = t // 2
    solver = SolverA(A, limit, a - 1, False)
    solver.dfs(1, A, 1, 0, 1)
    return p3 * solver.sum_m

def compute_T(N):
    tasks = []
    pow3 = 1
    a = 1
    while True:
        pow3 *= 3
        if pow3 > N: break
        tasks.append((a, pow3, N))
        a += 1
        
    threads = multiprocessing.cpu_count() or 1
    total = 0
    if threads <= 1 or len(tasks) <= 1:
        for t in tasks:
            total += solve_one(t)
    else:
        with multiprocessing.Pool(threads) as pool:
            results = pool.map(solve_one, tasks)
        total = sum(results)
    return total

def solve():
    N = 100000000000000
    ans = compute_T(N)
    return str(ans)

if __name__ == '__main__':
    print(solve())
