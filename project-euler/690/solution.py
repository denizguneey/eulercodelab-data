MOD = 1000000007

def add_mod(a, b):
    return (a + b) % MOD

def sub_mod(a, b):
    return (a - b + MOD) % MOD

def mul_mod(a, b):
    return (a * b) % MOD

def pow_mod(base, exp):
    return pow(base, exp, MOD)

def precompute_inverses(n):
    inv = [0] * (n + 1)
    if n >= 1:
        inv[1] = 1
    for i in range(2, n + 1):
        inv[i] = MOD - mul_mod(MOD // i, inv[MOD % i])
    return inv

def convolve_truncated(a, b, n):
    out = [0] * (n + 1)
    for i in range(min(n + 1, len(a))):
        ai = a[i]
        if ai == 0:
            continue
        for j in range(min(n - i + 1, len(b))):
            bj = b[j]
            if bj == 0:
                continue
            out[i + j] = (out[i + j] + ai * bj) % MOD
    return out

def invert_series(den, n):
    out = [0] * (n + 1)
    out[0] = pow_mod(den[0], MOD - 2)
    for i in range(1, n + 1):
        sum_val = 0
        for k in range(1, i + 1):
            sum_val = (sum_val + den[k] * out[i - k]) % MOD
        out[i] = (MOD - mul_mod(out[0], sum_val)) % MOD
    return out

def partition_series(n):
    p = [0] * (n + 1)
    p[0] = 1
    for part in range(1, n + 1):
        for i in range(part, n + 1):
            p[i] = (p[i] + p[i - part]) % MOD
    return p

def compute_lobster_tree_counts(n, inv):
    p = partition_series(n)
    
    inv_1mx = [1] * (n + 1)
    a = [(p[i] - inv_1mx[i]) % MOD for i in range(n + 1)]
    
    x_p = [0] * (n + 1)
    for i in range(1, n + 1):
        x_p[i] = p[i - 1]
        
    den1 = [0] * (n + 1)
    den1[0] = 1
    for i in range(1, n + 1):
        den1[i] = (-x_p[i]) % MOD
        
    inv_den1 = invert_series(den1, n)
    
    a_sq = convolve_truncated(a, a, n)
    part1 = convolve_truncated(a_sq, inv_den1, n)
    
    p2 = [0] * (n + 1)
    for i in range(0, n + 1, 2):
        p2[i] = p[i // 2]
        
    inv_1mx2 = [0] * (n + 1)
    for i in range(0, n + 1, 2):
        inv_1mx2[i] = 1
        
    b = [(p2[i] - inv_1mx2[i]) % MOD for i in range(n + 1)]
    
    one_plus_x_p = list(x_p)
    one_plus_x_p[0] = (one_plus_x_p[0] + 1) % MOD
    
    den2 = [0] * (n + 1)
    den2[0] = 1
    for i in range(2, n + 1):
        den2[i] = (-p2[i - 2]) % MOD
        
    inv_den2 = invert_series(den2, n)
    
    tmp = convolve_truncated(b, one_plus_x_p, n)
    part2 = convolve_truncated(tmp, inv_den2, n)
    
    lobsters = [0] * (n + 1)
    for i in range(n - 1):
        sum_val = (part1[i] + part2[i]) % MOD
        lobsters[i + 2] = (lobsters[i + 2] + sum_val * inv[2]) % MOD
        
    for i in range(1, n + 1):
        lobsters[i] = (lobsters[i] + x_p[i]) % MOD
        
    rec = [0] * (n + 1)
    rec[0] = 1
    for i in range(1, n + 1):
        v = rec[i - 1]
        if i >= 2: v = (v + rec[i - 2]) % MOD
        if i >= 3: v = (v - rec[i - 3]) % MOD
        rec[i] = v % MOD
        
    for i in range(n - 2):
        lobsters[i + 3] = (lobsters[i + 3] - rec[i]) % MOD
        
    return [(v % MOD + MOD) % MOD for v in lobsters]

def euler_transform(tree_counts, n, inv):
    c = [0] * (n + 1)
    for d in range(1, n + 1):
        val = (d * tree_counts[d]) % MOD
        for m in range(d, n + 1, d):
            c[m] = (c[m] + val) % MOD
            
    out = [0] * (n + 1)
    out[0] = 1
    for i in range(1, n + 1):
        sum_val = 0
        for k in range(1, i + 1):
            sum_val = (sum_val + c[k] * out[i - k]) % MOD
        out[i] = (sum_val * inv[i]) % MOD
        
    return out

def solve():
    n = 2019
    inv = precompute_inverses(n)
    lobsters = compute_lobster_tree_counts(n, inv)
    tom = euler_transform(lobsters, n, inv)
    return str(tom[n])

if __name__ == '__main__':
    print(solve())
