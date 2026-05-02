def bit_length(v):
    bits = 0
    while v > 0:
        bits += 1
        v >>= 1
    return 1 if bits == 0 else bits

kMod = 1000036000099
kP1 = 1000003
kP2 = 1000033

class SmallComb:
    def __init__(self, max_n):
        self.c = [[0] * (max_n + 1) for _ in range(max_n + 1)]
        for n in range(max_n + 1):
            self.c[n][0] = self.c[n][n] = 1
            for k in range(1, n):
                self.c[n][k] = self.c[n - 1][k - 1] + self.c[n - 1][k]

def build_small_comb(max_n):
    return SmallComb(max_n)

def mod_pow(base, exp, mod):
    return pow(base, exp, mod)

def mod_inv_prime(a, p):
    return pow(a, p - 2, p)

class FactTable:
    def __init__(self, n, p):
        self.fact = [0] * (n + 1)
        self.invfact = [0] * (n + 1)
        self.fact[0] = 1
        for i in range(1, n + 1):
            self.fact[i] = (self.fact[i - 1] * i) % p
        self.invfact[n] = mod_inv_prime(self.fact[n], p)
        for i in range(n, 0, -1):
            self.invfact[i - 1] = (self.invfact[i] * i) % p

def build_fact_table(n, p):
    return FactTable(n, p)

def binom_mod_prime(n, k, ft, p):
    if k < 0 or k > n: return 0
    res = (ft.fact[n] * ft.invfact[k]) % p
    res = (res * ft.invfact[n - k]) % p
    return res

def crt(a, b):
    t = (b + kP2 - (a % kP2)) % kP2
    inv = mod_inv_prime(kP1 % kP2, kP2)
    k = (t * inv) % kP2
    return a + kP1 * k

def binom_mod_composite(n, k, f1, f2):
    a = binom_mod_prime(n, k, f1, kP1)
    b = binom_mod_prime(n, k, f2, kP2)
    return crt(a, b)

class WaysEvenMod:
    def __init__(self, k, r, comb):
        self.max_s = k + r
        self.ways = [0] * (self.max_s + 1)
        for x in range(0, k + 1, 2):
            cx = comb.c[k][x]
            for y in range(0, r + 1):
                s = x + y
                add = (cx * comb.c[r][y]) % kMod
                self.ways[s] = (self.ways[s] + add) % kMod

def build_ways_even_mod(k, r, comb):
    return WaysEvenMod(k, r, comb)

def count_with_ways_mod(S, ways):
    max_s = ways.max_s
    dp = [0] * (max_s + 1)
    dp[0] = 1
    
    bits = bit_length(S) + 7
    for b in range(bits):
        bit = (S >> b) & 1
        nxt = [0] * (max_s + 1)
        for carry in range(max_s + 1):
            base = dp[carry]
            if base == 0: continue
            for s in range(max_s + 1):
                ways_s = ways.ways[s]
                if ways_s == 0: continue
                total = s + carry
                if (total & 1) != bit: continue
                carry_out = total >> 1
                add = (base * ways_s) % kMod
                nxt[carry_out] = (nxt[carry_out] + add) % kMod
        dp = nxt
    return dp[0]

def compute_W_mod(n, c, comb, f1, f2):
    m = c + 1
    N = n - m
    total = (m * binom_mod_composite(n, m, f1, f2)) % kMod
    if m == 1:
        return total
        
    k = (m + 1) // 2
    r = m - k + 1
    if m % 2 == 0:
        ways = build_ways_even_mod(k, r, comb)
        losing = ((m - 1) * count_with_ways_mod(N, ways)) % kMod
        return (total + kMod - losing) % kMod
        
    ways_k = build_ways_even_mod(k, r, comb)
    ways_km1 = build_ways_even_mod(k - 1, r, comb)
    
    L0 = count_with_ways_mod(N, ways_k)
    L1 = count_with_ways_mod(N + 1, ways_k)
    L1_sub = count_with_ways_mod(N + 1, ways_km1)
    L1 = (L1 + kMod - L1_sub) % kMod
    
    losing = (L0 + ((m - 2) * L1) % kMod) % kMod
    return (total + kMod - losing) % kMod

def solve():
    max_small = 52
    comb = build_small_comb(max_small)
    n = 1000000
    c = 100
    f1 = build_fact_table(n, kP1)
    f2 = build_fact_table(n, kP2)
    ans = compute_W_mod(n, c, comb, f1, f2)
    return str(ans)

if __name__ == '__main__':
    print(solve())
