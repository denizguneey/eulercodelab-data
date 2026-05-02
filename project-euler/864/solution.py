import math

def solve():
    TARGET = 123567101113; B = 60000000

    def mod_pow(base, exp, mod):
        r = 1; base %= mod
        while exp > 0:
            if exp & 1: r = r * base % mod
            base = base * base % mod; exp >>= 1
        return r

    def egcd(a, b):
        if b == 0: return a, 1, 0
        g, x1, y1 = egcd(b, a%b)
        return g, y1, x1 - (a//b)*y1

    def mod_inv(a, m):
        g, x, _ = egcd(a % m, m)
        return x % m if g == 1 else 0

    def sqrt_m1_mod_p(p):
        for b in range(2, p):
            if mod_pow(b, (p-1)//2, p) == p-1:
                return mod_pow(b, (p-1)//4, p)
        return -1

    # Build prime roots for p ≡ 1 (mod 4) up to B
    sieve = bytearray(b'\x01')*(B+1); sieve[0] = sieve[1] = 0
    for i in range(2, int(B**0.5)+1):
        if sieve[i]:
            for j in range(i*i, B+1, i): sieve[j] = 0
    prime_roots = []
    for p in range(5, B+1):
        if sieve[p] and p % 4 == 1:
            r0 = sqrt_m1_mod_p(p); p2 = p*p
            m = (r0*r0+1)//p; inv = mod_pow(2*r0%p, p-2, p)
            k = (p - m%p) % p; k = k*inv%p
            r = r0 + p*k
            prime_roots.append((p, p2, r, p2-r))

    # Small primes for Mobius
    slp = []; sp_sieve = bytearray(b'\x01')*400001; sp_sieve[0] = sp_sieve[1] = 0
    for i in range(2, 400001):
        if sp_sieve[i]:
            slp.append(i)
            for j in range(i*i, 400001, i): sp_sieve[j] = 0

    def count_sols(n, mod, roots):
        q = n // mod; s = n - q*mod
        return q*len(roots) + sum(1 for r in roots if r <= s)

    def combine(roots, pr, mod_old):
        _, p2, r1, r2 = pr; inv = mod_inv(mod_old % p2, p2)
        out = []
        for ro in roots:
            rm = ro % p2
            for rn in (r1, r2):
                diff = (rn - rm) % p2
                t = diff * inv % p2
                out.append(ro + mod_old * t)
        return out

    def dfs1(si, d, d2, roots, sign, n, total):
        for i in range(si, len(prime_roots)):
            p, p2, r1, r2 = prime_roots[i]
            if p > B or d > B // p: break
            nd = d*p; nd2 = nd*nd
            nr = combine(roots, prime_roots[i], d2)
            term = count_sols(n, nd2, nr)
            ns = -sign; total[0] += ns * term
            dfs1(i+1, nd, nd2, nr, ns, n, total)

    total1 = [0]
    for i in range(len(prime_roots)):
        p, p2, r1, r2 = prime_roots[i]
        if p > B: break
        roots = [r1, r2]; term = count_sols(TARGET, p2, roots)
        total1[0] -= term
        dfs1(i+1, p, p2, roots, -1, TARGET, total1)

    # Part 2: Pell equation
    def solve_neg_pell(k, n):
        a0 = int(k**0.5)
        while (a0+1)**2 <= k: a0 += 1
        while a0*a0 > k: a0 -= 1
        if a0*a0 == k: return None
        m = 0; d = 1; a = a0
        pp1, qp1 = 1, 0; pc, qc = a0, 1
        if pc > n: return None
        for step in range(1, 10000):
            m = d*a - m; d = (k - m*m)//d; a = (a0 + m)//d
            pn = a*pc + pp1; qn = a*qc + qp1
            pp1, qp1 = pc, qc; pc, qc = pn, qn
            if d == 1 and a == 2*a0:
                if step%2 == 1 and pp1 <= n and qp1 <= n: return pp1, qp1
                return None
            if pc > n: return None
        return None

    def mobius_sf(y):
        mu = 1; tmp = y
        for p in slp:
            if p*p > tmp: break
            if tmp%p == 0:
                tmp //= p
                if tmp%p == 0: return 0
                mu = -mu
        if tmp > 1: mu = -mu
        return mu

    k_max = (TARGET*TARGET + 1) // (B*B)
    valid = bytearray(b'\x01')*(k_max+1); valid[0] = 0
    ksv = bytearray(b'\x01')*(k_max+1); ksv[0] = ksv[1] = 0
    for i in range(2, k_max+1):
        if ksv[i]:
            if i%4 == 3:
                for j in range(i, k_max+1, i): valid[j] = 0
            for j in range(i*i, k_max+1, i): ksv[j] = 0

    total2 = 0
    for k in range(1, k_max+1):
        if not valid[k]: continue
        s = int(k**0.5)
        if s*s == k: continue
        res = solve_neg_pell(k, TARGET)
        if res is None: continue
        x0, y0 = res
        X_mul = x0*x0 + k*y0*y0; Y_mul = 2*x0*y0
        x, y = x0, y0
        while x <= TARGET:
            if y > B:
                mu = mobius_sf(y)
                if mu != 0: total2 += mu
            xn = x*X_mul + y*Y_mul*k; yn = x*Y_mul + y*X_mul
            if xn > TARGET: break
            x, y = xn, yn

    return str(TARGET + total1[0] + total2)

if __name__ == '__main__':
    print(solve())
