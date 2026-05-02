import math

def primes_up_to(n):
    is_composite = bytearray(n + 1)
    primes = []
    
    for i in range(2, n + 1):
        if not is_composite[i]:
            primes.append(i)
        for p in primes:
            v = i * p
            if v > n:
                break
            is_composite[v] = 1
            if i % p == 0:
                break
    return primes

def sum_multiples_in_range(d, left, right):
    if left > right:
        return 0
        
    first = ((left + d - 1) // d) * d
    last = (right // d) * d
    
    if first > last:
        return 0
        
    count = (last - first) // d + 1
    return (first + last) * count // 2

def solve(limit=999966663333):
    sqrt_limit = int(math.sqrt(limit)) + 10
    primes = primes_up_to(sqrt_limit + 100)
    
    # Ensure one prime above sqrt(limit) exists
    candidate = sqrt_limit + 101
    while True:
        is_prime = True
        for p in primes:
            if p * p > candidate:
                break
            if candidate % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
            break
        candidate += 1
        
    total = 0
    for i in range(len(primes) - 1):
        p = primes[i]
        q = primes[i + 1]
        
        p2 = p * p
        if p2 > limit:
            break
            
        q2 = q * q
        left = p2 + 1
        right = min(limit, q2 - 1)
        
        if left > right:
            continue
            
        sum_p = sum_multiples_in_range(p, left, right)
        sum_q = sum_multiples_in_range(q, left, right)
        sum_pq = sum_multiples_in_range(p * q, left, right)
        
        total += sum_p + sum_q - 2 * sum_pq
        
    return str(total)

if __name__ == '__main__':
    print(solve())
