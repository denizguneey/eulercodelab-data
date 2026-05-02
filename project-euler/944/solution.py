def solve():
    MOD = 1234567891
    N = 100000000000000
    SPLIT = 3000000

    def pow_mod(base, exp):
        r = 1; base %= MOD
        while exp > 0:
            if exp & 1: r = r * base % MOD
            base = base * base % MOD; exp >>= 1
        return r

    def sum_range_mod(l, r):
        if l > r: return 0
        cnt = r - l + 1; s = l + r
        return cnt * s // 2 % MOD

    pow_n1 = pow_mod(2, N - 1)
    split = min(N, SPLIT)
    wsum = 0
    for x in range(1, split + 1):
        q = N // x
        p = pow_mod(2, N - q)
        wsum = (wsum + x % MOD * p) % MOD

    inv2 = (MOD + 1) // 2
    qmax = N // (split + 1)
    p = pow_n1
    for q in range(1, qmax + 1):
        l = N // (q + 1) + 1
        if l <= split: l = split + 1
        r = N // q
        if l <= r:
            sx = sum_range_mod(l, r)
            wsum = (wsum + sx * p) % MOD
        p = p * inv2 % MOD

    tri = sum_range_mod(1, N)
    first = pow_n1 * tri % MOD
    return str((first - wsum) % MOD)

if __name__ == '__main__':
    print(solve())
