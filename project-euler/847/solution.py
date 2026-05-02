kMod = 1000000007

def mod_add(a, b):
    return (a + b) % kMod

def mod_sub(a, b):
    return (a - b + kMod) % kMod

def mod_mul(a, b):
    return (a * b) % kMod

def mod_pow(a, e):
    return pow(a, e, kMod)

INV2 = mod_pow(2, kMod - 2)
INV6 = mod_pow(6, kMod - 2)

def sum1_mod(n):
    if n < 0: return 0
    nm = n % kMod
    return mod_mul(mod_mul(nm, (nm + 1) % kMod), INV2)

def sum2_mod(n):
    if n < 0: return 0
    nm = n % kMod
    n1 = (nm + 1) % kMod
    two_n1 = (mod_mul(2, nm) + 1) % kMod
    return mod_mul(mod_mul(mod_mul(nm, n1), two_n1), INV6)

def sum1_range_mod(l, r):
    if l > r: return 0
    return mod_sub(sum1_mod(r), sum1_mod(l - 1))

def sum2_range_mod(l, r):
    if l > r: return 0
    return mod_sub(sum2_mod(r), sum2_mod(l - 1))

def sum_pair_mod(l, r, N):
    if l > r: return 0
    cnt = r - l + 1
    S1 = sum1_range_mod(l, r)
    S2 = sum2_range_mod(l, r)
    sum_s_plus = mod_add(S1, cnt % kMod)
    sum_s2_plus = mod_add(S2, S1)
    return mod_sub(mod_mul((N + 1) % kMod, sum_s_plus), sum_s2_plus)

def sum_tri_mod(l, r):
    if l > r: return 0
    cnt = r - l + 1
    S1 = sum1_range_mod(l, r)
    S2 = sum2_range_mod(l, r)
    total = mod_add(S2, mod_add(mod_mul(3, S1), mod_mul(2, cnt % kMod)))
    return mod_mul(total, INV2)

def sum_M1_sq_mod(l, r, D):
    if l > r: return 0
    u_low = D - r + 1
    u_high = D - l + 1
    return sum2_range_mod(u_low, u_high)

def sum_t_t1_mod(t0, step, n):
    if n <= 0: return 0
    n_mod = n % kMod
    n1_mod = (n - 1) % kMod
    sum_i = mod_mul(mod_mul(n_mod, n1_mod), INV2)
    two_n1 = (mod_mul(2, n1_mod) + 1) % kMod
    sum_i2 = mod_mul(mod_mul(mod_mul(n_mod, n1_mod), two_n1), INV6)
    
    t0_mod = t0 % kMod
    step_mod = step % kMod
    
    sum_t = mod_add(mod_mul(n_mod, t0_mod), mod_mul(step_mod, sum_i))
    t0_sq = mod_mul(t0_mod, t0_mod)
    term1 = mod_mul(n_mod, t0_sq)
    term2 = mod_mul(mod_mul(mod_mul(2, t0_mod), step_mod), sum_i)
    term3 = mod_mul(mod_mul(step_mod, step_mod), sum_i2)
    sum_t2 = mod_add(term1, mod_add(term2, term3))
    
    return mod_mul(mod_add(sum_t2, sum_t), INV2)

def T_mod(x):
    if x < 0: return 0
    xm = x % kMod
    return mod_mul(mod_mul(mod_mul((xm + 1) % kMod, (xm + 2) % kMod), (xm + 3) % kMod), INV6)

def count_within_cube_mod(N, D):
    if N < 0: return 0
    if N > 2 * D: N = 2 * D
    
    if N <= D:
        U = T_mod(N)
    else:
        U = mod_sub(T_mod(N), mod_mul(3, T_mod(N - D - 1)))
        
    if N <= D:
        A = sum_pair_mod(0, N, N)
    else:
        s1 = N - D
        part1 = mod_mul((D + 1) % kMod, mod_mul(mod_mul((s1 + 1) % kMod, (s1 + 2) % kMod), INV2))
        part2 = sum_pair_mod(s1 + 1, D, N)
        A = mod_add(part1, part2)
        
    if N <= D:
        AB = sum_tri_mod(0, N)
    else:
        a0 = 2 * D - N
        mid1 = sum_M1_sq_mod(0, a0 - 1, D)
        mid2 = sum_t_t1_mod(a0, -1, a0)
        mid = mod_sub(mid1, mid2)
        full = sum_M1_sq_mod(a0, D, D)
        AB = mod_add(mid, full)
        
    if N <= D:
        ABC = sum_tri_mod(0, N)
    else:
        A1 = N - D
        a_half = D // 2
        total = 0
        
        r1_end = min(A1, a_half - 1)
        if r1_end >= 0:
            mid1 = sum_M1_sq_mod(0, r1_end, D)
            n = r1_end + 1
            mid2 = sum_t_t1_mod(D, -2, n)
            total = mod_add(total, mod_sub(mid1, mid2))
            
        r1_full_start = max(0, a_half)
        if r1_full_start <= A1:
            total = mod_add(total, sum_M1_sq_mod(r1_full_start, A1, D))
            
        l2 = A1 + 1
        if l2 <= D:
            a0 = 2 * D - N
            r2_end = min(a0 - 1, D)
            if l2 <= r2_end:
                mid1 = sum_M1_sq_mod(l2, r2_end, D)
                n = r2_end - l2 + 1
                mid2 = sum_t_t1_mod(a0 - l2, -1, n)
                total = mod_add(total, mod_sub(mid1, mid2))
                
            l_full = max(l2, a0)
            if l_full <= D:
                total = mod_add(total, sum_M1_sq_mod(l_full, D, D))
                
        ABC = total
        
    return mod_sub(mod_add(mod_sub(U, mod_mul(3, A)), mod_mul(3, AB)), ABC)

memo = {}

def hard_count_mod(k, N):
    if N < 0: return 0
    if k == 1:
        if N <= 2: return 0
        return mod_sub(T_mod(N), T_mod(2))
    if N > (1 << k): N = 1 << k
    
    key = (k, N)
    if key in memo: return memo[key]
    
    D = 1 << (k - 1)
    if N <= D:
        res = count_within_cube_mod(N, D)
    else:
        res = mod_add(count_within_cube_mod(N, D), mod_mul(3, hard_count_mod(k - 1, N - D)))
        
    memo[key] = res
    return res

def sum_C_range(L, R):
    if L > R: return 0
    cnt = R - L + 1
    S1 = sum1_range_mod(L, R)
    S2 = sum2_range_mod(L, R)
    total = mod_add(S2, mod_add(mod_mul(3, S1), mod_mul(2, cnt % kMod)))
    return mod_mul(total, INV2)

def compute_H(N):
    if N <= 1: return 0
    max_k = (N - 1).bit_length()
    
    base = 0
    for k in range(1, max_k + 1):
        L = (1 << (k - 1)) + 1
        R = min(N, 1 << k)
        if L > R: continue
        sumC = sum_C_range(L, R)
        base = mod_add(base, mod_mul(k % kMod, sumC))
        
    global memo
    memo.clear()
    
    extra = 0
    for k in range(1, max_k + 1):
        X = min(N, 1 << k)
        extra = mod_add(extra, hard_count_mod(k, X))
        
    return mod_add(base, extra)

def solve():
    N = int("1" * 19)
    ans = compute_H(N)
    return str(ans)

if __name__ == "__main__":
    print(solve())
