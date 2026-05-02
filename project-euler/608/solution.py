def solve():
    MOD = 1000000007
    FACT = 200; N = 1000000000000; SL = 1000000

    def mod_norm(x):
        x %= MOD
        return x + MOD if x < 0 else x
    def mod_mul(a, b): return a * b % MOD
    def mod_pow(base, exp):
        r = 1; base = mod_norm(base)
        while exp > 0:
            if exp & 1: r = mod_mul(r, base)
            base = mod_mul(base, base); exp >>= 1
        return r

    # Sieve smallest primes up to FACT
    primes = []
    sieve = bytearray(b'\x01')*(FACT+1); sieve[0] = sieve[1] = 0
    for p in range(2, FACT+1):
        if sieve[p]:
            primes.append(p)
            for q in range(p, FACT+1, p): sieve[q] = 0

    def exp_in_fact(p, n):
        e = 0; m = n
        while m > 0: m //= p; e += m
        return e

    # Build small prefix tau
    spt = [0]*SL
    for d in range(1, SL):
        for m in range(d, SL, d): spt[m] += 1
    for i in range(1, SL): spt[i] = (spt[i] + spt[i-1]) % MOD

    cache = {}
    def prefix_tau(n):
        if n < SL: return spt[n]
        if n in cache: return cache[n]
        s = 0; x = 1
        while x*x <= n: s += n//x; x += 1
        val = mod_norm((2*s - (x-1)*(x-1)) % MOD)
        cache[n] = val; return val

    def tri(x): return x*(x+1)//2

    ds = [0]*len(primes); k = 1
    for i in range(len(primes)):
        e = exp_in_fact(primes[i], FACT)
        te = tri(e) % MOD; tep1 = tri(e+1) % MOD
        ds[i] = mod_mul(te, mod_pow(tep1, MOD-2))
        k = mod_mul(k, tep1)

    ans = [0]
    def dfs(acc, start_idx, d, sign):
        term = mod_mul(d, prefix_tau(N // acc))
        ans[0] = mod_norm(ans[0] + term * sign)
        for j in range(start_idx, len(primes)):
            p = primes[j]
            if acc > N // p: break
            dfs(acc*p, j+1, mod_mul(d, ds[j]), -sign)

    dfs(1, 0, k, 1)
    return str(ans[0])

if __name__ == '__main__':
    print(solve())
