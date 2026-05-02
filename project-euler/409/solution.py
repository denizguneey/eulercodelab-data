MOD = 1000000007

def mod_pow(base, exp):
    return pow(base, exp, MOD)

def solve():
    n = 10000000
    pow2n = mod_pow(2, n)
    total_base = (pow2n - 1) % MOD
    
    T = 1
    for i in range(n):
        T = (T * (total_base - i)) % MOD
        
    m = n // 2
    
    fact_n = 1
    fact_m = 1
    for i in range(1, n + 1):
        fact_n = (fact_n * i) % MOD
        if i <= m:
            fact_m = (fact_m * i) % MOD
            
    inv_fact_m = mod_pow(fact_m, MOD - 2)
    
    q_minus_1 = (mod_pow(2, n - 1) - 1) % MOD
    falling_q = 1
    for i in range(m):
        falling_q = (falling_q * (q_minus_1 - i)) % MOD
        
    comb = (falling_q * inv_fact_m) % MOD
    
    if (n & 1) == 0:
        if (m & 1) == 1:
            comb = (MOD - comb) % MOD
    else:
        if (m & 1) == 0:
            comb = (MOD - comb) % MOD
            
    S = (fact_n * comb) % MOD
    
    inv_pow2n = mod_pow(pow2n, MOD - 2)
    losing = ((T + (total_base * S) % MOD) * inv_pow2n) % MOD
    winning = (T - losing + MOD) % MOD
    
    return str(winning)

if __name__ == '__main__':
    print(solve())
