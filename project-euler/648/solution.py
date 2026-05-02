def solve():
    DEG = 1000
    MOD = 1000000000

    MAXN = 2 * DEG
    C = [[0] * (DEG + 1) for _ in range(MAXN + 1)]
    C[0][0] = 1
    for n in range(1, MAXN + 1):
        C[n][0] = 1
        up = min(n, DEG)
        for k in range(1, up + 1):
            C[n][k] = (C[n - 1][k] + C[n - 1][k - 1]) % MOD

    S = [0] * (DEG + 1)
    g = [0] * (DEG + 1)
    P = [0] * (DEG + 1)
    y = [0] * (DEG + 1)
    
    P[0] = 1
    y[0] = 1
    
    for n in range(1, DEG + 1):
        m = 2 * (n - 1)
        up = min(m, DEG)
        for k in range(up + 1):
            coef = C[m][k]
            if k % 2 == 1:
                coef = 0 if coef == 0 else MOD - coef
            S[k] = (S[k] + coef) % MOD
            
        for k in range(DEG + 1): g[k] = 0
        for k in range(1, DEG + 1): g[k] = S[k - 1]
        for k in range(2, DEG + 1):
            g[k] = (g[k] + MOD - S[k - 2]) % MOD
            
        acc = [0] * (DEG + 1)
        for i in range(DEG + 1):
            if P[i] == 0: continue
            maxj = DEG - i
            for j in range(1, maxj + 1):
                if g[j] == 0: continue
                acc[i + j] += P[i] * g[j]
                
        newP = [0] * (DEG + 1)
        for k in range(DEG + 1):
            newP[k] = acc[k] % MOD
            
        P = newP
        
        for k in range(DEG + 1):
            y[k] = (y[k] + P[k]) % MOD
            
    return str(y[DEG])

if __name__ == '__main__':
    print(solve())
