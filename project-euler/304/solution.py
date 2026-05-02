def sieve_base_primes(limit):
    is_prime = bytearray(limit + 1)
    for i in range(2, limit + 1):
        is_prime[i] = 1
        
    p = 2
    while p * p <= limit:
        if is_prime[p]:
            for q in range(p * p, limit + 1, p):
                is_prime[q] = 0
        p += 1
        
    primes = [p for p in range(2, limit + 1) if is_prime[p]]
    return primes

def first_primes_after(start, count):
    base_limit = 10000000 + 1000000  # sqrt(10^14) is 10^7
    base_primes = sieve_base_primes(base_limit)
    
    segment_size = 4000000
    out = []
    
    low = start + 1
    while len(out) < count:
        high = low + segment_size - 1
        is_prime = bytearray(segment_size)
        for i in range(segment_size):
            is_prime[i] = 1
            
        for p in base_primes:
            if p * p > high:
                break
                
            first = ((low + p - 1) // p) * p
            if first < p * p:
                first = p * p
                
            start_idx = first - low
            for x in range(start_idx, segment_size, p):
                is_prime[x] = 0
                
        for i in range(segment_size):
            if len(out) >= count:
                break
            if is_prime[i]:
                value = low + i
                if value >= 2:
                    out.append(value)
                    
        low = high + 1
        
    return out

def fib_pair_mod(n, mod):
    if n == 0:
        return (0, 1 % mod)
        
    a, b = fib_pair_mod(n >> 1, mod)
    two_b = (2 * b) % mod
    c = (a * ((two_b + mod - a) % mod)) % mod
    d = (a * a + b * b) % mod
    
    if (n & 1) == 0:
        return (c, d)
    return (d, (c + d) % mod)

def solve(start=100000000000000, count=100000, mod=1234567891011):
    primes = first_primes_after(start, count)
    total_sum = 0
    for p in primes:
        total_sum += fib_pair_mod(p, mod)[0]
        if total_sum >= mod:
            total_sum %= mod
            
    return str(total_sum % mod)

if __name__ == '__main__':
    print(solve())
