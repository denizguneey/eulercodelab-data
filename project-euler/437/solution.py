import math

def solve():
    limit = 100000000

    def mod_pow(base, exp, mod):
        r = 1; base %= mod
        while exp > 0:
            if exp & 1: r = r * base % mod
            base = base * base % mod
            exp >>= 1
        return r

    # SPF sieve for odd numbers
    half = limit // 2 + 1
    spf = [0] * half
    root = int(limit**0.5)
    for i in range(3, root + 1, 2):
        if spf[i >> 1] == 0:
            step = 2 * i
            for j in range(i*i, limit + 1, step):
                if spf[j >> 1] == 0: spf[j >> 1] = i

    primes = [2]
    for p in range(3, limit + 1, 2):
        if spf[p >> 1] == 0: primes.append(p)

    def tonelli_sqrt5(p):
        if p == 2: return 1
        if mod_pow(5, (p-1)//2, p) != 1: return -1
        if p % 4 == 3: return mod_pow(5, (p+1)//4, p)
        q, s = p-1, 0
        while q % 2 == 0: q //= 2; s += 1
        z = 2
        while mod_pow(z, (p-1)//2, p) != p-1: z += 1
        c = mod_pow(z, q, p); x = mod_pow(5, (q+1)//2, p)
        t = mod_pow(5, q, p); m = s
        while t != 1:
            tt, i = t, 0
            while tt != 1 and i < m: tt = tt*tt%p; i += 1
            b = mod_pow(c, 1<<(m-i-1), p)
            x = x*b%p; t = t*b%p*b%p; c = b*b%p; m = i
        return x

    def factor_unique(n):
        factors = []
        if n % 2 == 0:
            factors.append(2)
            while n % 2 == 0: n //= 2
        while n > 1:
            if n & 1:
                f = spf[n >> 1]
                if f == 0: f = n
            else: f = 2
            factors.append(f)
            while n % f == 0: n //= f
        return factors

    def is_prim_root(g, p, factors):
        phi = p - 1
        for q in factors:
            if mod_pow(g, phi // q, p) == 1: return False
        return True

    total = 0
    for p in primes:
        if p <= 3: continue
        if p == 5: total += 5; continue
        if p % 5 != 1 and p % 5 != 4: continue
        s5 = tonelli_sqrt5(p)
        if s5 < 0: continue
        inv2 = (p + 1) // 2
        r1 = (1 + s5) % p * inv2 % p
        r2 = (1 + p - s5) % p * inv2 % p
        factors = factor_unique(p - 1)
        if is_prim_root(r1, p, factors) or is_prim_root(r2, p, factors):
            total += p

    return str(total)

if __name__ == '__main__':
    print(solve())
