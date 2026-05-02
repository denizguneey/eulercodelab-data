def solve():
    MOD = 100000000
    n = 100000007
    k = 10007
    
    two_n_mod = pow(2, n, MOD)
    two_nk_mod = pow(2, n - k, MOD)
    x_mod = (two_n_mod + MOD - 1) % MOD
    
    inner_mod = ((k - 1) * two_n_mod + (n - k + 1)) % MOD
    
    ans = (two_nk_mod * inner_mod) % MOD
    ans = (ans * x_mod) % MOD
    ans = (ans * x_mod) % MOD
    
    return f"{ans:08d}"

if __name__ == '__main__':
    print(solve())
