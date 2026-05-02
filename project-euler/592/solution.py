import sys

kHexDigits = 12
kModBits = 4 * kHexDigits
kMod = 1 << kModBits
kMask = kMod - 1

kStepBits = 16
kStep = 1 << kStepBits
kMask32 = (1 << (kModBits - kStepBits)) - 1
kMask16 = (1 << (kModBits - 2 * kStepBits)) - 1

def mul_mod(a, b):
    return (a * b) & kMask

def pow_mod(base, exp):
    result = 1
    base &= kMask
    while exp > 0:
        if exp & 1:
            result = mul_mod(result, base)
        base = mul_mod(base, base)
        exp >>= 1
    return result

def inverse_odd_mod_2_48(odd):
    x = 1
    for _ in range(6):
        ax = mul_mod(odd, x)
        two_minus_ax = (2 + kMod - ax) & kMask
        x = mul_mod(x, two_minus_ax)
    return x

def build_inverse_table():
    inv = [0] * (kStep // 2)
    for r in range(1, kStep, 2):
        inv[r >> 1] = inverse_odd_mod_2_48(r)
    return inv

odd_inv_table = build_inverse_table()

def e1_mod_2_32(c):
    if c < 2: return 0
    a = c
    b = c - 1
    if (a & 1) == 0:
        a >>= 1
    else:
        b >>= 1
    return ((a & kMask32) * (b & kMask32)) & kMask32

def e2_mod_2_16(c):
    if c < 3: return 0
    f = [c, c - 1, c - 2, 3 * c - 1]
    twos_to_remove = 3
    for i in range(4):
        while twos_to_remove > 0 and (f[i] & 1) == 0:
            f[i] >>= 1
            twos_to_remove -= 1
            
    divided_by_three = False
    for i in range(3):
        if f[i] % 3 == 0:
            f[i] //= 3
            divided_by_three = True
            break
            
    res = 1
    for v in f:
        res = (res * (v & kMask16)) & kMask16
    return res

def class_product(odd_residue, count):
    if count == 0: return 1
    r_pow = pow_mod(odd_residue, count)
    r_inv = odd_inv_table[odd_residue >> 1]
    a = mul_mod(kStep, r_inv)
    
    poly = 1
    poly = (poly + mul_mod(a, e1_mod_2_32(count))) & kMask
    poly = (poly + mul_mod(mul_mod(a, a), e2_mod_2_16(count))) & kMask
    return mul_mod(r_pow, poly)

def odd_prefix(n):
    if n == 0: return 1
    q = n >> kStepBits
    rem = n & (kStep - 1)
    
    if q == 0:
        p = 1
        for r in range(1, rem + 1, 2):
            p = mul_mod(p, r)
        return p
        
    p = 1
    q_step = (q * kStep) & kMask
    for r in range(1, kStep, 2):
        p = mul_mod(p, class_product(r, q))
        if r <= rem:
            p = mul_mod(p, (q_step + r) & kMask)
    return p

def odd_factorial_part(n):
    levels = []
    x = n
    while x > 0:
        levels.append(x)
        x >>= 1
        
    res = 1
    for L in levels:
        res = mul_mod(res, odd_prefix(L))
    return res

def v2_factorial(n):
    e = 0
    while n > 0:
        n >>= 1
        e += n
    return e

def f_value(n):
    odd_part = odd_factorial_part(n)
    rem_twos = v2_factorial(n) & 3
    return mul_mod(odd_part, 1 << rem_twos)

def factorial_u64(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

def to_hex12(x):
    return f"{x:012X}"

def solve():
    n = factorial_u64(20)
    ans = f_value(n)
    return to_hex12(ans)

if __name__ == '__main__':
    print(solve())
