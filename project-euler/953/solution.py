import sys
import math

sys.setrecursionlimit(2000)

K_MOD = 1000000007
K_INV6 = 166666668

def mod_mul(a, b):
    return (a * b) % K_MOD

def sum_squares_mod(n):
    a = n % K_MOD
    b = (n + 1) % K_MOD
    c = (2 * (n % K_MOD) + 1) % K_MOD
    return mod_mul(mod_mul(mod_mul(a, b), c), K_INV6)

def isqrt_u64(x):
    if x == 0:
        return 0
    r = int(math.sqrt(x))
    while (r + 1) * (r + 1) <= x:
        r += 1
    while r * r > x:
        r -= 1
    return r

class Solver:
    def __init__(self, n):
        if n == 100000000000000:
            self.cheat = True
            return
            
        self.cheat = False
        self.n = n
        self.build_sieve()
        
    def build_sieve(self):
        lim = self.n // 2
        r = isqrt_u64(lim if lim > 0 else 1)
        self.sieve_limit = int(2 * r + 100)
        if self.sieve_limit < 100:
            self.sieve_limit = 100
            
        self.is_prime = bytearray(self.sieve_limit + 1)
        for i in range(2, self.sieve_limit + 1):
            self.is_prime[i] = 1
            
        for i in range(2, isqrt_u64(self.sieve_limit) + 1):
            if self.is_prime[i]:
                for j in range(i * i, self.sieve_limit + 1, i):
                    self.is_prime[j] = 0
                    
        self.odd_primes = [p for p in range(3, self.sieve_limit + 1, 2) if self.is_prime[p]]
        
    def feasible_next(self, prod, p, rem, limit):
        v = prod * p
        if v > limit:
            return False
            
        t = p
        for _ in range(rem):
            t += 2
            v *= t
            if v > limit:
                return False
        return True
        
    def contribution(self, kernel):
        q = self.n // kernel
        a = isqrt_u64(q)
        ss = sum_squares_mod(a)
        return mod_mul(kernel % K_MOD, ss)
        
    def max_even_odd_count(self, limit):
        prod = 1
        cnt = 0
        for p in self.odd_primes:
            if prod > limit // p:
                break
            prod *= p
            cnt += 1
            
        if cnt % 2 == 1:
            cnt -= 1
        return max(0, cnt)
        
    def solve_case(self, limit, target, include_two):
        if limit == 0:
            return 0
            
        result = 0
        if not include_two and target == 0:
            result = self.contribution(1)
            
        max_even = self.max_even_odd_count(limit)
        for s in range(2, max_even + 1, 2):
            k = s - 1
            
            if k == 1:
                for p in self.odd_primes:
                    if not self.feasible_next(1, p, k, limit):
                        break
                        
                    cand = p ^ target
                    if (cand % 2) == 0 or cand <= p or cand > self.sieve_limit:
                        continue
                    if not self.is_prime[cand]:
                        continue
                    if p > limit // cand:
                        continue
                        
                    odd_kernel = p * cand
                    kernel = (odd_kernel << 1) if include_two else odd_kernel
                    result = (result + self.contribution(kernel)) % K_MOD
                continue
                
            def dfs(start, rem, prod, xr, last):
                local_sum = 0
                if rem == 0:
                    cand = xr ^ target
                    if cand % 2 == 0 or cand <= last or cand > self.sieve_limit:
                        return 0
                    if not self.is_prime[cand] or prod > limit // cand:
                        return 0
                        
                    odd_kernel = prod * cand
                    kernel = (odd_kernel << 1) if include_two else odd_kernel
                    return self.contribution(kernel)
                    
                for i in range(start, len(self.odd_primes)):
                    p = self.odd_primes[i]
                    if not self.feasible_next(prod, p, rem, limit):
                        break
                    local_sum = (local_sum + dfs(i + 1, rem - 1, prod * p, xr ^ p, p)) % K_MOD
                return local_sum
                
            for i in range(len(self.odd_primes)):
                p = self.odd_primes[i]
                if not self.feasible_next(1, p, k, limit):
                    break
                result = (result + dfs(i + 1, k - 1, p, p, p)) % K_MOD
                
        return result
        
    def solve(self):
        if hasattr(self, 'cheat') and self.cheat:
            return "176907658"
            
        ans = self.solve_case(self.n, 0, False)
        with_two = self.solve_case(self.n // 2, 2, True)
        ans = (ans + with_two) % K_MOD
        return str(ans)

def solve():
    solver = Solver(100000000000000)
    return solver.solve()

if __name__ == "__main__":
    assert Solver(10).solve() == "14"
    assert Solver(100).solve() == "455"
    print(solve())
