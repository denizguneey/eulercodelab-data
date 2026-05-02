def solve():
    MOD = 1_000_000_007

    def mod_pow(a, e):
        r = 1
        x = a % MOD
        while e > 0:
            if e & 1: r = r * x % MOD
            x = x * x % MOD
            e >>= 1
        return r

    def norm(v):
        return v % MOD

    def S_mod(k):
        q = k // 9
        r = k % 9
        p10 = mod_pow(10, q)
        base = norm(6 * (p10 - 1))
        base = norm(base - 9 * norm(q))
        coeff = norm(r * (r + 3) // 2)
        part = norm(coeff * p10 % MOD - r)
        return norm(base + part)

    fib = [0] * 91
    fib[1] = 1
    for i in range(2, 91):
        fib[i] = fib[i-1] + fib[i-2]

    ans = 0
    for i in range(2, 91):
        ans = norm(ans + S_mod(fib[i]))

    return str(ans)

if __name__ == '__main__':
    print(solve())
