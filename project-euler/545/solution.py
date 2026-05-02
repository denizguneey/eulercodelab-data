import math

kDenTarget = 20010
kL = 308

def sieve_primes(n):
    is_comp = [False] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if not is_comp[i]:
            primes.append(i)
            if i <= n // i:
                for j in range(i * i, n + 1, i):
                    is_comp[j] = True
    return primes

def is_prime_u64(x, primes):
    if x < 2: return False
    for p in primes:
        if p * p > x: break
        if x % p == 0: return x == p
    return True

def mod_inv(a, mod):
    return pow(a, -1, mod)

def bernoulli_denominator_even_k(k, primes_small):
    fac = []
    x = k
    for p in primes_small:
        if p * p > x: break
        if x % p == 0:
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            fac.append((p, e))
    if x > 1: fac.append((x, 1))
    
    divs = [1]
    for p, e in fac:
        cur_len = len(divs)
        pe = 1
        for i in range(1, e + 1):
            pe *= p
            for j in range(cur_len):
                divs.append(divs[j] * pe)
                
    den = 1
    for d in divs:
        cand = d + 1
        if is_prime_u64(cand, primes_small):
            den *= cand
    return den

def brute_F_10():
    lim = 200000
    primes = sieve_primes(int(math.sqrt(lim + 1)) + 5)
    found = 0
    m = 1
    while kL * m <= lim:
        k = kL * m
        den = bernoulli_denominator_even_k(k, primes)
        if den == kDenTarget:
            found += 1
            if found == 10:
                return k
        m += 1
    return 0

def kth_multiplier_with_den(M, kth):
    pmax = kL * M + 1
    qmax = int(math.sqrt(pmax)) + 2
    primes = sieve_primes(qmax)
    
    forbidden = bytearray(M + 1)
    
    gs = [2, 4, 14, 22, 28, 44, 154, 308]
    for g in gs:
        maxp_g = g * M + 1
        qlim = int(math.sqrt(maxp_g)) + 1
        
        is_prime_u = bytearray(b'\x01' * (M + 1))
        is_prime_u[0] = 0
        
        for q in primes:
            if q > qlim: break
            if g % q == 0: continue
            
            a = g % q
            inv = mod_inv(a, q)
            u0 = ((q - 1) * inv) % q
            
            u_start = (q * q - 1 + g - 1) // g
            u = u0
            if u < u_start:
                u += ((u_start - u + q - 1) // q) * q
            
            if u <= M:
                end_range = M + 1
                count = (end_range - u + q - 1) // q
                is_prime_u[u:end_range:q] = b'\x00' * count
                
        div = kL // g
        
        for u in range(1, M + 1):
            if not is_prime_u[u]: continue
            p = g * u + 1
            if p in (2, 3, 5, 23, 29): continue
            r = u // math.gcd(u, div)
            if r <= M:
                forbidden[r] = 1
                
    invalid = bytearray(M + 1)
    for r in range(2, M + 1):
        if not forbidden[r]: continue
        end_range = M + 1
        count = (end_range - r + r - 1) // r
        invalid[r:end_range:r] = b'\x01' * count
            
    cnt = 0
    for m in range(1, M + 1):
        if not invalid[m]:
            cnt += 1
            if cnt == kth:
                return m
    return 0
    
def solve_F_1e5():
    kth = 100000
    M = 4000000
    while True:
        m = kth_multiplier_with_den(M, kth)
        if m != 0: return kL * m
        M *= 2

def solve():
    return str(solve_F_1e5())

if __name__ == '__main__':
    print(solve())
