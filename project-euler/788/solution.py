MOD = 1000000007

def mod_pow(a, e):
    return pow(a, e, MOD)

def comb(n, k, fact, inv_fact):
    if k < 0 or k > n:
        return 0
    return (fact[n] * inv_fact[k] % MOD) * inv_fact[n - k] % MOD

def solve_fast(n):
    fact = [1] * (n + 1)
    inv_fact = [1] * (n + 1)
    pow9 = [1] * (n + 2)
    
    for i in range(1, n + 1):
        fact[i] = (fact[i - 1] * i) % MOD
        
    inv_fact[n] = mod_pow(fact[n], MOD - 2)
    for i in range(n, 0, -1):
        inv_fact[i - 1] = (inv_fact[i] * i) % MOD
        
    for i in range(1, n + 2):
        pow9[i] = (pow9[i - 1] * 9) % MOD
        
    ans = 0
    for length in range(1, n + 1):
        for k in range(length // 2 + 1, length + 1):
            c = comb(length, k, fact, inv_fact)
            # The C++ code uses length - k + 1 for pow9 offset:
            # pow9[length - k + 1] -> this has 1 for length - k (non-zero leading),
            # but then there's a logic about 9 options for other digits
            # The C++ code did: ways = (pow9[len - k + 1] * c) % MOD
            ways = (pow9[length - k + 1] * c) % MOD
            ans = (ans + ways) % MOD
            
    return ans

def solve():
    return str(solve_fast(2022))

if __name__ == "__main__":
    print(solve())
