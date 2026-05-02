def normalize(num, exp):
    if num == 0:
        return 0, 0
    while exp > 0 and (num & 1) == 0:
        num >>= 1
        exp -= 1
    return num, exp

def floor_div_pow2(x, sh):
    if sh == 0:
        return x
    if x >= 0:
        return x >> sh
    a = -x
    return -((a + ((1 << sh) - 1)) >> sh)

def cmp_dyad(num_a, exp_a, num_b, exp_b):
    na = num_a
    nb = num_b
    if exp_a < exp_b:
        na <<= (exp_b - exp_a)
    elif exp_b < exp_a:
        nb <<= (exp_a - exp_b)
    
    if na < nb:
        return -1
    if na > nb:
        return 1
    return 0

def floor_dyad(num, exp):
    return floor_div_pow2(num, exp)

def ceil_dyad(num, exp):
    return -floor_div_pow2(-num, exp)

def floor_scaled(num, exp, k):
    if k >= exp:
        return num << (k - exp)
    return floor_div_pow2(num, exp - k)

def ceil_scaled(num, exp, k):
    return -floor_scaled(-num, exp, k)

def simplest_between(num_L, exp_L, hasL, num_R, exp_R, hasR):
    if not hasL and not hasR:
        return 0, 0
    if hasL and not hasR:
        return floor_dyad(num_L, exp_L) + 1, 0
    if not hasL and hasR:
        return ceil_dyad(num_R, exp_R) - 1, 0
        
    for k in range(81):
        lo = floor_scaled(num_L, exp_L, k) + 1
        hi = ceil_scaled(num_R, exp_R, k) - 1
        if lo > hi:
            continue
            
        if lo <= 0 and hi >= 0:
            m = 0
        elif hi < 0:
            m = hi
        else:
            m = lo
            
        return normalize(m, k)
    
    return 0, 0

def bit_length_custom(x):
    if x == 0:
        return 1
    return x.bit_length()

def delete_bit(x, length, idx_from_left):
    p = length - 1 - idx_from_left
    hi = x >> (p + 1)
    lo = 0 if p == 0 else (x & ((1 << p) - 1))
    return (hi << p) | lo

def compute_values(n):
    v = [(0, 0)] * (n + 1)
    
    for x in range(1, n + 1):
        length = bit_length_custom(x)
        bestL_num, bestL_exp = 0, 0
        bestR_num, bestR_exp = 0, 0
        hasL = False
        hasR = False
        
        for i in range(length):
            bit = (x >> (length - 1 - i)) & 1
            y = delete_bit(x, length, i)
            vy_num, vy_exp = v[y]
            
            if bit == 1:
                if not hasL or cmp_dyad(vy_num, vy_exp, bestL_num, bestL_exp) > 0:
                    bestL_num = vy_num
                    bestL_exp = vy_exp
                    hasL = True
            else:
                if not hasR or cmp_dyad(vy_num, vy_exp, bestR_num, bestR_exp) < 0:
                    bestR_num = vy_num
                    bestR_exp = vy_exp
                    hasR = True
                    
        v[x] = simplest_between(bestL_num, bestL_exp, hasL, bestR_num, bestR_exp, hasR)
        
    return v

def S_value(n):
    vals = compute_values(n)
    max_exp = 0
    for i in range(1, n + 1):
        max_exp = max(max_exp, vals[i][1])
        
    scaled_sum = 0
    for i in range(1, n + 1):
        num, exp = vals[i]
        sh = max_exp - exp
        term = i * num
        scaled_sum += (term << sh)
        
    den = 1 << max_exp
    return (scaled_sum + den - 1) // den

def solve():
    return str(S_value(100000))

if __name__ == "__main__":
    print(solve())
