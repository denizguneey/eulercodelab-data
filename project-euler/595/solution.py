import math
from decimal import Decimal, getcontext

def solve():
    getcontext().prec = 100
    N = 52
    
    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = fact[i - 1] * i
        
    def comb(n, k):
        if k < 0 or k > n: return 0
        return fact[n] // (fact[k] * fact[n - k])
        
    f = [0] * (N + 1)
    f[0] = 1
    for b in range(1, N + 1):
        fb = 0
        for r in range(b):
            term = comb(b - 1, r) * fact[b - r]
            if r % 2 == 1:
                fb -= term
            else:
                fb += term
        f[b] = fb
        
    P = [[Decimal(0)] * (N + 1) for _ in range(N + 1)]
    for m in range(1, N + 1):
        denom = Decimal(fact[m])
        for b in range(1, m + 1):
            cnt = comb(m - 1, b - 1) * f[b]
            P[m][b] = Decimal(cnt) / denom
            
    E = [Decimal(0)] * (N + 1)
    for m in range(2, N + 1):
        num = Decimal(1)
        for b in range(1, m):
            num += P[m][b] * E[b]
        E[m] = num / (Decimal(1) - P[m][m])
        
    def S(n):
        s = Decimal(0)
        for b in range(1, n + 1):
            s += P[n][b] * E[b]
        return s
        
    ans = S(N)
    return f"{ans:.8f}"

if __name__ == '__main__':
    print(solve())
