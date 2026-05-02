def normalize_mod(x, mod_val):
    return x % mod_val

def pow_mod(base, exp, mod_val):
    return pow(base, exp, mod_val)

def inverse_mod_prime(a, p):
    return pow(a, p - 2, p)

def factorial_mod_small(n, p):
    f = 1 % p
    for i in range(1, n + 1):
        f = (f * (i % p)) % p
    return f

def compute_A_mod_prime(p, max_n):
    values = [0] * (max_n + 1)
    comb = [0] * (max_n + 1)
    comb[0] = 1
    
    fact = 1 % p
    
    for n in range(max_n + 1):
        if n > 0:
            comb[n] = 1
            for k in range(n - 1, 0, -1):
                comb[k] = (comb[k] + comb[k - 1]) % p
                
            if n < p:
                fact = (fact * n) % p
            else:
                fact = 0
                
        current = fact
        for k in range(n):
            current = (current + comb[k] * values[k]) % p
            
        values[n] = current
        
    return values

def reduced_index_for_prime(n, p):
    if n < p:
        return n
    period = p * (p - 1)
    return p + ((n - p) % period)

def solve_mod_prime(p, n):
    index = reduced_index_for_prime(n, p)
    A = compute_A_mod_prime(p, index)
    
    n_factorial_mod = 0 if n >= p else factorial_mod_small(n, p)
    return (n_factorial_mod - A[index]) % p

def crt_combine(residues, moduli, full_mod):
    x = 0
    current_modulus = 1
    
    for i in range(len(residues)):
        m = moduli[i]
        a = residues[i]
        
        inv = inverse_mod_prime(current_modulus % m, m)
        t = ((a - x) % m * inv) % m
        x = (x + current_modulus * t) % full_mod
        current_modulus *= m
        
    return x % full_mod

def solve():
    n = 1000000000
    modulus = 77777777
    primes = [7, 11, 73, 101, 137]
    
    residues = []
    for p in primes:
        residues.append(solve_mod_prime(p, n))
        
    ans = crt_combine(residues, primes, modulus)
    return str(ans)

if __name__ == '__main__':
    print(solve())
