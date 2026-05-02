kMod = 1000000007

def build_linear_sieve(limit):
    spf = [0] * (limit + 1)
    pi = [0] * (limit + 1)
    if limit < 2: return spf, pi
    
    primes = []
    
    for i in range(2, limit + 1):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
        
        for p in primes:
            v = i * p
            if v > limit: break
            spf[v] = p
            if p == spf[i]: break
            
    prime_count = 0
    for x in range(1, limit + 1):
        if x >= 2 and spf[x] == x:
            prime_count += 1
        pi[x] = prime_count
        
    return spf, pi

def fwht_xor(a):
    n = len(a)
    length = 1
    while length < n:
        step = length << 1
        for i in range(0, n, step):
            for j in range(length):
                u = a[i + j]
                v = a[i + j + length]
                a[i + j] = (u + v) % kMod
                a[i + j + length] = (u - v + kMod) % kMod
        length <<= 1

def solve_losing_positions(n, k):
    limit = n - 1
    spf, pi = build_linear_sieve(limit)
    
    max_index = max(1, pi[limit])
    counts = [0] * (max_index + 1)
    
    counts[0] = limit // 2
    counts[1] = 1
    
    for x in range(3, limit + 1, 2):
        p = spf[x]
        idx = pi[p]
        counts[idx] += 1
        
    size = 1
    while size < len(counts):
        size <<= 1
        
    transformed = [0] * size
    for i in range(len(counts)):
        transformed[i] = counts[i] % kMod
        
    fwht_xor(transformed)
    
    for i in range(size):
        transformed[i] = pow(transformed[i], k, kMod)
        
    fwht_xor(transformed)
    
    inv_size = pow(size % kMod, kMod - 2, kMod)
    return (transformed[0] * inv_size) % kMod

def solve():
    return str(solve_losing_positions(10000000, 10000000))

if __name__ == '__main__':
    print(solve())
