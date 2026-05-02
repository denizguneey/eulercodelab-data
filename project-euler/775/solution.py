import math

MOD = 1000000007
INV2 = (MOD + 1) // 2

def p2_prefix(r):
    if r == 0: return 0
    s = math.isqrt(r)
    if s * s < r:
        s += 1
    k = s - 1
    
    base = (8 * k**3 + 3 * k**2 + k) // 3
    consumed = k * k
    rem = r - consumed
    
    len1 = rem if rem < (s - 1) else (s - 1)
    len2 = rem - len1
    
    add1 = len1 * (4 * s - 2)
    add2 = len2 * (4 * s)
    
    return base + add1 + add2

def mod_sum_range(l, r):
    if l > r: return 0
    length = (r - l + 1) % MOD
    ends = (l + r) % MOD
    return (length * ends * INV2) % MOD

def add_phase(acc, L, R, capN, base, rBase):
    if L > capN: return acc
    left = L
    right = R if R < capN else capN
    if left > right: return acc
    
    len_u = right - left + 1
    length = len_u % MOD
    sum_n = mod_sum_range(left, right)
    
    rr = right - rBase
    ll = left - rBase
    sum_p_u = p2_prefix(rr) - p2_prefix(ll - 1 if ll > 0 else 0)
    sum_p = sum_p_u % MOD
    
    cur = (6 * sum_n) % MOD
    cur = (cur - length * (base % MOD) + MOD) % MOD
    cur = (cur - sum_p + MOD) % MOD
    
    return (acc + cur) % MOD

def G_mod(N):
    ans = 0
    mMax = int(math.floor(math.pow(N, 1.0/3.0)))
    while (mMax + 1)**3 <= N: mMax += 1
    while mMax**3 > N: mMax -= 1
    
    for m in range(1, mMax + 1):
        m2 = m * m
        mp1 = m + 1
        
        v0 = m * m2
        v1 = m2 * mp1
        v2 = m * mp1 * mp1
        v3 = mp1 * mp1 * mp1
        
        s0 = 6 * m2
        s1 = 2 * (m2 + 2 * m * mp1)
        s2 = 2 * (2 * m * mp1 + mp1 * mp1)
        
        ans = add_phase(ans, v0, v1, N, s0, v0)
        ans = add_phase(ans, v1 + 1, v2, N, s1, v1)
        ans = add_phase(ans, v2 + 1, v3 - 1, N, s2, v2)
        
    return ans

def solve():
    return str(G_mod(10**16))

if __name__ == "__main__":
    print(solve())
