import math

MOD = 1000000007

def is_prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    for d in range(3, int(math.isqrt(n)) + 1, 2):
        if n % d == 0: return False
    return True

def first_primes_ending7(k):
    out = []
    x = 7
    while len(out) < k:
        if is_prime(x):
            out.append(x)
        x += 10
    return out

def mod_pow(a, e):
    return pow(a, e, MOD)

def solve_k(k):
    primes = first_primes_ending7(k)
    
    p_mod = 1
    phi_mod = 1
    for p in primes:
        p_mod = (p_mod * p) % MOD
        phi_mod = (phi_mod * (p - 1)) % MOD
        
    pattern = [7, 1, 3, 9]
    s = 0
    comb = 1
    
    for t in range(k + 1):
        term = (comb * pattern[t & 3]) % MOD
        if (t & 1) == 0:
            s = (s + term) % MOD
        else:
            s = (s - term + MOD) % MOD
            
        if t < k:
            num = k - t
            inv = mod_pow(t + 1, MOD - 2)
            comb = (comb * num) % MOD
            comb = (comb * inv) % MOD
            
    inner = (5 * phi_mod + s) % MOD
    return (p_mod * inner) % MOD

def solve():
    return str(solve_k(97))

if __name__ == "__main__":
    print(solve())
