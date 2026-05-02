def solve():
    N = 10**15
    MOD = 10**9

    def sum_sq_mod(n, mod):
        if n == 0: return 0
        a, b, c = n, n+1, 2*n+1
        if a % 2 == 0: a //= 2
        else: b //= 2
        if a % 3 == 0: a //= 3
        elif b % 3 == 0: b //= 3
        else: c //= 3
        return (a % mod) * (b % mod) % mod * (c % mod) % mod

    def sum_sq_range(l, r, mod):
        return (sum_sq_mod(r, mod) - sum_sq_mod(l-1, mod)) % mod

    ans = 0
    l = 1
    while l <= N:
        q = N // l
        r = N // q
        term = (q % MOD) * sum_sq_range(l, r, MOD) % MOD
        ans = (ans + term) % MOD
        l = r + 1

    return str(ans)

if __name__ == '__main__':
    print(solve())
