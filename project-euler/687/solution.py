def solve():
    memo = {}
    
    def dfs(f, c1, c2, c3, c4, prev):
        rem = f + c1 + 2 * c2 + 3 * c3 + 4 * c4
        if rem == 0:
            return 1.0
            
        key = (f, c1, c2, c3, c4, prev)
        if key in memo:
            return memo[key]
            
        out = 0.0
        
        if f > 0:
            out += (f / rem) * dfs(f - 1, c1, c2, c3, c4, -1)
            
        def add_rank(r, count, nc1, nc2, nc3, nc4):
            nonlocal out
            if count == 0:
                return
            avail = count
            if prev == r:
                avail -= 1
            if avail <= 0:
                return
                
            np_val = -1 if r == 1 else r - 1
            prob = (avail * r) / rem
            out += prob * dfs(f, nc1, nc2, nc3, nc4, np_val)
            
        add_rank(1, c1, c1 - 1, c2, c3, c4)
        add_rank(2, c2, c1 + 1, c2 - 1, c3, c4)
        add_rank(3, c3, c1, c2 + 1, c3 - 1, c4)
        add_rank(4, c4, c1, c2, c3 + 1, c4 - 1)
        
        memo[key] = out
        return out

    def prob_all_perfect(j):
        memo.clear()
        return dfs(52 - 4 * j, 0, 0, 0, j, -1)
        
    C = [[0] * 14 for _ in range(14)]
    for n in range(14):
        C[n][0] = 1
        C[n][n] = 1
        for k in range(1, n):
            C[n][k] = C[n - 1][k - 1] + C[n - 1][k]
            
    p = [0.0] * 14
    p[0] = 1.0
    for j in range(1, 14):
        p[j] = prob_all_perfect(j)
        
    M = [0.0] * 14
    for j in range(14):
        M[j] = C[13][j] * p[j]
        
    P = [0.0] * 14
    for k in range(13, -1, -1):
        v = M[k]
        for t in range(k + 1, 14):
            v -= C[t][k] * P[t]
        P[k] = v
        
    primes = [2, 3, 5, 7, 11, 13]
    ans = 0.0
    for pval in primes:
        ans += P[pval]
        
    return f"{ans:.10f}"

if __name__ == '__main__':
    print(solve())
