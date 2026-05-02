def pow_mod(base, exp, mod):
    if mod == 1: return 0
    res = 1
    cur = base % mod
    while exp > 0:
        if exp & 1:
            res = (res * cur) % mod
        cur = (cur * cur) % mod
        exp >>= 1
    return res

def multiply_matrix(a, b, mod):
    out = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            s = 0
            for k in range(3):
                s += a[i][k] * b[k][j]
            out[i][j] = s % mod
    return out

def power_matrix(base, exp, mod):
    res = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    while exp > 0:
        if exp & 1:
            res = multiply_matrix(res, base, mod)
        base = multiply_matrix(base, base, mod)
        exp >>= 1
    return res

def compute_newton_sum_mod(n, exp, mod):
    c = pow_mod(2, n, mod)
    s0 = 3 % mod
    s1 = c
    s2 = (c * c) % mod
    
    if exp == 0: return s0
    if exp == 1: return s1
    if exp == 2: return s2
    
    transition = [
        [c, 0, (mod - (n % mod)) % mod],
        [1, 0, 0],
        [0, 1, 0]
    ]
    p = power_matrix(transition, exp - 2, mod)
    top = p[0][0] * s2 + p[0][1] * s1 + p[0][2] * s0
    return top % mod

def compute_term_mod(n, exp, mod):
    sum_mod = compute_newton_sum_mod(n, exp, mod)
    return (sum_mod + mod - 1) % mod

def solve():
    mod = 100000000
    total = 0
    for n in range(1, 31):
        total = (total + compute_term_mod(n, 987654321, mod)) % mod
    return str(total)

if __name__ == '__main__':
    print(solve())
