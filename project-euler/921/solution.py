def solve():
    MOD = 398874989
    GROUP = MOD * MOD - 1
    kM = 1618034

    def add_mod(x, y): return (x + y) % MOD
    def mul_mod(x, y): return x * y % MOD

    def mul_elem(x, y):
        aa = x[0]*y[0]%MOD; bb = x[1]*y[1]%MOD
        real = (aa + 5*bb) % MOD
        imag = (x[0]*y[1] + x[1]*y[0]) % MOD
        return (real, imag)

    def pow_elem(base, exp):
        r = (1, 0)
        while exp > 0:
            if exp & 1: r = mul_elem(r, base)
            exp >>= 1
            if exp > 0: base = mul_elem(base, base)
        return r

    def pow5(x):
        x2 = x*x%MOD; x4 = x2*x2%MOD; return x4*x%MOD

    base = ((MOD + MOD - 2) % MOD, 1)
    # Precompute powers of base for fast exponentiation
    powers = [base]
    for _ in range(63): powers.append(mul_elem(powers[-1], powers[-1]))

    def pow_base(exp):
        r = (1, 0)
        while exp:
            b = (exp & -exp).bit_length() - 1
            r = mul_elem(r, powers[b]); exp &= exp - 1
        return r

    def s_from_exp(exp):
        v = pow_base(exp)
        p = v[1]; q = (MOD - v[0]) % MOD
        return (pow5(p) + pow5(q)) % MOD

    ep2 = 5; ep1 = 5  # 5^{F_1}, 5^{F_2}
    answer = s_from_exp(ep1)
    for i in range(3, kM + 1):
        cur = ep1 * ep2 % GROUP
        answer = (answer + s_from_exp(cur)) % MOD
        ep2, ep1 = ep1, cur

    return str(answer)

if __name__ == '__main__':
    print(solve())
