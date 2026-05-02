MOD = 1000267129
DIGS = 10
FULL = (1 << DIGS) - 1

def count_by_mask(max_len):
    cnt = [0] * (FULL + 1)
    dp = [0] * (FULL + 1)
    ndp = [0] * (FULL + 1)
    
    for d in range(1, 10):
        dp[1 << d] += 1
        
    for length in range(1, max_len + 1):
        for m in range(FULL + 1):
            cnt[m] = (cnt[m] + dp[m]) % MOD
            
        if length == max_len:
            break
            
        ndp = [0] * (FULL + 1)
        for m in range(FULL + 1):
            v = dp[m]
            if not v: continue
            for d in range(10):
                nm = m | (1 << d)
                ndp[nm] = (ndp[nm] + v) % MOD
                
        dp = ndp
        
    return cnt

def solve_f(K):
    inv2 = (MOD + 1) // 2
    cnt = count_by_mask(K)
    
    sum_sub = list(cnt)
    for b in range(DIGS):
        bit = 1 << b
        for mask in range(FULL + 1):
            if mask & bit:
                sum_sub[mask] = (sum_sub[mask] + sum_sub[mask ^ bit]) % MOD
                
    ordered_disjoint = 0
    for a in range(FULL + 1):
        ordered_disjoint = (ordered_disjoint + cnt[a] * sum_sub[FULL ^ a]) % MOD
        
    disjoint_pairs = (ordered_disjoint * inv2) % MOD
    
    M = (pow(10, K, MOD) - 1) % MOD
    total_pairs = (M * (M - 1) % MOD) * inv2 % MOD
    
    return (total_pairs - disjoint_pairs + MOD) % MOD

def solve():
    return str(solve_f(18))

if __name__ == '__main__':
    print(solve())
