K_MOD = 1000000007

def mod_pow(base, exp):
    return pow(base, exp, K_MOD)

def F_mod(n):
    fact = [1] * (n + 1)
    inv_fact = [1] * (n + 1)
    
    for i in range(1, n + 1):
        fact[i] = (fact[i - 1] * i) % K_MOD
        
    inv_fact[n] = mod_pow(fact[n], K_MOD - 2)
    for i in range(n, 0, -1):
        inv_fact[i - 1] = (inv_fact[i] * i) % K_MOD
        
    def comb(nn, kk):
        if kk < 0 or kk > nn:
            return 0
        return (fact[nn] * inv_fact[kk] * inv_fact[nn - kk]) % K_MOD
        
    total_sum = 0
    for k in range(1, n):
        w = min(k, n - k)
        term = comb(n, k)
        term = (term * w) % K_MOD
        term = (term * mod_pow(k, k - 1)) % K_MOD
        term = (term * mod_pow(n - k, n - k - 1)) % K_MOD
        total_sum = (total_sum + term) % K_MOD
        
    inv2 = (K_MOD + 1) // 2
    total_sum = (total_sum * inv2) % K_MOD
    return (fact[n - 1] * total_sum) % K_MOD

def F_exact_small(n):
    sum2 = 0
    for k in range(1, n):
        w = min(k, n - k)
        term = math.comb(n, k) * w * (k ** max(0, k - 1)) * ((n - k) ** max(0, n - k - 1))
        sum2 += term
        
    total_sum = sum2 // 2
    return math.factorial(n - 1) * total_sum

import math
def run_validations():
    assert F_exact_small(3) == 12
    assert F_exact_small(4) == 360
    assert F_exact_small(8) == 16785941760

def solve():
    return str(F_mod(100))

if __name__ == "__main__":
    run_validations()
    print(solve())
