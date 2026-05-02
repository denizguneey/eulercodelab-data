import math
import sys

sys.setrecursionlimit(20000)

MOD = 1000000000
MOD2 = 2 * MOD

def pow_mod(base, exp, mod):
    return pow(base, exp, mod)

def mod_norm(x):
    return x % MOD

def sum_a_prefix(m):
    if m <= 0:
        return 0
    pow3 = pow_mod(3, m + 1, MOD2)
    num = (pow3 - 3) % MOD2
    sum3 = num // 2
    
    pow2 = pow_mod(2, m + 1, MOD)
    sum2 = (pow2 - 2) % MOD
    
    res = (sum3 - sum2 - (m % MOD)) % MOD
    return res

class Mertens:
    def __init__(self, n):
        self.limit = int(math.pow(n, 2.0 / 3.0)) + 1
        if self.limit < 1:
            self.limit = 1
        self.mu = [0] * (self.limit + 1)
        self.prefix = [0] * (self.limit + 1)
        self.cache = {}
        self.init_mu()
        
    def init_mu(self):
        primes = []
        is_comp = bytearray(self.limit + 1)
        self.mu[1] = 1
        for i in range(2, self.limit + 1):
            if not is_comp[i]:
                primes.append(i)
                self.mu[i] = -1
            for p in primes:
                v = i * p
                if v > self.limit:
                    break
                is_comp[v] = 1
                if i % p == 0:
                    self.mu[v] = 0
                    break
                else:
                    self.mu[v] = -self.mu[i]
        
        for i in range(1, self.limit + 1):
            self.prefix[i] = self.prefix[i - 1] + self.mu[i]
            
    def get(self, n):
        if n <= self.limit:
            return self.prefix[n]
        if n in self.cache:
            return self.cache[n]
        res = 1
        l = 2
        while l <= n:
            q = n // l
            r = n // q
            res -= (r - l + 1) * self.get(q)
            l = r + 1
        self.cache[n] = res
        return res

def compute_t_mod(n):
    mertens = Mertens(n)
    segs = []
    l = 1
    while l <= n:
        q = n // l
        r = n // q
        segs.append((l, r, q))
        l = r + 1
        
    total = 1 % MOD
    for l_val, r_val, q_val in segs:
        sum_a = (sum_a_prefix(r_val) - sum_a_prefix(l_val - 1)) % MOD
        mq_mod = mertens.get(q_val) % MOD
        contrib = (sum_a * mq_mod) % MOD
        total = (total + contrib) % MOD
        
    return total

def solve():
    n = 10000000000
    ans = compute_t_mod(n)
    return str(ans)
    
if __name__ == '__main__':
    print(solve())
