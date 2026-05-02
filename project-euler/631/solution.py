def solve():
    MOD = 1000000007
    m = 40
    n = 10**18
    dim_inv = m + 1
    dim_last132 = m + 3
    dim_last21 = m + 3
    plane = dim_last132 * dim_last21
    total_states = dim_inv * plane
    
    cur = [0] * total_states
    cur[m * plane + 0] = 1 # last132p1 = 0, last21 = 0
    
    total = 1
    max_len = m + 2
    limit = min(n, max_len)
    
    for length in range(1, limit + 1):
        nxt = [0] * total_states
        for inv in range(m + 1):
            upper = min(inv + 1, length)
            if upper <= 0: continue
            for last132p1 in range(length + 1):
                start = last132p1
                if start >= upper: continue
                for last21 in range(length):
                    cnt = cur[inv * plane + last132p1 * dim_last21 + last21]
                    if cnt == 0: continue
                    for i in range(start, upper):
                        total += cnt
                        if i < last21:
                            idx_val = (inv - i) * plane + (i + 1) * dim_last21 + (last21 + 1)
                            nxt[idx_val] += cnt
                        else:
                            idx_val = (inv - i) * plane + last132p1 * dim_last21 + i
                            nxt[idx_val] += cnt
        cur = [x % MOD for x in nxt]
        total %= MOD

    if n <= max_len:
        return str(total)
        
    g = sum(cur) % MOD
        
    extra = ((n - max_len) % MOD) * g % MOD
    return str((total + extra) % MOD)

if __name__ == '__main__':
    print(solve())
