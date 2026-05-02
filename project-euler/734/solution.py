def sieve_primes(n):
    is_prime = bytearray(n + 1)
    for i in range(2, n + 1):
        is_prime[i] = 1
    
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for x in range(p * p, n + 1, p):
                is_prime[x] = 0
        p += 1
        
    primes = [x for x in range(2, n + 1) if is_prime[x]]
    return primes

def solve():
    kMod = 1000000007
    n = 1000000
    k = 999983
    
    bits = 0
    while (1 << bits) <= n:
        bits += 1
    size = 1 << bits
    
    primes = sieve_primes(n)
    
    g = [0] * size
    for p in primes:
        g[p] = 1
        
    for b in range(bits):
        bit = 1 << b
        for mask in range(size):
            if mask & bit:
                v = g[mask] + g[mask ^ bit]
                g[mask] = v if v < kMod else v - kMod
                
    exact = [0] * size
    for mask in range(size):
        exact[mask] = pow(g[mask], k, kMod)
        
    for b in range(bits):
        bit = 1 << b
        for mask in range(size):
            if mask & bit:
                v = exact[mask] - exact[mask ^ bit]
                exact[mask] = v if v >= 0 else v + kMod
                
    answer = 0
    for p in primes:
        answer += exact[p]
        if answer >= kMod:
            answer -= kMod
            
    return str(answer)

if __name__ == "__main__":
    print(solve())
