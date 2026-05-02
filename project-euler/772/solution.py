MOD = 1000000007

def odd_sieve_primes(n):
    if n < 2: return []
    if n == 2: return [2]
    
    m = (n - 1) // 2
    composite = bytearray(m)
    
    i = 0
    while (2 * i + 3) * (2 * i + 3) <= n:
        if not composite[i]:
            p = 2 * i + 3
            j = (p * p - 3) // 2
            while j < m:
                composite[j] = 1
                j += p
        i += 1
        
    primes = [2]
    for i in range(m):
        if not composite[i]:
            primes.append(2 * i + 3)
            
    return primes

def lcm_upto_mod(k):
    primes = odd_sieve_primes(k)
    ans = 1
    
    for p in primes:
        pw = p
        limit = k // p
        while pw <= limit:
            pw *= p
        ans = (ans * pw) % MOD
        
    return ans
    
def f_mod(k):
    l = lcm_upto_mod(k)
    return (2 * l) % MOD

def solve():
    return str(f_mod(100**4))

if __name__ == "__main__":
    print(solve())
