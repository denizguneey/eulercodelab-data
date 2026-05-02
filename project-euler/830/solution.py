def pow_int(base, exp):
    return base ** exp

def mod_pow(base, exp, mod):
    return pow(base, exp, mod)

def ext_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = ext_gcd(b, a % b)
    x = y1
    y = x1 - y1 * (a // b)
    return g, x, y

def mod_inv(a, mod):
    g, x, y = ext_gcd(a, mod)
    if g != 1: return 0
    return x % mod

def compute_mod_prime(n, p):
    mod_p3 = pow_int(p, 3)
    if n == 0: return 1 % mod_p3
    
    max_j = min(n, 3 * p - 1)
    mod_big = pow_int(p, 5)
    
    binom = [[0] * (max_j + 1) for _ in range(max_j + 1)]
    binom[0][0] = 1
    for j in range(1, max_j + 1):
        binom[j][0] = 1
        binom[j][j] = 1
        for i in range(1, j):
            v = binom[j - 1][i - 1] + binom[j - 1][i]
            if v >= mod_big: v -= mod_big
            binom[j][i] = v
            
    pow_i = [mod_pow(i, n, mod_big) for i in range(max_j + 1)]
    
    vp_fact = [0] * (max_j + 1)
    u_fact = [0] * (max_j + 1)
    u_fact[0] = 1 % mod_p3
    
    for j in range(1, max_j + 1):
        temp = j
        cnt = 0
        while temp % p == 0:
            temp //= p
            cnt += 1
        vp_fact[j] = vp_fact[j - 1] + cnt
        u_fact[j] = (u_fact[j - 1] * (temp % mod_p3)) % mod_p3
        
    inv2 = mod_inv(2 % mod_p3, mod_p3)
    pow2 = mod_pow(2, n, mod_p3)
    n_mod = n % mod_p3
    fall = 1 % mod_p3
    total_sum = 0
    
    for j in range(1, max_j + 1):
        factor = (n_mod - (j - 1)) % mod_p3
        if factor < 0: factor += mod_p3
        fall = (fall * factor) % mod_p3
        pow2 = (pow2 * inv2) % mod_p3
        
        a = vp_fact[j]
        mod_ext = mod_p3 * pow_int(p, a)
        
        N = 0
        for i in range(j + 1):
            term = (binom[j][i] * pow_i[i]) % mod_big
            if (j - i) & 1:
                N -= term
                if N < 0: N += mod_big
            else:
                N += term
                if N >= mod_big: N -= mod_big
                
        if mod_ext != mod_big: N %= mod_ext
        if N < 0: N += mod_ext
        
        N_div = N // pow_int(p, a)
        
        inv_u = mod_inv(u_fact[j], mod_p3)
        stirling = ((N_div % mod_p3) * inv_u) % mod_p3
        
        term = (stirling * fall) % mod_p3
        term = (term * pow2) % mod_p3
        total_sum = (total_sum + term) % mod_p3
        
    return total_sum

def combine_crt(rem, mods):
    M = 1
    for m in mods: M *= m
    res = 0
    for i in range(len(mods)):
        Mi = M // mods[i]
        inv = mod_inv(Mi % mods[i], mods[i])
        term = (rem[i] * Mi) % M
        term = (term * inv) % M
        res = (res + term) % M
    return res

def compute_mod_all(n):
    primes = [83, 89, 97]
    mods = [pow_int(p, 3) for p in primes]
    rems = [compute_mod_prime(n, p) for p in primes]
    return combine_crt(rems, mods)

def solve():
    n = 1000000000000000000
    ans = compute_mod_all(n)
    return str(ans)

if __name__ == "__main__":
    print(solve())
