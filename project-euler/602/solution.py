MOD = 1000000007

def solve():
    n = 10000000
    k = 4000000
    m = k - 1
    N = n + 1
    JMAX = m + 1
    
    inv = [0] * (JMAX + 2)
    inv[1] = 1
    for i in range(2, JMAX + 2):
        inv[i] = MOD - (MOD // i) * inv[MOD % i] % MOD
        
    ans = 0
    binom = 1
    for j in range(JMAX + 1):
        base = JMAX - j
        pown = pow(base, n, MOD)
        term = (binom * pown) % MOD
        
        if j & 1:
            ans = (ans - term + MOD) % MOD
        else:
            ans = (ans + term) % MOD
            
        if j == JMAX: break
        binom = (binom * (N - j)) % MOD
        binom = (binom * inv[j + 1]) % MOD
        
    return str(ans)

if __name__ == '__main__':
    print(solve())
