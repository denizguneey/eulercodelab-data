import math

def pow10_int(e):
    return 10 ** e

def sieve_primes(limit):
    composite = [False] * (limit + 1)
    primes = []
    for i in range(2, limit + 1):
        if not composite[i]:
            primes.append(i)
            if i * i <= limit:
                for j in range(i * i, limit + 1, i):
                    composite[j] = True
    return primes

def factor_prime_powers(x, primes):
    parts = []
    for p in primes:
        if p * p > x:
            break
        if x % p != 0:
            continue
        pk = 1
        while x % p == 0:
            x //= p
            pk *= p
        parts.append(pk)
    if x > 1:
        parts.append(x)
    return parts

def mod_inv(a, mod):
    return pow(a, -1, mod)

def crt_merge(r1, m1, r2, m2):
    if m1 == 1:
        return r2 % m2, m2
    inv = mod_inv(m1 % m2, m2)
    diff = (r2 - r1) % m2
    t = (diff * inv) % m2
    mod = m1 * m2
    r = (r1 + m1 * t) % mod
    return r, mod

def solve_digits(nd):
    max_n = pow10_int(nd) - 1
    s_limit = int(math.isqrt(max_n))
    
    pow10 = [1] * (nd + 1)
    for i in range(1, nd + 1):
        pow10[i] = pow10[i - 1] * 10
        
    sieve_limit = int(math.isqrt(pow10[nd - 1] - 1)) + 10
    primes = sieve_primes(sieve_limit)
    
    seen = set()
    
    for d in range(1, nd):
        mod = pow10[d] - 1
        prime_powers = factor_prime_powers(mod, primes)
        
        residues = [(0, 1)]
        for pk in prime_powers:
            nxt = []
            for r, m in residues:
                nxt.append(crt_merge(r, m, 0, pk))
                nxt.append(crt_merge(r, m, 1 % pk, pk))
            residues = nxt
            
        s_max = min(s_limit, pow10[d] - 1)
        b_low = 1 if d == 1 else pow10[d - 1]
        p10d = pow10[d]
        
        for r0, step in residues:
            s = r0
            if s <= 1:
                need = 2 - s
                k = (need + step - 1) // step
                if k > (s_max - s) // step:
                    continue
                s += k * step
                
            while s <= s_max:
                ss = s * (s - 1)
                if ss % mod != 0:
                    s += step
                    continue
                    
                a = ss // mod
                if a == 0 or a >= s:
                    s += step
                    continue
                b = s - a
                
                if b < b_low or b >= p10d:
                    s += step
                    continue
                    
                n = s * s
                if n > max_n:
                    s += step
                    continue
                if a * p10d + b != n:
                    s += step
                    continue
                    
                seen.add(n)
                s += step
                
    return sum(seen)

def solve():
    return str(solve_digits(16))

if __name__ == "__main__":
    print(solve())
