import math
import random

def mul_mod_u64(a, b, mod):
    return (a * b) % mod

def pow_mod_u64(base, exp, mod):
    return pow(base, exp, mod)

def is_prime_u64(n):
    if n < 2:
        return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if n == p:
            return True
        if n % p == 0:
            return False
            
    d = n - 1
    s = 0
    while (d & 1) == 0:
        d >>= 1
        s += 1
        
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        if a % n == 0:
            continue
        x = pow_mod_u64(a % n, d, n)
        if x == 1 or x == n - 1:
            continue
        witness = True
        for _ in range(1, s):
            x = mul_mod_u64(x, x, n)
            if x == n - 1:
                witness = False
                break
        if witness:
            return False
    return True

def pollard_rho(n, rng):
    if (n & 1) == 0:
        return 2
    if n % 3 == 0:
        return 3
        
    while True:
        c = rng.randint(2, n - 2)
        x = rng.randint(2, n - 2)
        y = x
        d = 1
        
        def f(v):
            return (v * v + c) % n
            
        while d == 1:
            x = f(x)
            y = f(f(y))
            diff = x - y if x > y else y - x
            d = math.gcd(diff, n)
            
        if d != n:
            return d

def factor_u64(n, factors, rng):
    if n == 1:
        return
    if is_prime_u64(n):
        factors[n] = factors.get(n, 0) + 1
        return
    d = pollard_rho(n, rng)
    factor_u64(d, factors, rng)
    factor_u64(n // d, factors, rng)

def isqrt_u128(x):
    if x == 0:
        return 0
    r = int(math.sqrt(x))
    while (r + 1) * (r + 1) <= x:
        r += 1
    while r * r > x:
        r -= 1
    return r

def triangle_u128(m):
    return (m * (m + 1)) // 2

def next_triangle_state(m, rng):
    a = m
    b = m + 1
    
    fac = {}
    factor_u64(a, fac, rng)
    factor_u64(b, fac, rng)
    
    pf = list(fac.items())
    p = m * (m + 1)
    root = isqrt_u128(p)
    
    best_u = [0]
    
    def dfs(idx, cur):
        if idx == len(pf):
            if cur > root:
                return
            v = p // cur
            if ((cur + v) & 1) == 1 and v > cur + 1 and cur > best_u[0]:
                best_u[0] = cur
            return
            
        prime, exp = pf[idx]
        val = 1
        for _ in range(exp + 1):
            dfs(idx + 1, cur * val)
            val *= prime
            
    dfs(0, 1)
    
    v = p // best_u[0]
    jump = (v - best_u[0] - 1) // 2
    next_m = (best_u[0] + v - 1) // 2
    return jump, next_m

def solve_kth_triangle_hit(k):
    rng = random.Random(0xC0FFEE)
    
    hit = 1
    index = 0
    m = 2
    
    while hit < k:
        jump, next_m = next_triangle_state(m, rng)
        index += jump
        m = next_m
        hit += 1
        
    return index, m

def solve():
    idx70, _ = solve_kth_triangle_hit(70)
    return str(idx70)

if __name__ == "__main__":
    idx10, m10 = solve_kth_triangle_hit(10)
    assert idx10 == 2964
    assert triangle_u128(m10) == 1439056
    print(solve())
