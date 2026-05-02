import math
from collections import deque

kMod = 1234567891

def sieve_spf(n):
    spf = list(range(n + 1))
    lim = math.isqrt(n)
    for i in range(2, lim + 1):
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf

def factor_list(x, spf):
    out = []
    while x > 1:
        p = spf[x]
        out.append(p)
        x //= p
    return out

def direct_sum_mod(n, m, mod):
    spf = sieve_spf(n)
    piles = []
    pos = []
    for i in range(2, n + 1):
        piles.append(factor_list(i, spf))
        pos.append(0)
        
    for _ in range(m):
        k = len(piles)
        extracted = [0] * k
        next_piles = []
        next_pos = []
        
        for i in range(k):
            extracted[i] = piles[i][pos[i]]
            pos[i] += 1
            if pos[i] < len(piles[i]):
                next_piles.append(piles[i])
                next_pos.append(pos[i])
                
        extracted.sort()
        next_piles.append(extracted)
        next_pos.append(0)
        
        piles = next_piles
        pos = next_pos
        
    total = 0
    for i in range(len(piles)):
        prod = 1
        for j in range(pos[i], len(piles[i])):
            prod = (prod * piles[i][j]) % mod
        total = (total + prod) % mod
        
    return total

def simulate_until_periodic(n, k_extra=10, streak_needed=2000, max_rounds=200000):
    spf = sieve_spf(n)
    piles = []
    pos = []
    total_factors = 0
    
    for i in range(2, n + 1):
        f = factor_list(i, spf)
        total_factors += len(f)
        piles.append(f)
        pos.append(0)
        
    k_lim = int(math.sqrt(2.0 * total_factors)) + k_extra
    bufs = [deque() for _ in range(k_lim + 1)]
    stable_streak = 0
    
    for t in range(1, max_rounds + 1):
        k = len(piles)
        extracted = [0] * k
        next_piles = []
        next_pos = []
        
        for i in range(k):
            extracted[i] = piles[i][pos[i]]
            pos[i] += 1
            if pos[i] < len(piles[i]):
                next_piles.append(piles[i])
                next_pos.append(pos[i])
                
        extracted.sort()
        next_piles.append(extracted)
        next_pos.append(0)
        
        piles = next_piles
        pos = next_pos
        
        mm = min(len(extracted), k_lim)
        
        if t <= k_lim:
            for kk in range(1, mm + 1):
                b = bufs[kk]
                b.append(extracted[kk - 1])
                if len(b) > kk:
                    b.popleft()
            for kk in range(mm + 1, k_lim + 1):
                b = bufs[kk]
                b.append(1)
                if len(b) > kk:
                    b.popleft()
            stable_streak = 0
            continue
            
        all_ok = True
        for kk in range(1, mm + 1):
            b = bufs[kk]
            v = extracted[kk - 1]
            if b[0] != v:
                all_ok = False
            b.append(v)
            if len(b) > kk:
                b.popleft()
                
        for kk in range(mm + 1, k_lim + 1):
            b = bufs[kk]
            if b[0] != 1:
                all_ok = False
            b.append(1)
            if len(b) > kk:
                b.popleft()
                
        if all_ok:
            stable_streak += 1
            if stable_streak >= streak_needed:
                patterns = [[] for _ in range(k_lim + 1)]
                kmax = 0
                for kk in range(1, k_lim + 1):
                    patterns[kk] = list(bufs[kk])
                    if any(x != 1 for x in patterns[kk]):
                        kmax = kk
                return t, patterns, kmax
        else:
            stable_streak = 0
            
    raise RuntimeError("periodicity not detected")

def sum_at_round_mod(n, m, mod):
    end_t, patterns, kmax = simulate_until_periodic(n)
    
    if m <= end_t:
        return direct_sum_mod(n, m, mod)
        
    r0 = m - end_t - 1
    total = 0
    
    for d in range(kmax):
        r = r0 - d
        if patterns[d + 1][r % (d + 1)] == 1:
            continue
            
        prod = 1
        for k in range(kmax, d, -1):
            v = patterns[k][r % k]
            if v != 1:
                prod = (prod * v) % mod
                
        total = (total + prod) % mod
        
    return total

def solve():
    ans = sum_at_round_mod(10000, 10000000000000000, kMod)
    return str(ans)

if __name__ == "__main__":
    print(solve())
