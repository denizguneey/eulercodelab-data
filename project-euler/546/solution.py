MOD = 1000000007

def mod_pow(base, exp):
    return pow(base, exp, MOD)

def to_digits(n, base):
    if n == 0: return [0]
    digits = []
    while n > 0:
        digits.append(n % base)
        n //= base
    return digits

class Precomputed:
    def __init__(self, max_deg):
        self.max_deg = max_deg
        size = max_deg + 2
        
        binom = [[0] * size for _ in range(size)]
        for n in range(size):
            binom[n][0] = 1
            binom[n][n] = 1
            for k in range(1, n):
                binom[n][k] = (binom[n - 1][k - 1] + binom[n - 1][k]) % MOD
        self.binom = binom
        
        stirling = [[0] * size for _ in range(size)]
        stirling[0][0] = 1
        for n in range(1, size):
            for k in range(1, n + 1):
                stirling[n][k] = (stirling[n - 1][k - 1] + k * stirling[n - 1][k]) % MOD
                
        fact = [1] * (size + 1)
        for i in range(1, size + 1):
            fact[i] = (fact[i - 1] * i) % MOD
            
        poly_binom = [[] for _ in range(size)]
        poly_binom[0] = [1]
        for m in range(1, size):
            prev = poly_binom[m - 1]
            cur = [0] * (len(prev) + 1)
            for p in range(len(prev)):
                a = prev[p]
                dec = (a * (m - 1)) % MOD
                cur[p] = (cur[p] - dec) % MOD
                cur[p + 1] = (cur[p + 1] + a) % MOD
                
            inv_m = mod_pow(m, MOD - 2)
            for i in range(len(cur)):
                cur[i] = (cur[i] * inv_m) % MOD
            poly_binom[m] = cur
            
        poly_binom_shift = [[] for _ in range(size)]
        for m in range(size):
            poly = poly_binom[m]
            shift = [0] * len(poly)
            for p in range(len(poly)):
                a = poly[p]
                if a == 0: continue
                for q in range(p + 1):
                    shift[q] = (shift[q] + a * binom[p][q]) % MOD
            poly_binom_shift[m] = shift
            
        sum_pow = [[] for _ in range(max_deg + 1)]
        for p in range(max_deg + 1):
            poly = [0] * (p + 2)
            for j in range(p + 1):
                if stirling[p][j] == 0: continue
                coeff = (stirling[p][j] * fact[j]) % MOD
                base = poly_binom_shift[j + 1]
                for idx in range(len(base)):
                    poly[idx] = (poly[idx] + coeff * base[idx]) % MOD
            sum_pow[p] = poly
            
        self.sum_pow = sum_pow

def prefix_sum_poly(poly, pre):
    res = [0] * (len(poly) + 1)
    for p in range(len(poly)):
        a = poly[p]
        if a == 0: continue
        base = pre.sum_pow[p]
        for i in range(len(base)):
            res[i] = (res[i] + a * base[i]) % MOD
    return res

def substitute_poly(poly, k, s, pre, pow_k):
    d = len(poly) - 1
    pow_s = [1] * (d + 1)
    pow_s[0] = 1
    for i in range(1, d + 1):
        pow_s[i] = (pow_s[i - 1] * s) % MOD
        
    res = [0] * (d + 1)
    for p in range(d + 1):
        a = poly[p]
        if a == 0: continue
        for q in range(p + 1):
            term = (a * pre.binom[p][q]) % MOD
            term = (term * pow_k[q]) % MOD
            term = (term * pow_s[p - q]) % MOD
            res[q] = (res[q] + term) % MOD
    return res

def compute_f(n, k, pre):
    if n == 0: return 1
    digits = to_digits(n, k)
    L = len(digits) - 1
    
    pow_k = [1] * (pre.max_deg + 2)
    for i in range(1, len(pow_k)):
        pow_k[i] = (pow_k[i - 1] * k) % MOD
        
    free_poly = [k % MOD]
    tight_poly = [(digits[0] + 1) % MOD]
    if L == 0: return tight_poly[0]
    
    for j in range(1, L + 1):
        sum_free = prefix_sum_poly(free_poly, pre)
        sum_tight = prefix_sum_poly(tight_poly, pre)
        
        new_free = [0] * len(sum_free)
        for s in range(k):
            sub = substitute_poly(sum_free, k, s, pre, pow_k)
            for i in range(len(sub)):
                new_free[i] = (new_free[i] + sub[i]) % MOD
                
        new_tight = [0] * len(sum_free)
        dj = digits[j]
        for s in range(dj):
            sub = substitute_poly(sum_free, k, s, pre, pow_k)
            for i in range(len(sub)):
                new_tight[i] = (new_tight[i] + sub[i]) % MOD
                
        sub_tight = substitute_poly(sum_tight, k, dj, pre, pow_k)
        for i in range(len(sub_tight)):
            new_tight[i] = (new_tight[i] + sub_tight[i]) % MOD
            
        free_poly = new_free
        tight_poly = new_tight
        
    return tight_poly[0] % MOD

def solve():
    n = 100000000000000
    max_n = max(n, 1000)
    max_deg = len(to_digits(max_n, 2)) + 2
    pre = Precomputed(max_deg)
    
    total = 0
    for k in range(2, 11):
        total = (total + compute_f(n, k, pre)) % MOD
            
    return str(total)

if __name__ == '__main__':
    print(solve())
