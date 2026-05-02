def solve():
    MOD = 1000000007
    n_max = 2021

    def mul_mod(a, b): return a * b % MOD
    def add_mod(a, b): return (a + b) % MOD
    def sub_mod(a, b): return (a - b) % MOD
    def mod_pow(base, exp):
        r = 1; base %= MOD
        while exp > 0:
            if exp & 1: r = r * base % MOD
            base = base * base % MOD; exp >>= 1
        return r

    max_len = 2 * n_max; max_k = n_max
    counts = [[0]*(max_k+1) for _ in range(max_len+1)]

    inits = [(a, b) for a in range(3) for b in range(3) if a == 0 or b == 0]
    SC = 9

    for ia, ib in inits:
        k0 = (ia != 0) + (ib != 0)
        s0 = 3*ia + ib
        dp = [[0]*(max_k+1) for _ in range(SC)]
        dp[s0][k0] = 1

        for ln in range(2, max_len+1):
            # Collect valid end states
            for state in range(SC):
                p2 = state // 3; p1 = state % 3
                if p1 != 0 and ia != 0: continue
                if p2 == 2 and ia == 1: continue
                if p1 == 2 and ib == 1: continue
                kc = min(max_k, ln // 2)
                for k in range(kc+1):
                    w = dp[state][k]
                    if w: counts[ln][k] = add_mod(counts[ln][k], w)
            if ln == max_len: break

            ndp = [[0]*(max_k+1) for _ in range(SC)]
            kc = min(max_k, (ln+1)//2)
            for state in range(SC):
                p2 = state // 3; p1 = state % 3
                for k in range(kc+1):
                    w = dp[state][k]
                    if w == 0: continue
                    for cur in range(3):
                        if p1 != 0 and cur != 0: continue
                        if p2 == 2 and cur == 1: continue
                        nk = k + (cur != 0)
                        if nk > max_k: continue
                        ns = 3*p1 + cur
                        ndp[ns][nk] = add_mod(ndp[ns][nk], w)
            dp = ndp

    # Factorials
    mf = 2*n_max
    fact = [1]*(mf+1)
    for i in range(1, mf+1): fact[i] = mul_mod(fact[i-1], i)
    inv_fact = [1]*(mf+1)
    inv_fact[mf] = mod_pow(fact[mf], MOD-2)
    for i in range(mf, 0, -1): inv_fact[i-1] = mul_mod(inv_fact[i], i)
    pow4 = [1]*(n_max+1)
    for i in range(1, n_max+1): pow4[i] = mul_mod(pow4[i-1], 4)

    def falling(n, k): return mul_mod(fact[n], inv_fact[n-k])

    ans = 0
    for n in range(2, n_max+1):
        total = 0
        for k in range(n+1):
            pw = counts[2*n][k]
            if pw == 0: continue
            rem = 2*n - 2*k
            term = mul_mod(pw, falling(n, k))
            term = mul_mod(term, pow4[k])
            term = mul_mod(term, mul_mod(fact[rem], fact[rem]))
            total = add_mod(total, term) if k % 2 == 0 else sub_mod(total, term)
        ans = add_mod(ans, mul_mod(2, total))

    return str(ans)

if __name__ == '__main__':
    print(solve())
