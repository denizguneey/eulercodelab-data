import sys
import multiprocessing

MOD = 1_000_000_007

def modpow(a, e):
    return pow(a, e, MOD)

def pow_base(b, e):
    if e == 0 or b == 1:
        return 1
    return pow_all[pow_offset[b] + e]

pow_all = []
pow_offset = []

def build_powers(n):
    global pow_all, pow_offset
    max_base = n + 1
    pow_offset = [0] * (max_base + 1)
    pow_len = [0] * (max_base + 1)
    
    total_len = 0
    for b in range(2, max_base + 1):
        max_exp = (n - 1) // (b - 1) + 1
        pow_len[b] = max_exp + 1
        pow_offset[b] = total_len
        total_len += pow_len[b]
        
    pow_all = [0] * total_len
    for b in range(2, max_base + 1):
        off = pow_offset[b]
        length = pow_len[b]
        pow_all[off] = 1
        for e in range(1, length):
            pow_all[off + e] = (pow_all[off + e - 1] * b) % MOD

def compute_B_range(n, l_start, l_end):
    sum_val = 0
    n1 = n - 1
    for l in range(l_start, l_end):
        max_q = n1 // l
        for q in range(1, max_q + 1):
            N0 = q * l
            N1 = min((q + 1) * l - 1, n1)
            R = N1 - N0
            
            powqL = pow_base(q, l)
            term0 = ((q - 1) * powqL) % MOD
            sum_block = term0
            
            if R >= 1:
                powqL1 = pow_base(q, l + 1)
                powqL1minusR = pow_base(q, l + 1 - R)
                powq1R1 = pow_base(q + 1, R + 1)
                sum_r = (powqL1minusR * powq1R1 - powqL1 * (q + 1)) % MOD
                if sum_r < 0:
                    sum_r += MOD
                sum_block = (sum_block + sum_r) % MOD
                
            sum_val = (sum_val + sum_block) % MOD
            
    return sum_val

def compute_B_chunk(args):
    n, l_start, l_end = args
    return compute_B_range(n, l_start, l_end)

def solve_fast(n):
    if n <= 0: return 0
    
    sumA = 0
    for l in range(1, n + 1):
        q = n // l
        r = n % l
        P = (pow_base(q, l - r) * pow_base(q + 1, r)) % MOD
        sumA = (sumA + P) % MOD
        
    if n == 1: return sumA
    
    n1 = n - 1
    
    sumB = compute_B_range(n, 1, n)
    return (sumA + sumB) % MOD

def brute_count(n):
    a = [0] * (n + 1)
    cnt = 0
    
    def dfs(idx):
        nonlocal cnt
        if idx > n:
            for k in range(1, n):
                if a[k + 1] != a[a[k]]:
                    return
            cnt += 1
            return
            
        for v in range(1, n + 1):
            a[idx] = v
            dfs(idx + 1)
            
    dfs(1)
    return cnt

def solve_slow(n):
    total = 0
    for t in range(n):
        N_val = n - t
        for l in range(1, N_val + 1):
            q = N_val // l
            r = N_val % l
            P = (modpow(q, l - r) * modpow(q + 1, r)) % MOD
            if t == 0:
                total += P
            else:
                multiplier = q - 1 if r == 0 else q
                total += (multiplier * P) % MOD
            total %= MOD
    return total

def solve():
    N = 1000000
    build_powers(N)
    return str(solve_fast(N))

def run_checkpoints():
    assert brute_count(7) == 174
    assert solve_slow(100) == 305741269
    build_powers(7)
    assert solve_fast(7) == 174

if __name__ == "__main__":
    run_checkpoints()
    print(solve())
