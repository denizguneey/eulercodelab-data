import math

def solve():
    MOD = 1000000007
    m = 200

    def mod_pow(base, exp, mod=MOD):
        r = 1; base %= mod
        while exp > 0:
            if exp & 1: r = r * base % mod
            base = base * base % mod; exp >>= 1
        return r

    def mod_inv(a, mod=MOD): return mod_pow(a, mod-2, mod)

    max_n = 10 * m * m * m
    # SPF sieve
    spf = list(range(max_n+1))
    for i in range(2, int(max_n**0.5)+1):
        if spf[i] == i:
            for j in range(i*i, max_n+1, i):
                if spf[j] == j: spf[j] = i

    def euler_phi(n):
        r = n; x = n
        while x > 1:
            p = spf[x]
            while x % p == 0: x //= p
            r -= r // p
        return r

    def pfm(n):
        f = []
        while n > 1:
            p = spf[n]; f.append(p); n //= p
        return f

    def mult_order(a, mm):
        if math.gcd(a, mm) != 1: return 0
        if mm == 1: return 1
        order = euler_phi(mm)
        factors = sorted(set(pfm(order)))
        for p in factors:
            while order % p == 0 and pow(a, order//p, mm) == 1: order //= p
        return order

    def min_l_mag(p, q):
        limit = (q + p - 1) // p; pw = 1; l = 1
        while pw < limit: pw *= 10; l += 1
        return l

    def solve_pair(u, v):
        p = u*u*u; q = v*v*v
        if p >= 10*q: return 0
        k_val = 10*q - p; min_l = min_l_mag(p, q)
        best_l = float('inf'); best_d = 10
        for d in range(1, 10):
            if p*(d+1) >= 10*q: continue
            g = math.gcd(k_val, d); mp = k_val // g
            if math.gcd(10, mp) != 1: continue
            lb = mult_order(10, mp)
            if lb == 0: continue
            lc = ((min_l + lb - 1) // lb) * lb
            if lc < best_l or (lc == best_l and d < best_d):
                best_l = lc; best_d = d
        if best_l == float('inf'): return 0
        t10l = mod_pow(10, best_l)
        t1 = best_d % MOD * (q % MOD) % MOD
        t2 = (t10l + MOD - 1) % MOD
        ki = mod_inv(k_val % MOD)
        return t1 * t2 % MOD * ki % MOD

    total = 0
    for u in range(1, m+1):
        for v in range(1, m+1):
            if math.gcd(u, v) == 1:
                total = (total + solve_pair(u, v)) % MOD
    return str(total)

if __name__ == '__main__':
    print(solve())
