def solve():
    a = 1801088541  # 21^7
    b = 558545864083284007  # 7^21
    c = 35831808  # 12^7
    MOD = 1_000_000_000

    d = a - c
    q = b // a
    r = b % a

    def mod_mul(x, y):
        return (x * y) % MOD

    if b % 2 == 0:
        sum_n = mod_mul((b // 2) % MOD, (b + 1) % MOD)
    else:
        sum_n = mod_mul(b % MOD, ((b + 1) // 2) % MOD)

    term_linear = mod_mul((b + 1) % MOD, (4 * (d % MOD)) % MOD)

    sum_floor = a * q * (q - 1) // 2 + (r + 1) * q
    sum_floor_mod = sum_floor % MOD
    term_floor = mod_mul((a + 3 * d) % MOD, sum_floor_mod)

    return str((sum_n + term_linear + term_floor) % MOD)

if __name__ == '__main__':
    print(solve())
