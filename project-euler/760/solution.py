import sys

sys.setrecursionlimit(2000)

MOD = 1000000007
INV2 = (MOD + 1) // 2

memo = {}

def add_mod(a, b):
    r = a + b
    if r >= MOD:
        r -= MOD
    return r

def mul_mod(a, b):
    return (a * b) % MOD

def solve_rec(n):
    if n <= 0:
        return (0, 0)
    if n in memo:
        return memo[n]
        
    m = n // 2
    sm_h, sm_s = solve_rec(m)
    sm1_h, sm1_s = solve_rec(m - 1)
    mm = m % MOD
    
    if (n & 1) == 0:
        h = (mul_mod(2, sm_h) + mul_mod(2, sm1_h) + mm) % MOD
        
        poly = mul_mod(3, mul_mod(mm, (mm + 1) % MOD))
        poly = mul_mod(poly, INV2)
        s = (mul_mod(2, sm_s) + mul_mod(6, sm1_s) + poly) % MOD
    else:
        h = (mul_mod(4, sm_h) + mul_mod(2, (mm + 1) % MOD)) % MOD
        
        poly = 0
        poly = (poly + mul_mod(3, mul_mod(mm, mm))) % MOD
        poly = (poly + mul_mod(7, mm)) % MOD
        poly = (poly + 4) % MOD
        poly = mul_mod(poly, INV2)
        s = (mul_mod(6, sm_s) + mul_mod(2, sm1_s) + poly) % MOD
        
    out = (h, s)
    memo[n] = out
    return out

def solve():
    n = 1000000000000000000
    h, s = solve_rec(n)
    ans = mul_mod(2, s)
    return str(ans)

if __name__ == "__main__":
    print(solve())
