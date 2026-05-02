import math
import random
from decimal import Decimal, getcontext
import sys

getcontext().prec = 100

kMod = 409120391

class Rep:
    def __init__(self):
        self.valid = False
        self.log2v = Decimal(0)
        self.exps = []

class BestD:
    def __init__(self):
        self.valid = False
        self.log2v = Decimal(0)
        self.e2 = 0
        self.rep3 = Rep()

def mul_mod(a, b, mod):
    return (a * b) % mod

def pow_mod(a, e, mod):
    return pow(a, e, mod)

def is_prime64(n):
    if n < 2: return False
    for p in [2,3,5,7,11,13,17,19,23,29,31,37]:
        if n % p == 0: return n == p
    
    d = n - 1
    s = 0
    while (d & 1) == 0:
        d >>= 1
        s += 1
        
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        if a % n == 0: continue
        x = pow_mod(a, d, n)
        if x == 1 or x == n - 1: continue
        comp = True
        for r in range(1, s):
            x = mul_mod(x, x, n)
            if x == n - 1:
                comp = False
                break
        if comp: return False
    return True

def pollard_rho(n):
    if (n & 1) == 0: return 2
    if n % 3 == 0: return 3
    if n % 5 == 0: return 5
    
    while True:
        c = random.randint(2, n - 2)
        x = random.randint(2, n - 2)
        y = x
        d = 1
        while d == 1:
            x = (mul_mod(x, x, n) + c) % n
            y = (mul_mod(y, y, n) + c) % n
            y = (mul_mod(y, y, n) + c) % n
            diff = x - y if x > y else y - x
            d = math.gcd(diff, n)
        if d != n: return d

def factor_rec(n, out):
    if n == 1: return
    if is_prime64(n):
        out[n] = out.get(n, 0) + 1
        return
    d = pollard_rho(n)
    factor_rec(d, out)
    factor_rec(n // d, out)

odd_div_cache = {}

def odd_divisors(n):
    if n in odd_div_cache:
        return odd_div_cache[n]
    
    fac = {}
    factor_rec(n, fac)
    
    divs = [1]
    for p, e in fac.items():
        next_divs = []
        pe = 1
        for i in range(e + 1):
            for d in divs:
                next_divs.append(d * pe)
            pe *= p
        divs = next_divs
        
    odd = sorted([d for d in divs if (d & 1)])
    odd_div_cache[n] = odd
    return odd

def primes_mod4(residue, count):
    ps = []
    x = 2
    while len(ps) < count:
        if x % 4 != residue:
            x += 1
            continue
        prime = True
        for p in range(2, math.isqrt(x) + 1):
            if x % p == 0:
                prime = False
                break
        if prime:
            ps.append(x)
        x += 1
    return ps

P1 = primes_mod4(1, 80)
P3 = primes_mod4(3, 80)

def make_logs(ps):
    ln2 = Decimal(2).ln()
    return [Decimal(p).ln() / ln2 for p in ps]

L1 = make_logs(P1)
L3 = make_logs(P3)
LOG2_2 = Decimal(1)

def solve_product(P_val, primes, logs, top_cache):
    if P_val == 1:
        r = Rep()
        r.valid = True
        r.log2v = Decimal(0)
        return r
        
    if P_val in top_cache:
        return top_cache[P_val]
        
    memo = {}
    
    def dfs(rem, idx, prevf):
        if rem == 1:
            base = Rep()
            base.valid = True
            base.log2v = Decimal(0)
            return base
        if idx >= len(primes):
            return Rep()
            
        key = (rem, idx, prevf)
        if key in memo:
            return memo[key]
            
        best = Rep()
        
        divs = odd_divisors(rem)
        for f in reversed(divs):
            if f == 1 or f > prevf: continue
            e = (f - 1) // 2
            if e == 0: continue
            
            sub = dfs(rem // f, idx + 1, f)
            if not sub.valid: continue
            
            cand = Rep()
            cand.valid = True
            cand.log2v = logs[idx] * Decimal(e) + sub.log2v
            cand.exps = [e] + sub.exps
            
            if not best.valid or cand.log2v < best.log2v:
                best = cand
                
        memo[key] = best
        return best
        
    res = dfs(P_val, 0, P_val)
    top_cache[P_val] = res
    return res

cache_rep1 = {}
cache_rep3 = {}
cache_bestD = {}

def best_for_D(D):
    if D in cache_bestD:
        return cache_bestD[D]
        
    best = BestD()
    divs = odd_divisors(D)
    for a2 in divs:
        e2 = 0
        part2 = Decimal(0)
        if a2 > 1:
            e2 = (a2 + 1) // 2
            part2 = LOG2_2 * Decimal(e2)
            
        C = D // a2
        rep3 = solve_product(C, P3, L3, cache_rep3)
        if not rep3.valid: continue
        
        cur = part2 + rep3.log2v
        if not best.valid or cur < best.log2v:
            best.valid = True
            best.log2v = cur
            best.e2 = e2
            best.rep3 = rep3
            
    cache_bestD[D] = best
    return best

class QRep:
    def __init__(self):
        self.valid = False
        self.log2v = Decimal(0)
        self.rep1 = Rep()
        self.e2 = 0
        self.rep3 = Rep()

def Q_rep(n):
    S = n + 1
    best = QRep()
    divs = odd_divisors(S)
    
    for B in divs:
        rep1 = solve_product(B, P1, L1, cache_rep1)
        if not rep1.valid: continue
        
        D = (2 * S) // B - 1
        bd = best_for_D(D)
        if not bd.valid: continue
        
        cur = rep1.log2v + bd.log2v
        if not best.valid or cur < best.log2v:
            best.valid = True
            best.log2v = cur
            best.rep1 = rep1
            best.e2 = bd.e2
            best.rep3 = bd.rep3
            
    return best

def rep_mod(rep, primes, mod):
    r = 1
    for i in range(len(rep.exps)):
        r = mul_mod(r, pow_mod(primes[i], rep.exps[i], mod), mod)
    return r

def Q_mod(n):
    qr = Q_rep(n)
    r = rep_mod(qr.rep1, P1, kMod)
    r = mul_mod(r, pow_mod(2, qr.e2, kMod), kMod)
    r = mul_mod(r, rep_mod(qr.rep3, P3, kMod), kMod)
    return r

def solve():
    sys.setrecursionlimit(20000)
    ans = 0
    for k in range(1, 19):
        ans += Q_mod(10**k)
        ans %= kMod
    return str(ans)

if __name__ == "__main__":
    print(solve())
