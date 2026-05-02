def mod_pow(base, exp, mod):
    return pow(base, exp, mod)

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def mod_inverse(a, mod):
    g, x, y = extended_gcd(a, mod)
    if g != 1: return 0
    res = x % mod
    if res < 0: res += mod
    return res

def direct_terms_exact(count):
    kDigits = [1, 2, 3, 4, 3, 2]
    out = [0] * (count + 1)
    pos = 0
    for n in range(1, count + 1):
        s = 0
        val = 0
        while s < n:
            d = kDigits[pos]
            pos = (pos + 1) % 6
            s += d
            val = val * 10 + d
        if s != n: return []
        out[n] = val
    return out

def geometric_sum(ratio, terms, mod, inv_ratio_minus_one):
    if terms == 0: return 0
    p = mod_pow(ratio, terms, mod)
    numerator = (p + mod - 1) % mod
    return (numerator * inv_ratio_minus_one) % mod

def fast_sum_mod(n_max):
    kMod = 123454321
    kBlockBase = 1000000
    terms = direct_terms_exact(45)
    if not terms: return 0
    
    base = [0] * 15
    add = [0] * 15
    for r in range(1, 16):
        v0 = terms[r]
        v1 = terms[r + 15]
        v2 = terms[r + 30]
        c = v1 - v0 * kBlockBase
        if v2 != v1 * kBlockBase + c: return 0
        base[r - 1] = v0
        add[r - 1] = c
        
    inv_b_minus_1 = mod_inverse(kBlockBase - 1, kMod)
    if inv_b_minus_1 == 0: return 0
    
    total = 0
    for r in range(1, 16):
        if n_max < r: break
        count = (n_max - r) // 15 + 1
        g = geometric_sum(kBlockBase, count, kMod, inv_b_minus_1)
        count_mod = count % kMod
        g_minus_count = (g + kMod - count_mod) % kMod
        t = (g_minus_count * inv_b_minus_1) % kMod
        
        part_base = ((base[r - 1] % kMod) * g) % kMod
        part_add = ((add[r - 1] % kMod) * t) % kMod
        total = (total + part_base) % kMod
        total = (total + part_add) % kMod
        
    return total

def solve():
    return str(fast_sum_mod(100000000000000))

if __name__ == '__main__':
    print(solve())
