def prime_sieve(n):
    is_prime = [True] * (n + 1)
    if n >= 0: is_prime[0] = False
    if n >= 1: is_prime[1] = False
    
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for q in range(p * p, n + 1, p):
                is_prime[q] = False
        p += 1
        
    primes = [i for i in range(2, n + 1) if is_prime[i]]
    return primes

def icbrt(n):
    lo = 0
    hi = 2000000
    while lo + 1 < hi:
        mid = lo + (hi - lo) // 2
        cube = mid * mid * mid
        if cube <= n:
            lo = mid
        else:
            hi = mid
    return lo

def summatory_cube_full_divisors(n):
    lim = icbrt(n)
    primes = prime_sieve(lim)
    
    total = 0
    
    def dfs(idx, cur):
        nonlocal total
        total += n // cur
        
        for j in range(idx, len(primes)):
            p = primes[j]
            p3 = p * p * p
            
            if cur * p3 > n:
                break
                
            value = cur * p3
            while value <= n:
                dfs(j + 1, value)
                if value > n // p:
                    break
                value *= p
                
    dfs(0, 1)
    return total

def solve():
    return str(summatory_cube_full_divisors(1000000000000000000))

if __name__ == '__main__':
    print(solve())
