import math

def mul(x, y, mod):
    return (
        (x[0] * y[0] + 7 * x[1] * y[1]) % mod,
        (x[0] * y[1] + x[1] * y[0]) % mod
    )

def pow_u(exp, mod):
    result = (1, 0)
    base = (1, 1)
    e = exp
    while e > 0:
        if e & 1:
            result = mul(result, base, mod)
        base = mul(base, base, mod)
        e >>= 1
    return result

def build_spf(n):
    spf = list(range(n + 1))
    for i in range(2, int(math.isqrt(n)) + 1):
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf

def distinct_prime_factors(n, spf):
    factors = []
    while n > 1:
        p = spf[n]
        factors.append(p)
        while n % p == 0:
            n //= p
    return factors

def order_mod_prime(p, spf):
    if p == 7:
        return 7
        
    def ls():
        r = 1
        b = 7 % p
        e = (p - 1) // 2
        while e > 0:
            if e & 1:
                r = (r * b) % p
            b = (b * b) % p
            e >>= 1
        return r
        
    ls_val = ls()
    
    if ls_val == 1:
        exponent = p - 1
        factors = distinct_prime_factors(p - 1, spf)
    else:
        exponent = (p - 1) * (p + 1)
        factors = distinct_prime_factors(p - 1, spf)
        extra = distinct_prime_factors(p + 1, spf)
        factors.extend(extra)
        factors = sorted(list(set(factors)))
        
    ord_val = exponent
    for q in factors:
        while ord_val % q == 0:
            test = pow_u(ord_val // q, p)
            if test[0] == 1 and test[1] == 0:
                ord_val //= q
            else:
                break
                
    return ord_val

def G(n):
    limit = n + 1
    spf = build_spf(limit)
    ord_prime_power = [0] * (n + 1)
    
    for p in range(5, n + 1):
        if spf[p] != p:
            continue
            
        ord_val = order_mod_prime(p, spf)
        pk = p
        ord_prime_power[pk] = ord_val
        
        while pk <= n // p:
            pk *= p
            test = pow_u(ord_val, pk)
            if not (test[0] == 1 and test[1] == 0):
                ord_val *= p
            ord_prime_power[pk] = ord_val
            
    total = 0
    for x in range(2, n + 1):
        if x % 2 == 0 or x % 3 == 0:
            continue
            
        t = x
        gx = 1
        while t > 1:
            p = spf[t]
            pk = 1
            while t % p == 0:
                t //= p
                pk *= p
            gx = (gx * ord_prime_power[pk]) // math.gcd(gx, ord_prime_power[pk])
            
        total += gx
        
    return total

def solve():
    return str(G(1000000))

if __name__ == "__main__":
    print(solve())
