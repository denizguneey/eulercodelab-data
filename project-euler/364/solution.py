def mod_pow(base, exp, mod):
    return pow(base, exp, mod)

def comfortable_arrangements_mod(n):
    mod = 100000007
    fact = [1] * (n + 2)
    for i in range(1, n + 2):
        fact[i] = (fact[i - 1] * i) % mod
        
    inv_fact = [1] * (n + 2)
    inv_fact[n + 1] = mod_pow(fact[n + 1], mod - 2, mod)
    for i in range(n + 1, 0, -1):
        inv_fact[i - 1] = (inv_fact[i] * i) % mod
        
    pow2 = [1] * (n + 1)
    for i in range(1, n + 1):
        pow2[i] = (pow2[i - 1] * 2) % mod
        
    boundary_sum = [0, 1, 2]
    boundary_mult = [1, 2, 1]
    
    total = 0
    for m in range(1, n + 1):
        fm = fact[m]
        fm1 = fact[m - 1]
        
        for t in range(3):
            s = boundary_sum[t]
            mult = boundary_mult[t]
            
            g2 = n - (2 * m - 1 + s)
            if g2 < 0 or g2 > (m - 1):
                continue
                
            comb = fm1
            comb = (comb * inv_fact[g2]) % mod
            comb = (comb * inv_fact[m - 1 - g2]) % mod
            
            term = (mult * comb) % mod
            term = (term * fm) % mod
            term = (term * fm1) % mod
            term = (term * fact[s + g2]) % mod
            term = (term * pow2[g2]) % mod
            
            total = (total + term) % mod
            
    return str(total)

def solve():
    return comfortable_arrangements_mod(1000000)

if __name__ == '__main__':
    print(solve())
