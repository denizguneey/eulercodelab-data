import math
import random
from collections import defaultdict

def solve():
    def mod_mul(a, b, m): return a * b % m
    def mod_pow(a, e, m):
        r = 1 % m
        a %= m
        while e > 0:
            if e & 1: r = r * a % m
            a = a * a % m
            e >>= 1
        return r

    def is_prime(n):
        if n < 2: return False
        for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
            if n % p == 0: return n == p
        d = n - 1; s = 0
        while d % 2 == 0: d >>= 1; s += 1
        for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
            if a % n == 0: continue
            x = mod_pow(a, d, n)
            if x == 1 or x == n - 1: continue
            w = True
            for _ in range(1, s):
                x = x * x % n
                if x == n - 1: w = False; break
            if w: return False
        return True

    def pollard_rho(n):
        if n % 2 == 0: return 2
        while True:
            c = random.randint(1, n - 1)
            x = random.randint(0, n - 1)
            y = x; d = 1
            while d == 1:
                x = (x * x + c) % n
                y = (y * y + c) % n
                y = (y * y + c) % n
                d = math.gcd(abs(x - y), n)
            if d != n: return d

    def factor(n):
        if n <= 1: return {}
        if is_prime(n): return {n: 1}
        d = pollard_rho(n)
        f1 = factor(d)
        f2 = factor(n // d)
        for p, e in f2.items():
            f1[p] = f1.get(p, 0) + e
        return f1

    def gen_divs(pf, idx, cur, out):
        if idx == len(pf):
            out.append(cur)
            return
        p, e = pf[idx]
        v = 1
        for _ in range(e + 1):
            gen_divs(pf, idx + 1, cur * v, out)
            v *= p

    def distinct_pf(n):
        pf = []
        p = 2
        while p * p <= n:
            if n % p == 0:
                pf.append(p)
                while n % p == 0: n //= p
            p += 1
        if n > 1: pf.append(n)
        return pf

    def has_exact_order(mod, ord, ord_primes):
        if mod == 1: return False
        if mod_pow(2, ord, mod) != 1: return False
        for p in ord_primes:
            if mod_pow(2, ord // p, mod) == 1: return False
        return True

    random.seed(987654321)
    ord = 60
    M = (1 << ord) - 1
    f = factor(M)
    pf = list(f.items())
    divs = []
    gen_divs(pf, 0, 1, divs)
    ord_primes = distinct_pf(ord)

    total = sum(d + 1 for d in divs if has_exact_order(d, ord, ord_primes))
    return str(total)

if __name__ == '__main__':
    print(solve())
