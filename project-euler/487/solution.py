import math
import sys

def mod_pow(base, exp, mod):
    return pow(base, exp, mod)

def mod_inv(x, p):
    return mod_pow(x, p - 2, p)

def add_mod(a, b, p):
    c = a + b
    return c % p if (c >= p or c < a) else c

def sub_mod(a, b, p):
    return a - b if a >= b else a + p - b

def is_prime_64(n):
    if n < 2: return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if n == p: return True
        if n % p == 0: return False
    
    d = n - 1
    s = 0
    while (d & 1) == 0:
        d >>= 1
        s += 1
        
    def witness(a):
        if a % n == 0: return False
        x = mod_pow(a, d, n)
        if x == 1 or x == n - 1: return False
        for _ in range(1, s):
            x = (x * x) % n
            if x == n - 1: return False
        return True
        
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        if witness(a): return False
    return True

def lagrange_from_0_to_m(y, m, x, fac, invfac, p):
    if x <= m:
        return y[x]
        
    pref = [1] * (m + 2)
    suf = [1] * (m + 2)
    
    for i in range(m + 1):
        pref[i + 1] = (pref[i] * sub_mod(x, i, p)) % p
    for i in range(m, -1, -1):
        suf[i] = (suf[i + 1] * sub_mod(x, i, p)) % p
        
    out = 0
    for i in range(m + 1):
        num = (pref[i] * suf[i + 1]) % p
        den = (invfac[i] * invfac[m - i]) % p
        if (m - i) & 1:
            den = 0 if den == 0 else p - den
        term = (y[i] * num) % p
        term = (term * den) % p
        out = add_mod(out, term, p)
    return out

def power_sum_mod(exp, n, p, fac, invfac):
    m = exp + 1
    y = [0] * (m + 1)
    for i in range(1, m + 1):
        pw = mod_pow(i, exp, p)
        y[i] = add_mod(y[i - 1], pw, p)
    return lagrange_from_0_to_m(y, m, n % p, fac, invfac, p)

def S_mod_prime(k, n, p):
    max_m = k + 2
    fac = [1] * (max_m + 1)
    for i in range(1, max_m + 1):
        fac[i] = (fac[i - 1] * i) % p
        
    invfac = [1] * (max_m + 1)
    invfac[max_m] = mod_inv(fac[max_m], p)
    for i in range(max_m, 0, -1):
        invfac[i - 1] = (invfac[i] * i) % p
        
    fk = power_sum_mod(k, n, p, fac, invfac)
    fk1 = power_sum_mod(k + 1, n, p, fac, invfac)
    n1 = (n + 1) % p
    part = (n1 * fk) % p
    return sub_mod(part, fk1, p)

def solve_impl(k, n, p_lo, p_hi):
    total = 0
    for p in range(p_lo, p_hi + 1):
        if not is_prime_64(p):
            continue
        total += S_mod_prime(k, n, p)
    return total

def solve():
    return str(solve_impl(10000, 1000000000000, 2000000000, 2000002000))

if __name__ == '__main__':
    print(solve())
