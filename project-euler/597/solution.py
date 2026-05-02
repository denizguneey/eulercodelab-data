import sys
from decimal import Decimal, getcontext

def solve():
    getcontext().prec = 50
    
    n = 13
    L = 1800
    gap = 40
    m = L // gap
    
    S = [[Decimal(0)] * (m + 1) for _ in range(n + 1)]
    
    for j in range(m + 1):
        S[0][j] = Decimal(1)
        S[1][j] = Decimal(1)
        
    for i in range(2, n + 1):
        m0 = i - 1
        if m0 <= m:
            sign = Decimal(-1) if ((i - 1) & 1) else Decimal(1)
            S[i][m0] = sign * S[i - 1][m0]
            
        for ext_m in range(i, m + 1):
            D = Decimal(i * ext_m - i * (i - 1) // 2)
            total = Decimal(0)
            for k in range(1, i + 1):
                d_k = ext_m - (k - 1)
                weight = Decimal(d_k) / D
                total += weight * S[k][k - 1] * S[i - k][ext_m - k]
            S[i][ext_m] = total
            
    ans = (S[n][m] + Decimal(1)) / Decimal(2)
    return f"{ans:.10f}"

if __name__ == '__main__':
    print(solve())
