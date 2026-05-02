import sys
import math

def mod_pow(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp >>= 1
    return result

def tonelli_shanks(n, p):
    if p == 2: return n & 1
    if n == 0: return 0
    if mod_pow(n, (p - 1) // 2, p) != 1: return 0
    if (p & 3) == 3: return mod_pow(n, (p + 1) // 4, p)
    
    q = p - 1
    s = 0
    while (q & 1) == 0:
        q >>= 1
        s += 1
        
    z = 2
    while mod_pow(z, (p - 1) // 2, p) != p - 1:
        z += 1
        
    m = s
    c = mod_pow(z, q, p)
    t = mod_pow(n, q, p)
    r = mod_pow(n, (q + 1) // 2, p)
    
    while t != 1:
        tt = t
        i = 0
        while tt != 1 and i < m:
            tt = (tt * tt) % p
            i += 1
            
        shift = m - i - 1
        b = mod_pow(c, 1 << shift, p)
        r = (r * b) % p
        b2 = (b * b) % p
        t = (t * b2) % p
        c = b2
        m = i
        
    return r

def lift_root(p, r):
    deriv = (2 * r + p - 3) % p
    inv_deriv = mod_pow(deriv, p - 2, p)
    
    fr = r * r - 3 * r - 1
    q = fr // p
    
    neg_q = -q % p
    if neg_q < 0: neg_q += p
    
    t = (neg_q * inv_deriv) % p
    return r + t * p

def solve_limit(limit):
    is_prime = bytearray([1]) * (limit + 1)
    if limit >= 0: is_prime[0] = 0
    if limit >= 1: is_prime[1] = 0
    
    for i in range(2, math.isqrt(limit) + 1):
        if is_prime[i]:
            is_prime[i*i : limit+1 : i] = bytearray([0]) * len(range(i*i, limit+1, i))
            
    residue = [False] * 13
    for i in [1, 3, 4, 9, 10, 12]:
        residue[i] = True
        
    total_sum = 0
    for p in range(2, limit + 1):
        if not is_prime[p] or p == 2 or p == 13:
            continue
            
        if not residue[p % 13]:
            continue
            
        s = tonelli_shanks(13 % p, p)
        inv2 = (p + 1) // 2
        
        r1 = ((3 + s) * inv2) % p
        r2 = ((3 + p - s) * inv2) % p
        
        n1 = lift_root(p, r1)
        n2 = lift_root(p, r2)
        total_sum += n1 if n1 < n2 else n2
        
    return total_sum

def solve():
    return str(solve_limit(10000000))

if __name__ == '__main__':
    print(solve())
