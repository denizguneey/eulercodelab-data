def inverse_mod(a, mod):
    a %= mod
    phi = mod - mod // 13
    return pow(a, phi - 1, mod)

def crt_coprime(a1, m1, a2, m2):
    inv_m1 = inverse_mod(m1 % m2, m2)
    delta = a2 - (a1 % m2)
    t = (delta * inv_m1) % m2
    return a1 + m1 * t

def c_mod_13_power_from_n_residue(n_residue, n_is_large, k):
    mod = 13 ** k
    
    if not n_is_large and n_residue <= 2:
        return 1 % mod
        
    ord12 = 2 * (13 ** (k - 1))
    two_ord = 2 * ord12
    lambda_val = 12 * (13 ** (k - 2)) if k >= 2 else 2
    
    exp = (n_residue + lambda_val - 2) % lambda_val
    x = pow(3, exp, two_ord)
    
    numer = (x + two_ord - 3) % two_ord
    e = (numer // 2) % ord12
    
    return ((8 % mod) * pow(12, e, mod)) % mod

def solve():
    n0 = 10000
    
    a_mod_13_4 = c_mod_13_power_from_n_residue(n0, False, 4)
    a_mod_12x13_4 = crt_coprime(0, 12, a_mod_13_4, 13 ** 4)
    
    b_mod_13_6 = c_mod_13_power_from_n_residue(a_mod_12x13_4, True, 6)
    b_mod_12x13_6 = crt_coprime(0, 12, b_mod_13_6, 13 ** 6)
    
    result = c_mod_13_power_from_n_residue(b_mod_12x13_6, True, 8)
    return str(result)

if __name__ == '__main__':
    print(solve())
