import math

TARGET_COUNT = 1000000
MOD = 123454321
PRIME_LIMIT = 1000000

def sieve_primes(n):
    is_prime = bytearray(b'\x01' * (n + 1))
    is_prime[0] = is_prime[1] = 0
    for i in range(2, math.isqrt(n) + 1):
        if is_prime[i]:
            is_prime[i * i : n + 1 : i] = bytes((n - i * i) // i + 1)
    return [i for i, b in enumerate(is_prime) if b]

class Enumerator:
    def __init__(self, primes, log_primes, need_factors, limit_n):
        self.primes = primes
        self.log_primes = log_primes
        self.need_factors = need_factors
        self.limit_n = limit_n
        self.log_limit_n = math.log(limit_n)
        self.values = []

    def dfs(self, i, used, n):
        if i >= len(self.primes):
            return False
            
        if used < self.need_factors:
            lb = math.log(n) + (self.need_factors - used) * self.log_primes[i]
            if lb > self.log_limit_n + 1e-12:
                return False
                
        if used >= self.need_factors:
            self.values.append(n)
            
        j = i
        while j < len(self.primes):
            p = self.primes[j]
            if n * p > self.limit_n:
                break
            if not self.dfs(j, used + 1, n * p):
                break
            j += 1
            
        return True

def solve():
    primes = sieve_primes(PRIME_LIMIT)
    log_primes = [math.log(p) for p in primes]
    
    c = 1
    n_limit = 3
    values = []
    
    while True:
        e = Enumerator(primes, log_primes, c, n_limit)
        e.dfs(0, 0, 1)
        values = e.values
        if len(values) >= TARGET_COUNT:
            break
        c += 1
        n_limit *= 3
        
    values.sort()
    x = values[TARGET_COUNT - 1]
    
    for _ in range(c, TARGET_COUNT):
        x = (x * 2) % MOD
        
    return str(x)

if __name__ == '__main__':
    print(solve())
