import math

def tri_u128(n):
    return n * (n + 1) // 2

def build_spf(n):
    spf = [0] * (n + 1)
    for i in range(2, n + 1):
        if spf[i] == 0:
            spf[i] = i
            if i * i <= n:
                for x in range(i * i, n + 1, i):
                    if spf[x] == 0:
                        spf[x] = i
    if n >= 1: spf[1] = 1
    return spf

def build_squarefree_mu_divisors(n, spf):
    divs = [[] for _ in range(n + 1)]
    if n >= 1: divs[1].append((1, 1))
    
    for x in range(2, n + 1):
        t = x
        primes = []
        while t > 1:
            p = spf[t]
            primes.append(p)
            while t % p == 0:
                t //= p
                
        cur = [(1, 1)]
        for p in primes:
            for i in range(len(cur)):
                cur.append((cur[i][0] * p, -cur[i][1]))
        divs[x] = cur
    return divs

def coprime_prefix_sum(x, sqf_divs_r):
    if x == 0: return 0
    out = 0
    for d, mu in sqf_divs_r:
        q = x // d
        term = d * tri_u128(q)
        if mu > 0:
            out += term
        else:
            out -= term
    return out

def coprime_range_sum(l, rr, sqf_divs_r):
    if l > rr: return 0
    hi = coprime_prefix_sum(rr, sqf_divs_r)
    lo = coprime_prefix_sum(l - 1, sqf_divs_r)
    return hi - lo

def solve():
    L = 1000000000
    if L < 2: return "0"
    
    r_max = int(math.sqrt(L))
    spf = build_spf(r_max)
    sqf_divs = build_squarefree_mu_divisors(r_max, spf)
    
    total = 0
    for r in range(1, r_max + 1):
        s_lo = r + 1
        s_hi = min(2 * r - 1, L // r)
        if s_lo > s_hi: continue
        
        while s_lo <= s_hi:
            m = L // (r * s_lo)
            s_end = min(s_hi, L // (r * m))
            
            sum_s = coprime_range_sum(s_lo, s_end, sqf_divs[r])
            add = r * tri_u128(m) * sum_s
            total += add
            
            s_lo = s_end + 1
            
    return str(total)

if __name__ == '__main__':
    print(solve())
