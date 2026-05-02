def solve():
    MOD = 76543217
    m, n = 10000, 5000
    p = m - n
    cells = m * m - n * n

    def mod_pow(base, exp, mod=MOD):
        r = 1; base %= mod
        while exp > 0:
            if exp & 1: r = r * base % mod
            base = base * base % mod
            exp >>= 1
        return r

    max_small = 2 * m - 1
    fact_small = [1] * (max_small + 1)
    for i in range(1, max_small + 1):
        fact_small[i] = fact_small[i-1] * i % MOD

    fact_cells = 1
    for i in range(1, cells + 1):
        fact_cells = fact_cells * (i % MOD) % MOD

    pa_num = 1
    for t in range(m + n, 2 * m):
        pa_num = pa_num * fact_small[t] % MOD
    pa_den = 1
    for s in range(2 * n, m + n):
        pa_den = pa_den * fact_small[s] % MOD
    pa = pa_num * mod_pow(pa_den, MOD - 2) % MOD

    pb_num = 1
    for t in range(n, m):
        pb_num = pb_num * fact_small[t] % MOD
    pb_den = 1
    for u in range(p):
        pb_den = pb_den * fact_small[u] % MOD
    pb = pb_num * mod_pow(pb_den, MOD - 2) % MOD

    hooks = pa * pb % MOD * pb % MOD
    return str(fact_cells * mod_pow(hooks, MOD - 2) % MOD)

if __name__ == '__main__':
    print(solve())
