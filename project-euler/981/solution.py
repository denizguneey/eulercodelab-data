import math

MOD = 888888883

def mod_pow(base, exp):
    return pow(base, exp, MOD)

def build_factorials(max_n):
    fac = [1] * (max_n + 1)
    for i in range(1, max_n + 1):
        fac[i] = (fac[i - 1] * i) % MOD
        
    invfac = [1] * (max_n + 1)
    invfac[max_n] = mod_pow(fac[max_n], MOD - 2)
    for i in range(max_n, 0, -1):
        invfac[i - 1] = (invfac[i] * i) % MOD
        
    return fac, invfac

def multinomial_mod(n, a, b, c, fac, invfac):
    res = fac[n]
    res = (res * invfac[a]) % MOD
    res = (res * invfac[b]) % MOD
    res = (res * invfac[c]) % MOD
    return res

def compute_N_mod(X, Y, Z, fac, invfac):
    px = X & 1
    py = Y & 1
    pz = Z & 1
    if px != py or py != pz:
        return 0
        
    S = X + Y + Z
    total = multinomial_mod(S, X, Y, Z, fac, invfac)
    inv2 = (MOD + 1) // 2
    
    if px == 1:
        return (total * inv2) % MOD
        
    half = multinomial_mod(S // 2, X // 2, Y // 2, Z // 2, fac, invfac)
    if (S // 2) & 1:
        diff = (total + MOD - half) % MOD
        return (diff * inv2) % MOD
        
    sum_val = total + half
    return (sum_val * inv2) % MOD

def compute_N_exact_small(X, Y, Z):
    px = X & 1
    py = Y & 1
    pz = Z & 1
    if px != py or py != pz:
        return 0
        
    S = X + Y + Z
    total = math.factorial(S) // (math.factorial(X) * math.factorial(Y) * math.factorial(Z))
    
    if px == 1:
        return total // 2
        
    half = math.factorial(S // 2) // (math.factorial(X // 2) * math.factorial(Y // 2) * math.factorial(Z // 2))
    if (S // 2) & 1:
        return (total - half) // 2
    return (total + half) // 2

def solve():
    max_i = 87
    cubes = [i * i * i for i in range(max_i + 1)]
    max_sum = 3 * cubes[-1]
    
    fac, invfac = build_factorials(max_sum)
    
    answer = 0
    for X in cubes:
        for Y in cubes:
            for Z in cubes:
                answer = (answer + compute_N_mod(X, Y, Z, fac, invfac)) % MOD
                
    return str(answer)

def run_checkpoints():
    assert compute_N_exact_small(2, 2, 2) == 42
    assert compute_N_exact_small(8, 8, 8) == 4732773210

if __name__ == "__main__":
    run_checkpoints()
    print(solve())
