def mod_pow(base, exp, mod):
    return pow(base, exp, mod)

def mod_inv(x, mod):
    return pow(x, mod - 2, mod)

def fib_pair_mod(n, mod):
    if n == 0:
        return 0, 1
    a, b = fib_pair_mod(n >> 1, mod)
    c = a * (2 * b - a) % mod
    d = (a * a + b * b) % mod
    if n & 1:
        return d, (c + d) % mod
    return c, d

def solve_checksum_mod(n):
    MOD = 1000000007
    MOD_EXP = MOD - 1
    
    k = n - 1
    fk_mod, fk1_mod = fib_pair_mod(k, MOD_EXP)
    F = fk_mod
    L = (2 * fk1_mod - fk_mod) % MOD_EXP
    
    sign = 1 if (k % 3 == 0) else -1
    
    two_pow_L = mod_pow(2, L, MOD)
    three_pow_F = mod_pow(3, F, MOD)
    
    if n & 1:
        alpha = two_pow_L
        beta = three_pow_F
        g1 = 4 if n == 1 else 12
        g2 = 1
    else:
        alpha = three_pow_F
        beta = two_pow_L
        g1 = 1
        g2 = 6 if n == 2 else 12
        
    alpha2 = (alpha * alpha) % MOD
    beta2 = (beta * beta) % MOD
    
    n1 = (3 * alpha2 + 4 * beta2) % MOD
    n2 = (4 * alpha2 - 3 * beta2) % MOD
    
    d_base = (two_pow_L * three_pow_F) % MOD
    
    a = (n1 * mod_inv(g1, MOD)) % MOD
    b = (d_base * mod_inv(g1, MOD)) % MOD
    c = (n2 * mod_inv(g2, MOD)) % MOD
    d = (d_base * mod_inv(g2, MOD)) % MOD
    
    if sign < 0:
        a = (-a) % MOD
        c = (-c) % MOD
        
    return str((a + b + c + d) % MOD)

def solve():
    return solve_checksum_mod(11**14)

if __name__ == '__main__':
    print(solve())
