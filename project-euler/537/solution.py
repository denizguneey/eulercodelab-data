def solve():
    MOD = 1004535809  # 2^21 * 479 + 1
    PROOT = 3
    N, K = 20000, 20000

    def mod_pow(a, e):
        r = 1; a %= MOD
        while e:
            if e & 1: r = r * a % MOD
            a = a * a % MOD; e >>= 1
        return r

    def ntt(a, invert):
        n = len(a)
        j = 0
        for i in range(1, n):
            bit = n >> 1
            while j & bit: j ^= bit; bit >>= 1
            j ^= bit
            if i < j: a[i], a[j] = a[j], a[i]
        l = 2
        while l <= n:
            wlen = mod_pow(PROOT, (MOD-1)//l)
            if invert: wlen = mod_pow(wlen, MOD-2)
            for i in range(0, n, l):
                w = 1
                for k in range(l//2):
                    u = a[i+k]; v = w * a[i+k+l//2] % MOD
                    a[i+k] = (u+v) % MOD
                    a[i+k+l//2] = (u-v) % MOD
                    w = w * wlen % MOD
            l <<= 1
        if invert:
            inv_n = mod_pow(n, MOD-2)
            for i in range(n): a[i] = a[i] * inv_n % MOD

    def conv(a, b, max_deg):
        need = len(a)+len(b)-1
        need = min(need, max_deg+1)
        nn = 1
        while nn < len(a)+len(b)-1: nn <<= 1
        fa = list(a) + [0]*(nn-len(a))
        fb = list(b) + [0]*(nn-len(b))
        ntt(fa, False); ntt(fb, False)
        for i in range(nn): fa[i] = fa[i]*fb[i]%MOD
        ntt(fa, True)
        return fa[:need]

    def poly_pow(base, exp, max_deg):
        res = [1]
        while exp > 0:
            if exp & 1: res = conv(res, base, max_deg)
            exp >>= 1
            if exp: base = conv(base, base, max_deg)
        return res + [0]*(max_deg+1-len(res))

    # Sieve primes
    limit = 300000
    sieve = bytearray(b'\x01')*(limit+1); sieve[0]=sieve[1]=0
    for i in range(2, int(limit**0.5)+1):
        if sieve[i]:
            for j in range(i*i, limit+1, i): sieve[j] = 0
    primes = [i for i in range(2, limit+1) if sieve[i]]

    a = [0]*(N+1); a[0] = 1
    for i in range(1, N+1): a[i] = primes[i] - primes[i-1]

    pk = poly_pow(a, K, N)
    return str(pk[N])

if __name__ == '__main__':
    print(solve())
