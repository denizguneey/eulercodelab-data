def poly_mul_mod(a, b, mod):
    c = [0] * 24
    for i in range(24):
        if a[i] == 0:
            continue
        for j in range(24 - i):
            if b[j] == 0:
                continue
            c[i + j] = (c[i + j] + a[i] * b[j]) % mod
    return c

def poly_pow_digit_sum(exponent, mod):
    base = [0] * 24
    for d in range(10):
        base[d] = 1

    result = [0] * 24
    result[0] = 1

    e = exponent
    while e > 0:
        if e & 1:
            result = poly_mul_mod(result, base, mod)
        e >>= 1
        if e > 0:
            base = poly_mul_mod(base, base, mod)
            
    return result

def count_via_classes_mod(n, mod):
    q = n // 22
    r = int(n % 22)

    c_q = poly_pow_digit_sum(q, mod)
    c_q1 = poly_pow_digit_sum(q + 1, mod)

    weights = [0] * 22
    cur = 1
    for i in range(22):
        weights[i] = cur
        cur = (cur * 10) % 23

    dp = [[0] * 23 for _ in range(24)]
    dp[0][0] = 1

    for cls in range(22):
        coeff = c_q1 if cls < r else c_q
        
        nxt = [[0] * 23 for _ in range(24)]
        
        for s in range(24):
            for rem in range(23):
                cur_count = dp[s][rem]
                if cur_count == 0:
                    continue
                    
                w = weights[cls]
                for t in range(24 - s):
                    ways = coeff[t]
                    if ways == 0:
                        continue
                        
                    rem2 = (rem + w * t) % 23
                    nxt[s + t][rem2] = (nxt[s + t][rem2] + cur_count * ways) % mod
                    
        dp = nxt

    return dp[23][0]

def solve(n=3138428376721, mod=1000000000):
    return str(count_via_classes_mod(n, mod))

if __name__ == '__main__':
    print(solve())
