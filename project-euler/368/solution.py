from decimal import Decimal, getcontext

getcontext().prec = 100

kStateCount = 20

def state_index(digit, run_len):
    return digit * 2 + (run_len - 1)

def has_three_equal_consecutive(n):
    s = str(n)
    for i in range(len(s) - 2):
        if s[i] == s[i+1] == s[i+2]: return True
    return False

def build_automaton():
    trans = [[] for _ in range(kStateCount)]
    for d in range(10):
        for r in (1, 2):
            s = state_index(d, r)
            for x in range(10):
                if x == d:
                    if r == 2: continue
                    trans[s].append((x, state_index(d, 2)))
                else:
                    trans[s].append((x, state_index(x, 1)))
    return trans

def solve_moments(trans, max_m):
    h = [[Decimal(0)] * (max_m + 1) for _ in range(kStateCount)]
    
    binom = [[0] * (max_m + 1) for _ in range(max_m + 1)]
    for n in range(max_m + 1):
        binom[n][0] = 1
        binom[n][n] = 1
        for k in range(1, n):
            binom[n][k] = binom[n-1][k-1] + binom[n-1][k]
            
    digit_pow = [[Decimal(1)] * 32 for _ in range(10)]
    for d in range(10):
        for p in range(1, 32):
            digit_pow[d][p] = digit_pow[d][p - 1] * Decimal(d)
            
    c10 = Decimal(10)
            
    for m in range(max_m + 1):
        c = Decimal(1) / (c10 ** (m + 1))
        
        a = [[Decimal(0)] * (kStateCount + 1) for _ in range(kStateCount)]
        
        for s in range(kStateCount):
            a[s][s] = Decimal(1)
            for digit, to in trans[s]:
                a[s][to] -= c
                
            rhs = Decimal(1) if m == 0 else Decimal(0)
            for digit, to in trans[s]:
                for u in range(m):
                    term = c * Decimal(binom[m][u]) * digit_pow[digit][m - u] * h[to][u]
                    rhs += term
            a[s][kStateCount] = rhs
            
        for col in range(kStateCount):
            pivot = col
            for r in range(col + 1, kStateCount):
                if abs(a[r][col]) > abs(a[pivot][col]):
                    pivot = r
            a[col], a[pivot] = a[pivot], a[col]
            
            pv = a[col][col]
            for j in range(col, kStateCount + 1):
                a[col][j] /= pv
                
            for r in range(kStateCount):
                if r == col: continue
                factor = a[r][col]
                if abs(factor) < Decimal("1e-80"): continue
                for j in range(col, kStateCount + 1):
                    a[r][j] -= factor * a[col][j]
                    
        for s in range(kStateCount):
            h[s][m] = a[s][kStateCount]
            
    return h

def estimate_series_value(h, max_m, prefix_digits):
    low = 1
    high_small = 10 ** (prefix_digits - 1)
    high_prefix = high_small * 10
    
    total = Decimal(0)
    for n in range(low, high_small):
        if not has_three_equal_consecutive(n):
            total += Decimal(1) / Decimal(n)
            
    for p in range(high_small, high_prefix):
        if has_three_equal_consecutive(p): continue
        
        last = p % 10
        prev = (p // 10) % 10
        run = 2 if last == prev else 1
        s = state_index(last, run)
        
        inv_p = Decimal(1) / Decimal(p)
        inv_power = inv_p
        contrib = Decimal(0)
        sign = 1
        for m in range(max_m + 1):
            term = h[s][m] * inv_power
            if sign > 0: contrib += term
            else: contrib -= term
            inv_power *= inv_p
            sign = -sign
            
        total += contrib
        
    return total

def solve():
    trans = build_automaton()
    max_m = 16
    h = solve_moments(trans, max_m)
    val = estimate_series_value(h, max_m, 3)
    return "{:.10f}".format(val)

if __name__ == '__main__':
    print(solve())
