import math

MOD = 1000000000

def sieve_primes(n):
    is_prime = bytearray(b'\x01' * (n + 1))
    is_prime[0] = is_prime[1] = 0
    for p in range(2, math.isqrt(n) + 1):
        if is_prime[p]:
            is_prime[p * p : n + 1 : p] = bytes((n - p * p) // p + 1)
    return [i for i, b in enumerate(is_prime) if b]

def solve():
    F = [0] * 25
    F[1] = 1
    F[2] = 1
    for i in range(3, 25):
        F[i] = F[i - 1] + F[i - 2]
        
    K = F[24]
    
    primes = sieve_primes(K)
    dp = [0] * (K + 1)
    dp[0] = 1
    
    for p in primes:
        for k in range(p, K + 1):
            dp[k] = (dp[k] + p * dp[k - p]) % MOD
            
    ans = 0
    for i in range(2, 25):
        ans = (ans + dp[F[i]]) % MOD
        
    return f"{ans:09d}"

if __name__ == '__main__':
    print(solve())
