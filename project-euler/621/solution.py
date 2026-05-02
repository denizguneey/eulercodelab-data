import math
import random

def mod_pow(a, e, mod):
    return pow(a, e, mod)

def is_prime(n):
    if n < 2: return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if n % p == 0: return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    def witness(a):
        if a % n == 0: return False
        x = pow(a, d, n)
        if x == 1 or x == n - 1: return False
        for _ in range(1, s):
            x = pow(x, 2, n)
            if x == n - 1: return False
        return True
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        if witness(a): return False
    return True

def pollard_rho(n):
    if n % 2 == 0: return 2
    while True:
        c = random.randint(0, n - 1)
        x = random.randint(0, n - 1)
        y = x
        d = 1
        f = lambda v: (v * v + c) % n
        while d == 1:
            x = f(x)
            y = f(f(y))
            diff = x - y if x > y else y - x
            d = math.gcd(diff, n)
        if d != n: return d

def factor_rec(n, out):
    if n == 1: return
    if is_prime(n):
        out[n] = out.get(n, 0) + 1
        return
    d = pollard_rho(n)
    factor_rec(d, out)
    factor_rec(n // d, out)

def tonelli_shanks(n, p):
    if n == 0: return 0
    if p == 2: return n
    if pow(n, (p - 1) // 2, p) != 1: return 0
    if p % 4 == 3: return pow(n, (p + 1) // 4, p)
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1: z += 1
    c = pow(z, q, p)
    r = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s
    while t != 1:
        i = 1
        tt = (t * t) % p
        while i < m and tt != 1:
            tt = (tt * tt) % p
            i += 1
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        b2 = (b * b) % p
        t = (t * b2) % p
        c = b2
        m = i
    return r

def roots_mod_prime_power(D, p, e):
    pe = p ** e
    Dmod = D % p
    if Dmod == 0:
        if e == 1: return [0]
        return []
    n = Dmod
    r = tonelli_shanks(n, p)
    if r == 0: return []
    pk = p
    for k in range(1, e):
        pk1 = pk * p
        Dmod_k1 = D % pk1
        r2 = (r * r) % pk1
        diff = (Dmod_k1 - r2) % pk1
        delta = diff // pk
        inv = pow((2 * r) % p, -1, p)
        t = (delta * inv) % p
        r += t * pk
        pk = pk1
    r %= pe
    r2 = (pe - r) % pe
    if r2 == r: return [r]
    return [r, r2]

def sieve_spf(n):
    spf = [0] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
        for p in primes:
            v = p * i
            if v > n: break
            spf[v] = p
            if p == spf[i]: break
    return spf

def factorize_small(x, spf):
    f = []
    while x > 1:
        p = spf[x]
        e = 0
        while x % p == 0:
            x //= p
            e += 1
        f.append((p, e))
    return f

def class_number_odd_fundamental(D):
    absD = -D
    maxA = int(math.sqrt(absD / 3.0))
    while 3 * (maxA + 1)**2 <= absD: maxA += 1
    while 3 * maxA**2 > absD: maxA -= 1
    lim = maxA
    spf = sieve_spf(lim)
    h = 0
    for a in range(1, lim + 1, 2):
        fac = factorize_small(a, spf)
        mod = 1
        roots = [0]
        ok = True
        for p, e in fac:
            pe = p ** e
            rpe = roots_mod_prime_power(D, p, e)
            if not rpe:
                ok = False
                break
            inv = pow(mod % pe, -1, pe)
            nxt = []
            for x in roots:
                xpe = x % pe
                for y in rpe:
                    t = (y - xpe) % pe
                    t = (t * inv) % pe
                    nxt.append(x + mod * t)
            mod *= pe
            roots = nxt
        if not ok: continue
        for r in roots:
            bmod = r
            if bmod % 2 == 0: bmod += a
            bmod %= (2 * a)
            b = bmod
            if b > a: b -= 2 * a
            if b == -a: b = a
            
            num = b * b - D
            den = 4 * a
            if num % den != 0: continue
            c = num // den
            if a > c: continue
            if (a == c or abs(b) == a) and b < 0: continue
            h += 1
    return h

def jacobi_symbol(a, n):
    a %= n
    if a < 0: a += n
    s = 1
    while a != 0:
        while a % 2 == 0:
            a //= 2
            r = n % 8
            if r == 3 or r == 5: s = -s
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: s = -s
        a %= n
    return s if n == 1 else 0

def kronecker_D_over_2(D):
    r = D % 8
    if r in (1, 7): return 1
    if r in (3, 5): return -1
    return 0

def sigma_prime_power(p, e):
    pe1 = p ** (e + 1)
    return (pe1 - 1) // (p - 1)

def r3_sum_of_three_squares(N):
    pf = {}
    factor_rec(N, pf)
    m = 1
    f_pf = {}
    for p, e in pf.items():
        if e % 2 == 1: m *= p
        k = e // 2
        if k > 0: f_pf[p] = k
    
    D = -m
    h = class_number_odd_fundamental(D)
    w = 6 if D == -3 else (4 if D == -4 else 2)
    one_minus = 1 - kronecker_D_over_2(D)
    
    primes = list(f_pf.keys())
    exps = list(f_pf.values())
    k_len = len(primes)
    
    S = 0
    for mask in range(1 << k_len):
        d = 1
        mu = 1
        sigma = 1
        for i in range(k_len):
            e = exps[i]
            if (mask & (1 << i)):
                d *= primes[i]
                mu = -mu
                e -= 1
            sigma *= sigma_prime_power(primes[i], e)
        chi = jacobi_symbol(D, d)
        if chi == 0: continue
        S += mu * chi * sigma
        
    t = 12 * (2 * h) * one_minus * S
    r3 = t // w
    return r3

def G(n):
    N = 8 * n + 3
    r3 = r3_sum_of_three_squares(N)
    return r3 // 8

def solve():
    n = 17526 * 1000000000
    r = G(n)
    return str(r)

if __name__ == '__main__':
    print(solve())
