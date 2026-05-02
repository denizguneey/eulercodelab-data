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

def inverse_mod_10(p):
    return pow(10, -1, p)

def solve(prime_limit=10000000):
    primes = primes_up_to(prime_limit - 1)
    
    total_sum = 0
    for p in primes:
        if p == 2 or p == 5:
            continue
        total_sum += inverse_mod_10(p)
        
    return str(total_sum)

if __name__ == '__main__':
    print(solve())
