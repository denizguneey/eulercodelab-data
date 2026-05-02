import math
import random
import multiprocessing

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_prime(n):
    if n < 2: return False
    if n in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37): return True
    if any(n % p == 0 for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)):
        return False

    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1

    def witness(a):
        if a % n == 0: return False
        x = pow(a, d, n)
        if x == 1 or x == n - 1: return False
        for _ in range(1, s):
            x = pow(x, 2, n)
            if x == n - 1: return False
        return True

    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if witness(a): return False
    return True

def pollard_rho(n):
    if n % 2 == 0: return 2
    if n % 3 == 0: return 3
    while True:
        c = random.randint(1, n - 1)
        x = random.randint(0, n - 1)
        y = x
        d = 1
        
        def f(v):
            return (pow(v, 2, n) + c) % n

        while d == 1:
            x = f(x)
            y = f(f(y))
            d = gcd(abs(x - y), n)
            
        if d != n:
            return d

def min_factor_rec(n):
    if n == 1: return 1
    if is_prime(n): return n
    d = pollard_rho(n)
    return min(min_factor_rec(d), min_factor_rec(n // d))

def min_factor(n):
    if n % 2 == 0: return 2
    return min_factor_rec(n)

class Solver:
    def __init__(self, limit, target_num):
        self.limit = limit
        self.target_num = target_num
        self.sum = 0
        self.min_factor_cache = {}

    def get_min_factor(self, n):
        if n in self.min_factor_cache:
            return self.min_factor_cache[n]
        res = min_factor(n)
        self.min_factor_cache[n] = res
        return res

    def dfs(self, n, rn, rs):
        if n * rs > self.limit: return
        if rn == rs:
            self.sum += n
            return
        if rn < rs: return
        if rs == 1: return
        
        p = self.get_min_factor(rs)
        if n % p == 0: return
        
        tmp = rs
        e = 0
        while tmp % p == 0:
            tmp //= p
            e += 1
            
        p_pow = 1
        sigma = 1
        i = 1
        while True:
            if p_pow > self.limit // p: break
            p_pow *= p
            sigma += p_pow
            
            if i >= e:
                n2 = n * p_pow
                if n2 > self.limit: break
                
                rn2 = rn * p_pow
                rs2 = rs * sigma
                g = gcd(rn2, rs2)
                rn2 //= g
                rs2 //= g
                
                if rn2 < rs2: break
                if n2 * rs2 <= self.limit:
                    self.dfs(n2, rn2, rs2)
                    
            i += 1

    def run(self):
        self.dfs(1, self.target_num, 2)
        return self.sum

def worker(args):
    limit, target = args
    solver = Solver(limit, target)
    return solver.run()

def solve(limit=10**18):
    targets = list(range(3, 14, 2))
    pool_args = [(limit, t) for t in targets]
    
    threads = min(multiprocessing.cpu_count(), len(targets))
    if threads > 1:
        with multiprocessing.Pool(threads) as pool:
            results = pool.map(worker, pool_args)
    else:
        results = map(worker, pool_args)
        
    return str(sum(results))

if __name__ == '__main__':
    print(solve())
