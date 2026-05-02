def solve():
    MOD = 1000000007
    n = 100000000
    r = n - 1

    def mul_mod(a, b): return a * b % MOD
    def mod_pow(base, exp):
        result = 1
        while exp > 0:
            if exp & 1: result = result * base % MOD
            base = base * base % MOD; exp >>= 1
        return result

    def fib_pair(n):
        if n == 0: return (0, 1)
        a, b = fib_pair(n >> 1)
        c = a * ((2*b - a) % MOD) % MOD
        d = (a*a + b*b) % MOD
        return (d, (c+d) % MOD) if n & 1 else (c, d)

    def lucas(n):
        if n == 0: return 2
        fn, fn1 = fib_pair(n)
        return (2*fn1 - fn) % MOD

    # Batch inverse
    def batch_inv(vals):
        m = len(vals)
        if m == 0: return []
        prefix = [0]*m; prefix[0] = vals[0]
        for i in range(1, m):
            prefix[i] = prefix[i-1] * vals[i] % MOD
        sinv = mod_pow(prefix[-1], MOD-2)
        inv = [0]*m
        for i in range(m-1, -1, -1):
            left = prefix[i-1] if i > 0 else 1
            inv[i] = sinv * left % MOD
            sinv = sinv * vals[i] % MOD
        return inv

    l_t = lucas(r); l_tp1 = lucas(r+1)
    coeff = 1; answer = 0; t = r
    BLOCK = 1000000

    while t >= 1:
        hi = t; lo = max(1, hi - BLOCK + 1)
        m = hi - lo + 1
        denoms = [0]*m
        for i in range(m):
            ct = hi - i
            if ct == 1: denoms[i] = 1
            else:
                u = r - ct + 1
                denoms[i] = ct % MOD * (u % MOD) % MOD
        inv_d = batch_inv(denoms)

        for i in range(m):
            ct = hi - i
            answer = (answer + coeff * l_tp1) % MOD
            if ct == 1: break
            num_a = (ct - 1) % MOD
            num_b = (2 * r - ct) % MOD
            num = num_a * num_b % MOD
            coeff = coeff * num % MOD * inv_d[i] % MOD
            nl_tp1 = l_t; nl_t = (l_tp1 - l_t) % MOD
            l_tp1 = nl_tp1; l_t = nl_t

        if lo == 1: break
        t = lo - 1

    return str(answer)

if __name__ == '__main__':
    print(solve())
