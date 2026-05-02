def extended_gcd(a, b):
    if b == 0:
        return 1, 0, a
    x1, y1, g = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return x, y, g

def mod_inverse(a, mod):
    a %= mod
    if a == 0:
        return 0
    x, y, g = extended_gcd(a, mod)
    if g != 1:
        return 0
    res = x % mod
    if res < 0:
        res += mod
    return res

def small_primes_up_to(n):
    is_prime = [True] * (n + 1)
    if n >= 0: is_prime[0] = False
    if n >= 1: is_prime[1] = False
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for m in range(p * p, n + 1, p):
                is_prime[m] = False
    return [i for i in range(2, n + 1) if is_prime[i]]

def segmented_primes(low, high_exclusive):
    if high_exclusive <= low:
        return []
    high_inclusive = high_exclusive - 1
    root = int(high_inclusive ** 0.5)
    
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

def D(a, b, k):
    m = k - 1
    primes = segmented_primes(a, a + b)
    total = 0
    for p in primes:
        total += mod_inverse(m, p)
    return total

def solve():
    a = 1000000000
    b = 100000
    k = 100000
    ans = D(a, b, k)
    return str(ans)

if __name__ == '__main__':
    print(solve())
