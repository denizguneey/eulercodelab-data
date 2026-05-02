import sys

MOD = 1000000007

def mod_pow(base, exp):
    res = 1
    base %= MOD
    while exp > 0:
        if exp & 1:
            res = (res * base) % MOD
        base = (base * base) % MOD
        exp >>= 1
    return res

def clmul(a, b):
    res = 0
    shift = 0
    while a > 0:
        tz = (a & -a).bit_length() - 1
        shift += tz
        a >>= tz
        res ^= (b << shift)
        a >>= 1
        shift += 1
    return res

def clpow(base, exp):
    res = 1
    while exp > 0:
        if exp & 1:
            res = clmul(res, base)
        exp >>= 1
        if exp > 0:
            base = clmul(base, base)
    return res

def eval_poly_mod(poly_bits, x_mod):
    if poly_bits == 0:
        return 0
    deg = poly_bits.bit_length() - 1
    ans = 0
    for i in range(deg, -1, -1):
        ans = (ans * x_mod) % MOD
        if (poly_bits >> i) & 1:
            ans += 1
            if ans == MOD:
                ans = 0
    return ans

def solve():
    three_pow_8 = 6561
    two_pow_52 = 1 << 52
    
    f = 11  # X^3 + X + 1
    g = clpow(f, three_pow_8)
    
    x = mod_pow(2, two_pow_52)
    ans = eval_poly_mod(g, x)
    return str(ans)

if __name__ == "__main__":
    print(solve())
