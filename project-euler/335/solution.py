def mul_mod(a, b, mod):
    return (a * b) % mod

def pow_mod(base, exp, mod):
    return pow(base, exp, mod)

def mod_inverse(a, mod):
    return pow(a, -1, mod)

def solve():
    kExponentLimit = 1000000000000000000
    kModulus = 40353607
    
    inv2 = mod_inverse(2, kModulus)
    inv3 = mod_inverse(3, kModulus)
    
    p2 = pow_mod(2, kExponentLimit + 1, kModulus)
    p3 = pow_mod(3, kExponentLimit + 1, kModulus)
    p4 = pow_mod(4, kExponentLimit + 1, kModulus)
    
    sum_2 = mul_mod(2, (p2 + kModulus - 1) % kModulus, kModulus)
    sum_4 = mul_mod((p4 + kModulus - 1) % kModulus, inv3, kModulus)
    sum_3 = mul_mod((p3 + kModulus - 1) % kModulus, inv2, kModulus)
    
    ans = (sum_2 + sum_4 + kModulus - sum_3) % kModulus
    return str(ans)

if __name__ == '__main__':
    print(solve())
