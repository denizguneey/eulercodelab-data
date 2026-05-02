import math
import heapq

def isqrt(n):
    if n < 0: return 0
    return int(math.sqrt(n))

def get_primes(limit):
    if limit < 2: return []
    is_prime = bytearray([1]) * (limit + 1)
    is_prime[0] = is_prime[1] = 0
    for p in range(2, isqrt(limit) + 1):
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = 0
    return [p for p in range(2, limit + 1) if is_prime[p]]

def get_factors(n, primes):
    factors = []
    m = n
    for p in primes:
        if p * p > m: break
        if m % p == 0:
            count = 0
            while m % p == 0:
                m //= p
                count += 1
            factors.append((p, count))
    if m > 1:
        factors.append((m, 1))
    return factors

def get_divisors_leq(factors, idx, current, limit, out):
    if idx == len(factors):
        out.append(current)
        return
        
    p, exponent = factors[idx]
    power = 1
    for e in range(exponent + 1):
        if current > limit // power:
            break
        get_divisors_leq(factors, idx + 1, current * power, limit, out)
        if e == exponent or power > limit // p:
            break
        power *= p

def solve(target=150000):
    heap = [] # will store negative values to act as max-heap
    active = set()
    
    primes = [2, 3]
    
    def ensure_primes(limit):
        while primes[-1] < limit:
            cand = primes[-1] + 2
            while True:
                is_p = True
                for p in primes:
                    if p * p > cand: break
                    if cand % p == 0:
                        is_p = False
                        break
                if is_p:
                    primes.append(cand)
                    break
                cand += 2
                
    p = 1
    while True:
        n = p * p + 1
        root = isqrt(n)
        ensure_primes(root + 1)
        
        factors = get_factors(n, primes)
        
        divisors = []
        get_divisors_leq(factors, 0, 1, root, divisors)
        
        for d in divisors:
            e = n // d
            value = p * (p + d) * (p + e)
            
            if len(heap) < target:
                if value not in active:
                    heapq.heappush(heap, -value)
                    active.add(value)
                continue
                
            current_max = -heap[0]
            if value >= current_max:
                continue
            if value in active:
                continue
                
            removed = -heapq.heappop(heap)
            active.remove(removed)
            
            heapq.heappush(heap, -value)
            active.add(value)
            
        if len(heap) == target:
            next_p = p + 1
            lower_bound = next_p * (next_p + 1) * (next_p + 1)
            if lower_bound > -heap[0]:
                return str(-heap[0])
                
        p += 1

if __name__ == '__main__':
    print(solve())
