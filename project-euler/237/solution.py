def mod_norm(x, mod):
    v = x % mod
    if v < 0:
        v += mod
    return v

def mat_mul(a, b, mod):
    c = [[0] * 4 for _ in range(4)]
    for i in range(4):
        for k in range(4):
            if a[i][k] == 0:
                continue
            for j in range(4):
                c[i][j] = mod_norm(c[i][j] + a[i][k] * b[k][j], mod)
    return c

def mat_vec_mul(a, x, mod):
    y = [0] * 4
    for i in range(4):
        sum_val = 0
        for j in range(4):
            sum_val += a[i][j] * x[j]
        y[i] = mod_norm(sum_val, mod)
    return y

def solve(n=10**12, mod=10**8):
    if n == 1 or n == 2: return 1 % mod
    if n == 3: return 4 % mod
    if n == 4: return 8 % mod

    step = [
        [2, 2, mod_norm(-2, mod), 1],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0]
    ]

    acc = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]

    power = n - 4
    while power > 0:
        if power % 2 == 1:
            acc = mat_mul(acc, step, mod)
        step = mat_mul(step, step, mod)
        power //= 2

    base = [8, 4, 1, 1]
    out = mat_vec_mul(acc, base, mod)
    return str(out[0])

if __name__ == '__main__':
    print(solve())
