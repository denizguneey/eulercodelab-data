import sys
import math
from bisect import bisect_right

def has_balanced_triple_even2(s):
    n = s // 2
    if n < 7: return False
    LIM = 2000
    for d1 in range(2, min(LIM + 1, n), 2):
        if math.gcd(d1, n) != 1: continue
        for d2 in range(d1 + 2, min(LIM + 1, n - d1), 2):
            if math.gcd(d2, n) != 1: continue
            if math.gcd(d1 + d2, n) != 1: continue
            return True
    return False

def F(N, pref_phi, pref_cost):
    target = 2 * N
    
    it = bisect_right(pref_cost, target)
    m = 0 if it == 0 else it - 1
    
    base_cnt = pref_phi[m] if m >= 2 else 0
    base_cost = pref_cost[m] if m >= 2 else 0
    
    slack = target - base_cost
    s = m + 1
    t = slack // s if s > 0 else 0
    r = slack % s if s > 0 else 0
    
    segments = base_cnt + t
    
    if r == 0 and (t & 1) and t > 0:
        ok = False
        if t == 1:
            ok = False
        elif s % 4 == 0:
            ok = False
        elif s % 4 == 2:
            ok = has_balanced_triple_even2(s)
            
        if not ok:
            segments -= 1
            
    return segments + 1

def solve_N(N_max):
    target_max = 2 * N_max
    limit = 3000000
    while True:
        phi = list(range(limit + 1))
        for p in range(2, limit + 1):
            if phi[p] == p:
                for j in range(p, limit + 1, p):
                    phi[j] -= phi[j] // p
                    
        pref_phi = [0] * (limit + 1)
        pref_cost = [0] * (limit + 1)
        
        for i in range(2, limit + 1):
            pref_phi[i] = pref_phi[i - 1] + phi[i]
            pref_cost[i] = pref_cost[i - 1] + i * phi[i]
            
        if pref_cost[limit] >= target_max:
            break
        limit = int(limit * 1.4) + 1000
        
    return str(F(N_max, pref_phi, pref_cost))

def solve():
    return solve_N(1000000000000000000)

if __name__ == '__main__':
    print(solve())
