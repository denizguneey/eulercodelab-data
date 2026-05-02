def solve():
    MOD = 1000000007
    k_target = 100000; n_target = 10000000000000000

    def mod_pow(base, exp, mod=MOD):
        r = 1; base %= mod
        while exp > 0:
            if exp & 1: r = r * base % mod
            base = base * base % mod; exp >>= 1
        return r

    def mod_inv(n, mod=MOD): return mod_pow(n, mod-2, mod)

    phi = MOD - 1
    m = n_target // k_target
    m_exp = m % phi
    lam = (mod_pow(2, m_exp) - 2 + MOD) % MOD

    fact = [1]*(k_target+1)
    for i in range(1, k_target+1): fact[i] = fact[i-1]*i % MOD
    inv_fact = [1]*(k_target+1)
    inv_fact[k_target] = mod_inv(fact[k_target])
    for i in range(k_target-1, -1, -1): inv_fact[i] = inv_fact[i+1]*(i+1) % MOD

    # NTT via 3 NTT primes + CRT
    P1, R1, RPW1 = 998244353, 3, 1<<23
    P2, R2, RPW2 = 1004535809, 3, 1<<21
    P3, R3, RPW3 = 469762049, 3, 1<<26

    def ntt(a, inv_flag, p, root):
        n = len(a)
        j = 0
        for i in range(1, n):
            bit = n >> 1
            while j & bit: j ^= bit; bit >>= 1
            j ^= bit
            if i < j: a[i], a[j] = a[j], a[i]
        ln = 2
        while ln <= n:
            wl = pow(root, (p-1)//ln, p)
            if inv_flag: wl = pow(wl, p-2, p)
            for i in range(0, n, ln):
                w = 1
                for jj in range(ln//2):
                    u = a[i+jj]; v = a[i+jj+ln//2]*w % p
                    a[i+jj] = (u+v) % p; a[i+jj+ln//2] = (u-v) % p
                    w = w*wl % p
            ln <<= 1
        if inv_flag:
            ni = pow(n, p-2, p)
            for i in range(n): a[i] = a[i]*ni % p

    def conv(a, b, p, root):
        n = 1
        while n < len(a)+len(b): n <<= 1
        fa = list(a) + [0]*(n-len(a)); fb = list(b) + [0]*(n-len(b))
        ntt(fa, False, p, root); ntt(fb, False, p, root)
        for i in range(n): fa[i] = fa[i]*fb[i] % p
        ntt(fa, True, p, root)
        return fa

    def crt3(a1, a2, a3):
        m1, m2, m3 = P1, P2, P3; M = m1*m2
        inv_m1_m2 = pow(m1, m2-2, m2)
        x = a1 + (a2-a1) % m2 * inv_m1_m2 % m2 * m1
        Mm3 = M % m3; inv_M = pow(Mm3, m3-2, m3)
        k = (a3 - x%m3) % m3 * inv_M % m3
        return (x + k*M) % MOD

    def conv_crt(a, b):
        r1 = conv(a, b, P1, R1); r2 = conv(a, b, P2, R2); r3 = conv(a, b, P3, R3)
        return [crt3(r1[i], r2[i], r3[i]) for i in range(len(r1))]

    # H[i] = invFact[i]^16
    H = [mod_pow(inv_fact[i], 16) for i in range(k_target+1)]
    H2 = conv_crt(H, H)

    U = [0]*(k_target+1)
    for s in range(k_target+1):
        A_s = mod_pow(fact[s], 16) * H2[s] % MOD
        U[s] = A_s * inv_fact[s] % MOD

    V = [0]*(k_target+1); lp = 1
    for j in range(k_target+1):
        V[j] = lp * inv_fact[j] % MOD; lp = lp * lam % MOD

    W = conv_crt(U, V)
    return str(fact[k_target] * W[k_target] % MOD)

if __name__ == '__main__':
    print(solve())
