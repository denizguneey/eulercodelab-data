import math
import sys

# Increase recursion depth if needed
sys.setrecursionlimit(20000)

class Solver:
    def __init__(self, limit):
        self.limit_exclusive = limit
        self.max_prime = int(math.isqrt(limit - 1))
        
        self.primes_desc = []
        self.spf = []
        self.factors_mod3_of_p_minus_1 = []
        self.residue_mod3 = []
        self.included_primes = []
        self.answer = 0

    def build_primes_and_spf(self):
        self.spf = list(range(self.max_prime + 1))
        for i in range(2, math.isqrt(self.max_prime) + 1):
            if self.spf[i] != i:
                continue
            for j in range(i * i, self.max_prime + 1, i):
                if self.spf[j] == j:
                    self.spf[j] = i
                    
        primes_asc = [i for i in range(2, self.max_prime + 1) if self.spf[i] == i]
        self.primes_desc = primes_asc[::-1]
        
        self.factors_mod3_of_p_minus_1 = [[] for _ in range(self.max_prime + 1)]
        for p in primes_asc:
            x = p - 1
            vec = self.factors_mod3_of_p_minus_1[p]
            while x > 1:
                q = self.spf[x]
                cnt = 0
                while x % q == 0:
                    x //= q
                    cnt += 1
                cnt %= 3
                if cnt != 0:
                    vec.append((q, cnt))
                    
        self.residue_mod3 = [0] * (self.max_prime + 1)

    def apply_factors(self, p, sign):
        for q, e in self.factors_mod3_of_p_minus_1[p]:
            v = self.residue_mod3[q]
            if sign > 0:
                v += e
            else:
                v -= e
            v %= 3
            if v < 0:
                v += 3
            self.residue_mod3[q] = v

    def multiplier_sum_rec(self, pos, remaining):
        if pos == len(self.included_primes):
            return 1
            
        p = self.included_primes[pos]
        p3 = p * p * p
        
        total = 0
        mul = 1
        
        while mul <= remaining:
            next_remaining = remaining // mul
            total += mul * self.multiplier_sum_rec(pos + 1, next_remaining)
            
            if mul > remaining // p3:
                break
            mul *= p3
            
        return total

    def add_solution(self, base_n):
        if base_n <= 1 or base_n >= self.limit_exclusive:
            return
            
        remaining = (self.limit_exclusive - 1) // base_n
        mul_sum = self.multiplier_sum_rec(0, remaining)
        self.answer += base_n * mul_sum

    def dfs(self, idx, current_n):
        i = idx
        npr = len(self.primes_desc)
        
        while i < npr:
            p = self.primes_desc[i]
            c = self.residue_mod3[p]
            if c != 0:
                break
                
            min_include = p * p
            if current_n * min_include < self.limit_exclusive:
                break
            i += 1
            
        if i >= npr:
            self.add_solution(current_n)
            return
            
        p = self.primes_desc[i]
        c = self.residue_mod3[p]
        
        if c == 0:
            self.dfs(i + 1, current_n)
            
            e0 = 2
            power = p ** e0
            if current_n * power < self.limit_exclusive:
                self.apply_factors(p, +1)
                self.included_primes.append(p)
                self.dfs(i + 1, current_n * power)
                self.included_primes.pop()
                self.apply_factors(p, -1)
            return
            
        m = (2 + c) % 3
        e0 = 3 if m == 0 else m
        power = p ** e0
        if current_n * power >= self.limit_exclusive:
            return
            
        self.apply_factors(p, +1)
        self.included_primes.append(p)
        self.dfs(i + 1, current_n * power)
        self.included_primes.pop()
        self.apply_factors(p, -1)

    def run(self):
        self.build_primes_and_spf()
        self.answer = 0
        self.included_primes = []
        self.dfs(0, 1)
        return self.answer

def solve():
    limit = 10000000000
    solver = Solver(limit)
    ans = solver.run()
    return str(ans)

if __name__ == '__main__':
    print(solve())
