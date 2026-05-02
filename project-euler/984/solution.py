MOD = 1000000007
K = 14

INIT = [
    1, 4, 9, 92, 903, 4411, 14959, 41083, 98200,
    212418, 425756, 803074, 1441065, 2479669
]

REC = [
    7, MOD - 19, 21, 6, MOD - 42, 42, MOD - 6,
    MOD - 21, 19, MOD - 7, 1, 0, 0, 0
]

def combine(a, b):
    prod = [0] * (2 * K)
    for i in range(K):
        if a[i] == 0: continue
        for j in range(K):
            if b[j] == 0: continue
            prod[i + j] = (prod[i + j] + a[i] * b[j]) % MOD
            
    for i in range(2 * K - 2, K - 1, -1):
        if prod[i] == 0: continue
        for j in range(1, K + 1):
            prod[i - j] = (prod[i - j] + prod[i] * REC[j - 1]) % MOD
            
    return prod[:K]

def f_even_closed_form_mod(n):
    x = n % MOD
    p = [0] * 9
    p[0] = 1
    for i in range(1, 9):
        p[i] = (p[i - 1] * x) % MOD
        
    def mod_inv(val):
        return pow(val % MOD, MOD - 2, MOD)
        
    inv40320 = mod_inv(40320)
    inv3360 = mod_inv(3360)
    inv1440 = mod_inv(1440)
    inv320 = mod_inv(320)
    inv240 = mod_inv(240)
    inv420 = mod_inv(420)
    inv140 = mod_inv(140)
    
    ans = 0
    ans = (ans + 31 * p[8] % MOD * inv40320) % MOD
    ans = (ans + 31 * p[7] % MOD * inv3360) % MOD
    ans = (ans + 67 * p[6] % MOD * inv1440) % MOD
    ans = (ans + 41 * p[5] % MOD * inv320) % MOD
    ans = (ans + 313 * p[4] % MOD * inv1440) % MOD
    ans = (ans + (MOD - 5699) * p[3] % MOD * inv240) % MOD
    ans = (ans + 16049 * p[2] % MOD * inv420) % MOD
    ans = (ans + 29413 * p[1] % MOD * inv140) % MOD
    ans = (ans + MOD - 419) % MOD
    return ans

def f_mod(n):
    if n == 0:
        return 0
    if n > 3 and (n & 1) == 0:
        return f_even_closed_form_mod(n)
    if n <= K:
        return INIT[n - 1] % MOD
        
    exp = n - 1
    poly = [0] * K
    step = [0] * K
    poly[0] = 1
    step[1] = 1
    
    while exp > 0:
        if exp & 1:
            poly = combine(poly, step)
        step = combine(step, step)
        exp >>= 1
        
    ans = 0
    for i in range(K):
        ans = (ans + poly[i] * INIT[i]) % MOD
    return ans

def solve():
    target = 1000000000000000000
    return str(f_mod(target))

if __name__ == "__main__":
    print(solve())
