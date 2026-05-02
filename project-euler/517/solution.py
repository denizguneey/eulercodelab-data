import math

kMod = 1000000007

def small_primes_up_to(n):
    is_prime = [True] * (n + 1)
    if n >= 0: is_prime[0] = False
    if n >= 1: is_prime[1] = False
    for p in range(2, int(math.isqrt(n)) + 1):
        if is_prime[p]:
            for m in range(p * p, n + 1, p):
                is_prime[m] = False
    return [i for i in range(2, n + 1) if is_prime[i]]

def segmented_primes(low, high_exclusive):
    if high_exclusive <= low:
        return []
    root = math.isqrt(high_exclusive - 1) + 1
    base_primes = small_primes_up_to(root)
    
    size = high_exclusive - low
    is_prime = [True] * size
    
    for p in base_primes:
        start = (low + p - 1) // p * p
        if start < p * p:
            start = p * p
        for x in range(start, high_exclusive, p):
            is_prime[x - low] = False
            
    if low == 0:
        is_prime[0] = False
        if size > 1: is_prime[1] = False
    elif low == 1:
        is_prime[0] = False
        
    primes = []
    for i in range(size):
        if is_prime[i]:
            primes.append(low + i)
    return primes

def ceil_k_sqrt_n(n, k):
    target = k * k * n
    x = math.isqrt(target)
    if x * x == target:
        return x
    return x + 1

def nCk_mod(n, k, fact, invfact):
    if k < 0 or k > n:
        return 0
    return (fact[n] * invfact[k] % kMod) * invfact[n - k] % kMod

def G_mod(n, fact, invfact):
    k_max = math.isqrt(n)
    total = 0
    for k in range(k_max + 1):
        ceil_term = ceil_k_sqrt_n(n, k)
        m = n - ceil_term + k
        if m < k:
            continue
        total = (total + nCk_mod(m, k, fact, invfact)) % kMod
    return total

def solve_sum_primes(low_exclusive, high_exclusive):
    max_n = high_exclusive - 1
    fact = [1] * (max_n + 1)
    for i in range(1, max_n + 1):
        fact[i] = (fact[i - 1] * i) % kMod
        
    invfact = [1] * (max_n + 1)
    invfact[max_n] = pow(fact[max_n], kMod - 2, kMod)
    for i in range(max_n, 0, -1):
        invfact[i - 1] = (invfact[i] * i) % kMod
        
    primes = segmented_primes(low_exclusive + 1, high_exclusive)
    total = 0
    for p in primes:
        total = (total + G_mod(p, fact, invfact)) % kMod
    return total

def solve():
    low = 10000000
    high = 10010000
    ans = solve_sum_primes(low, high)
    return str(ans)

if __name__ == '__main__':
    print(solve())
