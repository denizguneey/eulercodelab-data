import sys

sys.set_int_max_str_digits(200000)
MOD = 1000000007

class Comb:
    def __init__(self, maxI):
        self.maxI = max(0, maxI)
        self.fact = [1] * (self.maxI + 1)
        self.invfact = [1] * (self.maxI + 1)
        self.pow2 = [1] * (self.maxI + 1)
        self.inv = [0] * (self.maxI + 1)
        
        for i in range(1, self.maxI + 1):
            self.fact[i] = (self.fact[i - 1] * i) % MOD
            self.pow2[i] = (self.pow2[i - 1] * 2) % MOD
            
        self.invfact[self.maxI] = pow(self.fact[self.maxI], MOD - 2, MOD)
        for i in range(self.maxI, 0, -1):
            self.invfact[i - 1] = (self.invfact[i] * i) % MOD
            
        if self.maxI >= 1:
            self.inv[1] = 1
            for i in range(2, self.maxI + 1):
                self.inv[i] = (MOD - (MOD // i) * self.inv[MOD % i] % MOD) % MOD

def H(C, u, v, w):
    if u < 0 or v < 0 or w < 0:
        return 0
    n = u + v + w
    if ((u ^ n) & 1) or ((v ^ n) & 1) or ((w ^ n) & 1):
        return 0
        
    A = (v + w) // 2
    B = (u + w) // 2
    Cc = (u + v) // 2
    
    lo = (n + 2) // 3
    if A > lo: lo = A
    if B > lo: lo = B
    if Cc > lo: lo = Cc
    
    hi = n // 2
    if lo > hi:
        return 0
        
    i0 = lo
    k0 = n - 2 * i0
    p0 = i0 - A
    q0 = i0 - B
    r0 = i0 - Cc
    
    coef = C.fact[i0]
    coef = (coef * C.invfact[k0]) % MOD
    coef = (coef * C.invfact[p0]) % MOD
    coef = (coef * C.invfact[q0]) % MOD
    coef = (coef * C.invfact[r0]) % MOD
    coef = (coef * C.pow2[k0]) % MOD
    
    s = coef
    inv4 = C.inv[4]
    k = k0
    
    for i in range(i0, hi):
        num = ((i + 1) * k * (k - 1)) % MOD
        den = (C.inv[i + 1 - A] * C.inv[i + 1 - B] % MOD) * C.inv[i + 1 - Cc] % MOD
        coef = (coef * num) % MOD
        coef = (coef * den) % MOD
        coef = (coef * inv4) % MOD
        s = (s + coef) % MOD
        k -= 2
        
    return s

def gCoeff(C, a, b, c):
    res = 0
    res = (res + H(C, a, b, c)) % MOD
    res = (res + H(C, a - 1, b, c)) % MOD
    res = (res + H(C, a, b, c - 1)) % MOD
    res = (res + H(C, a - 1, b - 1, c)) % MOD
    res = (res + H(C, a, b - 1, c - 1)) % MOD
    res = (res - H(C, a, b - 2, c) + MOD) % MOD
    return res

def enumerate_xor_triples(n):
    cur = [(0, 0, 0)]
    if n % 2 == 1:
        return []
        
    bit = 1
    while (1 << bit) <= n * 2 or bit <= 20:
        if (n >> bit) & 1:
            v = 1 << (bit - 1)
            nxt = []
            for t in cur:
                nxt.append((t[0], t[1] + v, t[2] + v))
                nxt.append((t[0] + v, t[1], t[2] + v))
                nxt.append((t[0] + v, t[1] + v, t[2]))
            cur = nxt
        if (1 << bit) > n and bit > 20:
            break
        bit += 1
        
    out = []
    for t in cur:
        if t[0] + t[1] + t[2] == n and (t[0] ^ t[1] ^ t[2]) == 0:
            out.append(t)
    return out

def solve_fast(C, n):
    if n < 0 or n % 2 == 1:
        return 0
        
    triples = enumerate_xor_triples(n)
    K = 0
    for t in triples:
        K = (K + gCoeff(C, t[0], t[1], t[2])) % MOD
        
    inv2 = (MOD + 1) // 2
    pow2n = pow(2, n, MOD)
    ans = (K * (pow2n - 1 + MOD)) % MOD
    ans = (ans * inv2) % MOD
    return ans

def solve():
    n = 100000
    maxN = max(n, 10)
    maxI = maxN // 2 + 5
    C = Comb(maxI)
    return str(solve_fast(C, n))

if __name__ == "__main__":
    print(solve())
