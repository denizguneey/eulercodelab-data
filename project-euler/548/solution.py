import math

kLimit = 10**16

def gcd_u64(a, b):
    return math.gcd(a, b)

def is_prime_u64(n):
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

rng_state = 0x123456789abcdef0

def splitmix64():
    global rng_state
    rng_state = (rng_state + 0x9e3779b97f4a7c15) & 0xffffffffffffffff
    z = rng_state
    z = (z ^ (z >> 30)) * 0xbf58476d1ce4e5b9 & 0xffffffffffffffff
    z = (z ^ (z >> 27)) * 0x94d049bb133111eb & 0xffffffffffffffff
    return z ^ (z >> 31)

def rand_u64(lo, hi):
    r = splitmix64()
    if hi > lo:
        return lo + (r % (hi - lo + 1))
    return lo

def pollard_rho(n):
    if (n & 1) == 0: return 2
    if n % 3 == 0: return 3
    
    while True:
        c = rand_u64(1, n - 1)
        x = rand_u64(0, n - 1)
        y = x
        d = 1
        
        def f(v):
            return (v * v + c) % n
            
        while d == 1:
            x = f(x)
            y = f(f(y))
            diff = x - y if x > y else y - x
            d = gcd_u64(diff, n)
            
        if d != n: return d

def factor_rec(n, out):
    if n == 1: return
    if is_prime_u64(n):
        out.append(n)
        return
    d = pollard_rho(n)
    factor_rec(d, out)
    factor_rec(n // d, out)

def exponent_pattern(n):
    if n == 1: return ()
    fac = []
    factor_rec(n, fac)
    fac.sort()
    
    exps = []
    i = 0
    while i < len(fac):
        j = i
        while j < len(fac) and fac[j] == fac[i]:
            j += 1
        exps.append(j - i)
        i = j
    exps.sort(reverse=True)
    return tuple(exps)

def binom(n, k):
    if k < 0 or k > n: return 0
    k = min(k, n - k)
    r = 1
    for i in range(1, k + 1):
        r = r * (n - k + i) // i
    return r

def g_from_pattern(exps, limit):
    if not exps: return 1
    omega = sum(exps)
    
    C = [[0] * (omega + 1) for _ in range(omega + 1)]
    C[0][0] = 1
    for n in range(1, omega + 1):
        C[n][0] = C[n][n] = 1
        for k in range(1, n):
            C[n][k] = C[n - 1][k - 1] + C[n - 1][k]
            
    total = [0] * (omega + 1)
    for k in range(1, omega + 1):
        prod = 1
        for a in exps:
            prod *= binom(a + k - 1, k - 1)
        total[k] = prod
        
    g = 0
    for k in range(1, omega + 1):
        fk = 0
        for i in range(1, k + 1):
            term = C[k][i] * total[i]
            if ((k - i) & 1) != 0:
                fk -= term
            else:
                fk += term
        g += fk
        if g > limit: return limit + 1
    return g

class Enumerator:
    def __init__(self):
        self.primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
        self.pattern_cache = {}
        self.solutions = set()
        self.cur = []
        
    def cached_pattern(self, n):
        if n in self.pattern_cache:
            return self.pattern_cache[n]
        p = exponent_pattern(n)
        self.pattern_cache[n] = p
        return p
        
    def dfs(self, last_exp, min_n):
        t_cur = tuple(self.cur)
        g = g_from_pattern(t_cur, kLimit)
        if g > kLimit: return
        
        if g >= min_n:
            pat = self.cached_pattern(g)
            if pat == t_cur:
                self.solutions.add(g)
                
        idx = len(self.cur)
        if idx >= len(self.primes): return
        p = self.primes[idx]
        
        pow_val = 1
        for e in range(1, last_exp + 1):
            pow_val *= p
            next_min = min_n * pow_val
            if next_min > kLimit: break
            self.cur.append(e)
            self.dfs(e, next_min)
            self.cur.pop()
            
    def run(self):
        self.cur = []
        self.dfs(53, 1)
        return sorted(list(self.solutions))

def solve():
    en = Enumerator()
    sols = en.run()
    return str(sum(sols))

if __name__ == '__main__':
    print(solve())
