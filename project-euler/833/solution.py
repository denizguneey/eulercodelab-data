import math

kMod = 136101521

def max_k_for_pair(n_val, i_idx, j_idx):
    def eval_pair_leq(k):
        x = 2 * k + 1
        max_idx = max(i_idx, j_idx)
        U = [0] * (max_idx + 1)
        U[0] = 1
        if max_idx >= 1: U[1] = 2 * x
        
        two_x = 2 * x
        for m in range(1, max_idx):
            if U[m] > (n_val + U[m - 1]) // two_x:
                U[m + 1] = n_val + 1
            else:
                nex = two_x * U[m] - U[m - 1]
                U[m + 1] = nex if nex <= n_val else n_val + 1
                
        t = k * (k + 1) // 2
        tmp = t * U[i_idx]
        if tmp > n_val: return False
        tmp *= U[j_idx]
        if tmp > n_val: return False
        return True

    lo = 0
    hi = 1
    while eval_pair_leq(hi):
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if eval_pair_leq(mid):
            lo = mid
        else:
            hi = mid
    return lo

def generate_non_fundamentals(k_max):
    nf = []
    if k_max < 4: return nf
    k1_max = int(math.sqrt(k_max / 4.0)) + 2
    for k1 in range(1, k1_max + 1):
        x1 = 2 * k1 + 1
        x_prev = 1
        x_cur = x1
        while True:
            x_next = 2 * x1 * x_cur - x_prev
            k_next = (x_next - 1) // 2
            if k_next > k_max: break
            nf.append(k_next)
            x_prev = x_cur
            x_cur = x_next
    return sorted(list(set(nf)))

def mod_pow(base, exp):
    res = 1 % kMod
    base %= kMod
    while exp > 0:
        if exp & 1: res = (res * base) % kMod
        base = (base * base) % kMod
        exp >>= 1
    return res

def mod_inv(a):
    return mod_pow(a, kMod - 2)

def poly_add(a, b):
    n = max(len(a), len(b))
    c = [0] * n
    for i in range(n):
        va = a[i] if i < len(a) else 0
        vb = b[i] if i < len(b) else 0
        c[i] = (va + vb) % kMod
    return c

def poly_sub(a, b):
    n = max(len(a), len(b))
    c = [0] * n
    for i in range(n):
        va = a[i] if i < len(a) else 0
        vb = b[i] if i < len(b) else 0
        c[i] = (va - vb) % kMod
    return c

def poly_mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i in range(len(a)):
        for j in range(len(b)):
            c[i + j] = (c[i + j] + a[i] * b[j]) % kMod
    return c

def poly_scale(a, s):
    return [(x * s) % kMod for x in a]

def build_U_polys(max_idx):
    t = [1, 2] # 2k+1
    U = [[0]] * (max_idx + 1)
    U[0] = [1]
    if max_idx >= 1:
        U[1] = poly_scale(t, 2)
    for m in range(1, max_idx):
        temp = poly_mul(t, U[m])
        temp = poly_scale(temp, 2)
        U[m + 1] = poly_sub(temp, U[m - 1])
    return U

class SumPowers:
    def __init__(self, y, fact, invfact):
        self.y = y
        self.fact = fact
        self.invfact = invfact

def precompute_sum_pows(max_p):
    y = [[0] * (p + 2) for p in range(max_p + 1)]
    for p in range(max_p + 1):
        m = p + 1
        s = 0
        for i in range(1, m + 1):
            s = (s + mod_pow(i, p)) % kMod
            y[p][i] = s
            
    fact = [1] * (max_p + 2)
    invfact = [1] * (max_p + 2)
    for i in range(1, len(fact)):
        fact[i] = (fact[i - 1] * i) % kMod
    invfact[-1] = mod_inv(fact[-1])
    for i in range(len(fact) - 1, 0, -1):
        invfact[i - 1] = (invfact[i] * i) % kMod
        
    return SumPowers(y, fact, invfact)

def sum_pows(p, n, sp):
    if n <= p + 1:
        return sp.y[p][n]
        
    m = p + 1
    pre = [1] * (m + 2)
    suf = [1] * (m + 2)
    nmod = n % kMod
    
    for i in range(m + 1):
        pre[i + 1] = (pre[i] * (nmod - i)) % kMod
    for i in range(m, -1, -1):
        suf[i] = (suf[i + 1] * (nmod - i)) % kMod
        
    res = 0
    for i in range(m + 1):
        num = (pre[i] * suf[i + 1]) % kMod
        denom_inv = (sp.invfact[i] * sp.invfact[m - i]) % kMod
        term = (sp.y[p][i] * num) % kMod
        term = (term * denom_inv) % kMod
        if (m - i) & 1:
            if term != 0: term = kMod - term
        res = (res + term) % kMod
    return res

def sum_poly(coeffs, n, sp):
    res = 0
    for p in range(len(coeffs)):
        if coeffs[p] == 0: continue
        spow = sum_pows(p, n, sp)
        res = (res + coeffs[p] * spow) % kMod
    return res

def build_pairs(n_val):
    U3 = [1, 6]
    while True:
        nex = 2 * 3 * U3[-1] - U3[-2]
        U3.append(nex)
        if nex > n_val: break
    
    max_idx = len(U3) - 1
    pairs = []
    for i in range(max_idx + 1):
        for j in range(i + 1, max_idx + 1):
            tmp = U3[i] * U3[j]
            if tmp <= n_val:
                pairs.append({'i_idx': i, 'j_idx': j})
    return pairs

def compute_mod(n_val):
    pairs = build_pairs(n_val)
    max_idx = 0
    k_max = 0
    for p in pairs:
        p['k_max'] = max_k_for_pair(n_val, p['i_idx'], p['j_idx'])
        k_max = max(k_max, p['k_max'])
        max_idx = max(max_idx, p['i_idx'], p['j_idx'])
        
    nf = generate_non_fundamentals(k_max)
    nf_set = set(nf)
    
    inv2 = mod_inv(2)
    U_polys = build_U_polys(max_idx)
    t_poly = [0, inv2, inv2]
    deg_max = 0
    for p in pairs:
        r = poly_mul(U_polys[p['i_idx']], U_polys[p['j_idx']])
        p['poly'] = poly_mul(r, t_poly)
        deg_max = max(deg_max, len(p['poly']) - 1)
        
    sp = precompute_sum_pows(deg_max)
    for p in pairs:
        p['sum_all'] = sum_poly(p['poly'], p['k_max'], sp)
        
    for p in pairs:
        p['sum_nf'] = 0
        for k in nf:
            if k > p['k_max']: continue
            k_mod = k % kMod
            x_mod = (2 * k_mod + 1) % kMod
            U = [0] * (max_idx + 1)
            U[0] = 1
            if max_idx >= 1: U[1] = (2 * x_mod) % kMod
            for m in range(1, max_idx):
                U[m + 1] = (2 * x_mod * U[m] - U[m - 1]) % kMod
            t = (k_mod * (k_mod + 1)) % kMod
            t = (t * inv2) % kMod
            val = (t * U[p['i_idx']]) % kMod
            val = (val * U[p['j_idx']]) % kMod
            p['sum_nf'] = (p['sum_nf'] + val) % kMod
            
    ans = 0
    for p in pairs:
        term = (p['sum_all'] - p['sum_nf']) % kMod
        ans = (ans + term) % kMod
        
    return ans

def solve():
    n = 10**35
    ans = compute_mod(n)
    return str(ans)

if __name__ == "__main__":
    print(solve())
