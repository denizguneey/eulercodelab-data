MOD = 1000000000

def canonicalize(k, deg, comp):
    m = {}    
    nxt = 0
    new_comp = list(comp)
    for i in range(k):
        c = comp[i]
        if c not in m:
            m[c] = nxt
            nxt += 1
        new_comp[i] = m[c]
    return tuple(new_comp)

def comps_all_same(k, comp):
    for i in range(1, k):
        if comp[i] != comp[0]: return False
    return True

def transitions(k, deg, comp, remove, remove_is_one):
    out = {}
    subsets = [[]]
    for i in range(k): subsets.append([i])
    for i in range(k):
        for j in range(i + 1, k):
            subsets.append([i, j])
            
    for subset in subsets:
        if len(subset) == 2 and comp[subset[0]] == comp[subset[1]]:
            continue
            
        ok = True
        for idx in subset:
            if deg[idx] >= 2:
                ok = False
                break
        if not ok: continue
        
        ndeg = list(deg) + [len(subset)]
        ncomp = list(comp) + [0]
        nk = k + 1
        
        for idx in subset:
            ndeg[idx] += 1
            
        if len(subset) == 0:
            maxc = -1
            for i in range(k):
                maxc = max(maxc, ncomp[i])
            new_comp = maxc + 1
        elif len(subset) == 1:
            new_comp = ncomp[subset[0]]
        else:
            comp_a, comp_b = ncomp[subset[0]], ncomp[subset[1]]
            new_comp = min(comp_a, comp_b)
            for i in range(k):
                if ncomp[i] in (comp_a, comp_b):
                    ncomp[i] = new_comp
        ncomp[k] = new_comp
        
        if remove:
            leaving_deg = ndeg[0]
            if remove_is_one:
                if leaving_deg != 1: continue
            else:
                if leaving_deg != 2: continue
                
            leaving_comp = ncomp[0]
            
            ndeg = ndeg[1:]
            ncomp = ncomp[1:]
            nk = k
            
            present = False
            for i in range(nk):
                if ncomp[i] == leaving_comp:
                    present = True
                    break
            if not present: continue
            
        ncomp = canonicalize(nk, ndeg, ncomp)
        st = (nk, tuple(ndeg), ncomp)
        out[st] = out.get(st, 0) + 1
        
    return out

def is_final_generic(k, deg, comp):
    return k == 3 and comps_all_same(k, comp) and deg[0] == 2 and deg[1] == 2 and deg[2] == 1

def build_model():
    dp = {(1, (0,), (0,)): 1}
    for t in range(1, 4):
        remove = (t + 1 >= 4)
        remove_is_one = remove and (t - 2 == 1)
        nxt = {}
        for st, count in dp.items():
            for nst, ncount in transitions(st[0], st[1], st[2], remove, remove_is_one).items():
                nxt[nst] = (nxt.get(nst, 0) + count * ncount) % MOD
        dp = nxt
        
    states = []
    idx_map = {}
    d = 0
    q = []
    for st in dp:
        if st not in idx_map:
            idx_map[st] = d
            states.append(st)
            q.append(st)
            d += 1
            
    while q:
        cur = q.pop(0)
        for nst in transitions(cur[0], cur[1], cur[2], True, False):
            if nst not in idx_map:
                idx_map[nst] = d
                states.append(nst)
                q.append(nst)
                d += 1
                
    A = [[0]*d for _ in range(d)]
    for j, cur in enumerate(states):
        for nst, count in transitions(cur[0], cur[1], cur[2], True, False).items():
            i = idx_map[nst]
            A[i][j] = (A[i][j] + count) % MOD
            
    v4 = [0]*d
    for st, count in dp.items():
        v4[idx_map[st]] = (v4[idx_map[st]] + count) % MOD
        
    c = [0]*d
    for i, st in enumerate(states):
        if is_final_generic(st[0], st[1], st[2]):
            c[i] = 1
            
    return d, states, A, v4, c

