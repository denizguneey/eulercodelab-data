def solve():
    MOD = 1000000007
    k = 10000000
    n = 1000000000000

    def mod_pow(base, exp):
        r = 1; base %= MOD
        while exp > 0:
            if exp & 1: r = r * base % MOD
            base = base * base % MOD; exp >>= 1
        return r

    inv = [0]*(k+2); inv[1] = 1
    for i in range(2, k+2):
        inv[i] = MOD - (MOD // i) * inv[MOD % i] % MOD

    exp = n + 1; n1 = exp % MOD
    A_next = k % MOD; C_curr = (k + 1) % MOD
    coeff = [0]*k

    for r in range(k-1, -1, -1):
        if r == k-1:
            A = A_next
        else:
            pos = ((k + 1 - r) & 1) == 0
            sC = C_curr if pos else (MOD - C_curr)
            A = (2 * A_next % MOD + sC + MOD - 1) % MOD
            A_next = A
        coeff[r] = A
        if r > 0:
            C_curr = C_curr * (r + 1) % MOD * inv[k - r + 1] % MOD

    ans = 0
    for r in range(k):
        if r == 0: g = 1
        elif r == 1: g = n1
        else:
            p = mod_pow(r, exp)
            g = (p - 1) % MOD * inv[r - 1] % MOD
        ans = (ans + coeff[r] * g) % MOD

    return str(ans)

if __name__ == '__main__':
    print(solve())
