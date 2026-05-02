def solve():
    N = 1_000_000
    MOD = 1_000_000_007

    def mod_pow(base, exp, mod):
        result = 1
        base %= mod
        while exp > 0:
            if exp & 1: result = result * base % mod
            base = base * base % mod
            exp >>= 1
        return result

    def mod_inv(a, mod): return mod_pow(a % mod, mod - 2, mod)

    ans = 0
    for k in range(1, N + 1):
        t = (1 - k * k) % MOD
        if t == 1:
            ans = (ans + N % MOD) % MOD
        else:
            pn = mod_pow(t, N, MOD)
            num = t * ((pn - 1) % MOD) % MOD
            den = (t - 1) % MOD
            ans = (ans + num * mod_inv(den, MOD)) % MOD

    return str(ans % MOD)

if __name__ == '__main__':
    print(solve())
