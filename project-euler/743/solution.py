def solve():
    MOD = 1_000_000_007
    k = 100_000_000
    n = 10_000_000_000_000_000

    def mod_pow(base, exp, mod=MOD):
        r = 1
        base %= mod
        while exp > 0:
            if exp & 1: r = r * base % mod
            base = base * base % mod
            exp >>= 1
        return r

    def mod_mul(a, b): return a * b % MOD

    q = n // k
    b = mod_pow(2, q)
    term = mod_pow(b, k)
    answer = term

    inv_b = mod_pow(b, MOD - 2)
    inv_b2 = mod_mul(inv_b, inv_b)

    half = k // 2
    inverses = [0] * (half + 1)
    if half >= 1: inverses[1] = 1
    for i in range(2, half + 1):
        inverses[i] = MOD - (MOD // i) * inverses[MOD % i] % MOD

    num1 = k % MOD
    num2 = (k - 1) % MOD
    for x in range(1, half + 1):
        inv_x = inverses[x]
        term = mod_mul(term, num1)
        term = mod_mul(term, num2)
        term = mod_mul(term, inv_x)
        term = mod_mul(term, inv_x)
        term = mod_mul(term, inv_b2)
        answer = (answer + term) % MOD
        num1 = (num1 + MOD - 2) % MOD
        num2 = (num2 + MOD - 2) % MOD

    return str(answer)

if __name__ == '__main__':
    print(solve())
