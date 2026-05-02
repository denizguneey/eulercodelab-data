import math

def solve():
    n = 100000000
    MOD = 1000000007
    
    is_prime = bytearray(b'\x01' * (n + 1))
    is_prime[0] = is_prime[1] = 0
    
    limit = math.isqrt(n)
    for p in range(2, limit + 1):
        if is_prime[p]:
            is_prime[p * p : n + 1 : p] = bytes((n - p * p) // p + 1)
            
    primes = [i for i, b in enumerate(is_prime) if b]
    M = len(primes)
    
    pi = [0] * (M + 1)
    for i in range(1, M + 1):
        pi[i] = pi[i - 1] + is_prime[i]
        
    cnt = {}
    
    for m in range(1, M + 1):
        pm = primes[m - 1]
        A = (primes[m] - pm) if m < M else (n - pm + 1)
        composites = A - 1 if A >= 1 else 0
        
        u = m
        c = 0
        while u >= 1:
            if not is_prime[u]:
                c += 1
            cnt[c] = cnt.get(c, 0) + 1
            if composites > 0:
                cnt[c + 1] = cnt.get(c + 1, 0) + composites
            if u == 1:
                break
            u = pi[u]
            
    ans = 1
    for x in cnt.values():
        if x > 0:
            ans = (ans * (x % MOD)) % MOD
            
    return str(ans)

if __name__ == '__main__':
    print(solve())