def mul_mat(A, B, d):
    C = [[0]*d for _ in range(d)]
    for i in range(d):
        for k in range(d):
            if A[i][k] == 0: continue
            for j in range(d):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
    return C

def mul_mat_vec(A, v, d):
    out = [0]*d
    for i in range(d):
        out[i] = sum(A[i][j] * v[j] for j in range(d)) % MOD
    return out

def idx3(i, j, k, d):
    return (i * d + j) * d + k

def transform_tensor(T, A, d):
    U = [0] * (d*d*d)
    for a in range(d):
        for j in range(d):
            for k in range(d):
                s = 0
                for i in range(d):
                    s += A[i][a] * T[idx3(i, j, k, d)]
                U[idx3(a, j, k, d)] = s % MOD
                
    V = [0] * (d*d*d)
    for a in range(d):
        for b in range(d):
            for k in range(d):
                s = 0
                for j in range(d):
                    s += A[j][b] * U[idx3(a, j, k, d)]
                V[idx3(a, b, k, d)] = s % MOD
                
    W = [0] * (d*d*d)
    for a in range(d):
        for b in range(d):
            for c in range(d):
                s = 0
                for k in range(d):
                    s += A[k][c] * V[idx3(a, b, k, d)]
                W[idx3(a, b, c, d)] = s % MOD
                
    return W

def eval_tensor(T, v, d):
    total = 0
    for i in range(d):
        if v[i] == 0: continue
        for j in range(d):
            if v[j] == 0: continue
            vij = (v[i] * v[j]) % MOD
            for k in range(d):
                if v[k] == 0: continue
                t = T[idx3(i, j, k, d)]
                if t == 0: continue
                term = (t * vij) % MOD
                term = (term * v[k]) % MOD
                total = (total + term) % MOD
    return total

def build_powers(A, c, max_bits, d):
    A_pow = [None] * max_bits
    T_pow = [None] * max_bits
    
    A_pow[0] = A
    T1 = [0] * (d*d*d)
    for i in range(d):
        if c[i] == 0: continue
        for j in range(d):
            if c[j] == 0: continue
            cij = (c[i] * c[j]) % MOD
            for k in range(d):
                if c[k] == 0: continue
                T1[idx3(i, j, k, d)] = (cij * c[k]) % MOD
    T_pow[0] = T1
    
    for bit in range(1, max_bits):
        A_pow[bit] = mul_mat(A_pow[bit - 1], A_pow[bit - 1], d)
        transformed = transform_tensor(T_pow[bit - 1], A_pow[bit - 1], d)
        merged = [0] * (d*d*d)
        for i in range(d*d*d):
            merged[i] = (T_pow[bit-1][i] + transformed[i]) % MOD
        T_pow[bit] = merged
        
    return A_pow, T_pow

def sum_from_4(L, d, v4, A_pow, T_pow):
    if L < 4: return 0
    length = L - 3
    v = list(v4)
    sum_val = 0
    bit = 0
    while length > 0:
        if length & 1:
            sum_val = (sum_val + eval_tensor(T_pow[bit], v, d)) % MOD
            v = mul_mat_vec(A_pow[bit], v, d)
        length >>= 1
        bit += 1
    return sum_val

def compute_S_mod(L, d, v4, A_pow, T_pow):
    total = 0
    if L >= 1: total = (total + 1) % MOD
    if L >= 2: total = (total + 1) % MOD
    if L >= 3: total = (total + 1) % MOD
    if L >= 4: total = (total + sum_from_4(L, d, v4, A_pow, T_pow)) % MOD
    return total

def solve():
    L = 100000000000000
    d, states, A, v4, c = build_model()
    
    max_bits = 0
    max_len = L - 3 if L >= 4 else 1
    while max_bits < 63 and (1 << max_bits) <= max_len:
        max_bits += 1
    if max_bits == 0: max_bits = 1
    
    A_pow, T_pow = build_powers(A, c, max_bits, d)
    answer = compute_S_mod(L, d, v4, A_pow, T_pow)
    return str(answer)

if __name__ == '__main__':
    print(solve())
