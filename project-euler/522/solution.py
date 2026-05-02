def solve():
    MOD = 135707531
    n = 12344321

    def mod_pow(base, exp):
        r = 1; base %= MOD
        while exp > 0:
            if exp & 1: r = r * base % MOD
            base = base * base % MOD
            exp >>= 1
        return r

    inv = [0] * (n + 1)
    inv[1] = 1
    for i in range(2, n+1):
        inv[i] = (MOD - MOD//i * inv[MOD%i] % MOD) % MOD

    fact_n = 1
    for i in range(2, n+1): fact_n = fact_n * i % MOD

    invfact = [1] * (n + 1)
    for i in range(1, n+1): invfact[i] = invfact[i-1] * inv[i] % MOD

    term_z = n % MOD * ((n-1) % MOD) % MOD * mod_pow(n-2, n-1) % MOD
    if n < 4: return str(term_z)

    s = 0
    for m in range(2, n-1):
        t = fact_n * invfact[m] % MOD * inv[n-m] % MOD * mod_pow(m-1, m) % MOD
        s = (s + t) % MOD

    return str((term_z + s) % MOD)

if __name__ == '__main__':
    print(solve())
