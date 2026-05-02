def solve():
    kMod = 100000007
    kFibLimit = 90
    block_size = 100000
    
    max_n = kMod - 1
    num_blocks = (max_n + block_size - 1) // block_size
    block_fact = [1] * (num_blocks + 1)
    
    cur = 1
    for b in range(1, num_blocks + 1):
        start = (b - 1) * block_size + 1
        end = min(b * block_size, max_n)
        for x in range(start, end + 1):
            cur = (cur * x) % kMod
        block_fact[b] = cur
        
    def factorial_mod(n):
        if n < 0 or n >= kMod: return 0
        if n == 0: return 1
        b = n // block_size
        cur_val = block_fact[b]
        start = b * block_size + 1
        for x in range(start, n + 1):
            cur_val = (cur_val * x) % kMod
        return cur_val
        
    def binom_small(n, k):
        if k < 0 or k > n: return 0
        if k == 0 or k == n: return 1
        nf = factorial_mod(n)
        kf = factorial_mod(k)
        nkf = factorial_mod(n - k)
        den = (kf * nkf) % kMod
        inv_den = pow(den, kMod - 2, kMod)
        return (nf * inv_den) % kMod
        
    def binom_lucas(n, k):
        if k > n: return 0
        nn = n
        kk = k
        res = 1
        while nn > 0 or kk > 0:
            ni = nn % kMod
            ki = kk % kMod
            if ki > ni: return 0
            res = (res * binom_small(ni, ki)) % kMod
            nn //= kMod
            kk //= kMod
        return res
        
    def central_binom(n):
        return binom_lucas(2 * n, n)
        
    def c_mod(n):
        central = central_binom(n)
        n_mod = n % kMod
        n2_mod = (n_mod * n_mod) % kMod
        correction = (3 * n2_mod + 2 * n_mod + 7) % kMod
        ans = (8 * central) % kMod
        ans = (ans - correction + kMod) % kMod
        return ans
        
    f = [0] * (kFibLimit + 1)
    f[1] = 1
    f[2] = 1
    for i in range(3, kFibLimit + 1):
        f[i] = f[i-1] + f[i-2]
        
    ans = 0
    for i in range(2, kFibLimit + 1):
        ans = (ans + c_mod(f[i])) % kMod
        
    return str(ans)

if __name__ == '__main__':
    print(solve())
