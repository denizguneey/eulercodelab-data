def solve():
    MOD = 1000000007
    n_limit = 10000000

    def mod_pow(base, exp, mod=MOD):
        r = 1; base %= mod
        while exp > 0:
            if exp & 1: r = r * base % mod
            base = base * base % mod
            exp >>= 1
        return r

    def tonelli_shanks(n, p):
        if p == 2: return n & 1
        if n == 0: return 0
        if mod_pow(n, (p-1)//2, p) != 1: return 0
        if p % 4 == 3: return mod_pow(n, (p+1)//4, p)
        q, s = p-1, 0
        while q % 2 == 0: q //= 2; s += 1
        z = 2
        while mod_pow(z, (p-1)//2, p) != p-1: z += 1
        m, c, t, r = s, mod_pow(z,q,p), mod_pow(n,q,p), mod_pow(n,(q+1)//2,p)
        while t != 1:
            tt, i = t, 0
            while tt != 1 and i < m: tt = tt*tt%p; i += 1
            b = mod_pow(c, 1<<(m-i-1), p)
            r = r*b%p; t = t*b%p*b%p; c = b*b%p; m = i
        return r

    max_m = n_limit + 1
    remaining = [0]*(max_m+1)
    q_value = [1]*(max_m+1)
    for m in range(max_m+1): remaining[m] = m*m+1

    spf = list(range(max_m+1))
    for p in range(2, int(max_m**0.5)+1):
        if spf[p] == p:
            for q in range(p*p, max_m+1, p):
                if spf[q] == q: spf[q] = p
    primes = [i for i in range(2, max_m+1) if spf[i] == i]

    def apply_prime(p, idx):
        v = remaining[idx]
        if v % p != 0: return
        pp = 1
        while v % p == 0: v //= p; pp = pp*p%MOD
        remaining[idx] = v
        q_value[idx] = q_value[idx] * ((1+pp)%MOD) % MOD

    for p in primes:
        if p == 2:
            for idx in range(1, max_m+1, 2): apply_prime(2, idx)
            continue
        if p % 4 != 1: continue
        root = tonelli_shanks(p-1, p)
        if root == 0: continue
        root2 = (p-root)%p
        for idx in range(root, max_m+1, p): apply_prime(p, idx)
        if root2 != root:
            for idx in range(root2, max_m+1, p): apply_prime(p, idx)

    for m in range(max_m+1):
        if remaining[m] > 1:
            q_value[m] = q_value[m] * ((1+remaining[m]%MOD)%MOD) % MOD

    inv9 = mod_pow(9, MOD-2)
    even_adj = 5*inv9%MOD
    answer = 0
    for n in range(1, n_limit+1):
        q1 = q_value[n-1]; q2 = q_value[n+1]
        qt = q1*q2%MOD
        if n % 2 == 0: qt = qt*even_adj%MOD
        nm = n%MOD; n4p4 = (nm*nm%MOD*nm%MOD*nm+4)%MOD
        answer = (answer + qt + MOD - n4p4) % MOD

    return str(answer)

if __name__ == '__main__':
    print(solve())
