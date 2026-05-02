def solve():
    MOD = 1000000007; PHIMOD = MOD - 1
    n = 100000000

    def mod_pow(base, exp, mod=MOD):
        r = 1; base %= mod
        while exp > 0:
            if exp & 1: r = r * base % mod
            base = base * base % mod; exp >>= 1
        return r

    # Mobius sieve
    mu = [0]*(n+1); mu[1] = 1
    is_comp = bytearray(n+1); primes = []
    for i in range(2, n+1):
        if not is_comp[i]: primes.append(i); mu[i] = -1
        for p in primes:
            if i*p > n: break
            is_comp[i*p] = 1
            if i % p == 0: mu[i*p] = 0; break
            mu[i*p] = -mu[i]

    # Floor quotient ranges
    import math
    ranges = []; l = 1
    while l <= n:
        q = n // l; r = n // q; ranges.append((l, r, q)); l = r + 1

    # Precompute superfactorial at needed points
    needed = sorted(set([0] + [q-1 for _,_,q in ranges]))
    sf_map = {}; fact = 1; sfac = 1; ptr = 0
    if needed[ptr] == 0: sf_map[0] = 1; ptr += 1
    for t in range(1, needed[-1]+1):
        fact = fact * t % MOD; sfac = sfac * fact % MOD
        while ptr < len(needed) and needed[ptr] == t:
            sf_map[t] = sfac; ptr += 1

    ans = 1
    for l, r, q in ranges:
        f = q * (q-1) // 2 % PHIMOD
        pp = pn = 1; sm = 0
        for d in range(l, r+1):
            m = mu[d]
            if m == 0: continue
            sm += m
            if m > 0: pp = pp * d % MOD
            else: pn = pn * d % MOD
        if f:
            ans = ans * mod_pow(pp, f) % MOD
            ans = ans * mod_pow(pn, (PHIMOD - f) % PHIMOD) % MOD
        esf = sm % PHIMOD
        if esf < 0: esf += PHIMOD
        sf = sf_map[q-1]
        ans = ans * mod_pow(sf, esf) % MOD

    return str(ans)

if __name__ == '__main__':
    print(solve())
