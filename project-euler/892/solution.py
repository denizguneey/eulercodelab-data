def solve():
    MOD = 1234567891
    target = 10000000
    inv_limit = 2 * target + 3
    inv = [0] * (inv_limit + 1)
    inv[1] = 1
    for i in range(2, inv_limit + 1):
        inv[i] = MOD - (MOD // i) * inv[MOD % i] % MOD

    def next_d(n, d_n, d_n1):
        n2 = n * n % MOD; n1 = (n + 1) % MOD
        t1 = n2 * n1 % MOD * ((2*n+3) % MOD) % MOD * 16 % MOD * d_n % MOD
        quad = (2*n2 + 4*n + 3) % MOD
        t2 = quad * d_n1 % MOD * n1 % MOD * 4 % MOD
        num = (t1 + t2) % MOD
        di = inv[n] * inv[n+2] % MOD * inv[n+3] % MOD * inv[2*n+1] % MOD
        return num * di % MOD

    dp, dc = 0, 2  # D(1)=0, D(2)=2
    total = dp + dc  # sum D(1)+D(2)
    for n in range(1, target - 1):
        dn = next_d(n, dp, dc)
        idx = n + 2
        if idx <= target:
            total = (total + dn) % MOD
        dp, dc = dc, dn

    return str(total % MOD)

if __name__ == '__main__':
    print(solve())
