def solve():
    MOD = 1000000007
    alpha = 10000000
    n = 1000000000000

    def mod_pow(base, exp):
        r = 1; base %= MOD
        while exp > 0:
            if exp & 1: r = r * base % MOD
            base = base * base % MOD; exp >>= 1
        return r

    inv = [0]*(alpha+1); inv[1] = 1
    for i in range(2, alpha+1):
        inv[i] = MOD - (MOD // i) * inv[MOD % i] % MOD

    comb = 1; coeff = [0]*alpha; coeff[0] = 1
    for k in range(alpha - 1):
        comb = comb * (alpha - k) % MOD * inv[k+1] % MOD
        coeff[k+1] = comb

    n1 = (n + 1) % MOD; exp = n + 1
    ans = 0
    for k in range(alpha):
        if k == 0: geo = 1
        elif k == 1: geo = n1
        else:
            p = mod_pow(k, exp)
            geo = (p - 1) % MOD * inv[k-1] % MOD
        term = coeff[k] * geo % MOD
        if (alpha - k + 1) % 2 == 0:
            ans = (ans + term) % MOD
        else:
            ans = (ans - term) % MOD

    return str(ans % MOD)

if __name__ == '__main__':
    print(solve())
