def solve():
    MOD = 999999001
    n_val = 1000; m_val = 1000

    def mod_pow(base, exp, mod=MOD):
        r = 1; base %= mod
        while exp > 0:
            if exp & 1: r = r * base % mod
            base = base * base % mod; exp >>= 1
        return r

    def mod_inv(x): return mod_pow(x, MOD - 2)

    # SPF sieve
    spf = list(range(n_val + 1))
    primes = []
    for i in range(2, n_val + 1):
        if spf[i] == i: primes.append(i)
        for p in primes:
            if i * p > n_val or p > spf[i]: break
            spf[i * p] = p

    # Prime exponents of superproduct
    exp_arr = [0] * (n_val + 1)
    for t in range(1, n_val + 1):
        coef = (n_val - t + 1) * (n_val - t + 2) // 2
        x = t
        while x > 1:
            p = spf[x]; cnt = 0
            while x % p == 0: x //= p; cnt += 1
            exp_arr[p] += coef * cnt

    factors = [(p, exp_arr[p]) for p in range(2, n_val + 1) if exp_arr[p] > 0]

    dp = [0] * m_val; dp[0] = 1
    for p_int, e in factors:
        p = p_int
        q = mod_pow(p, m_val)
        coeff = [0] * m_val
        pp = 1
        for t in range(m_val):
            if e >= t:
                cnt = (e - t) // m_val + 1
                if q == 1: geom = cnt % MOD
                else:
                    num = (mod_pow(q, cnt) - 1) % MOD
                    geom = num * mod_inv((q - 1) % MOD) % MOD
                coeff[t] = pp * geom % MOD
            pp = pp * p % MOD

        nxt = [0] * m_val
        for r in range(m_val):
            if dp[r] == 0: continue
            for t in range(m_val):
                idx = (r + t) % m_val
                nxt[idx] = (nxt[idx] + dp[r] * coeff[t]) % MOD
        dp = nxt

    return str(dp[0])

if __name__ == '__main__':
    print(solve())
