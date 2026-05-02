MOD = 1000000000

def zero_matrix():
    return [[0] * 3 for _ in range(3)]

def add_matrix(a, b, mod=0):
    out = zero_matrix()
    for i in range(3):
        for j in range(3):
            if mod == 0:
                out[i][j] = a[i][j] + b[i][j]
            else:
                out[i][j] = (a[i][j] + b[i][j]) % mod
    return out

def base_matrix_for_orientation(frm, to):
    m = zero_matrix()
    m[frm][to] = 1
    return m

def mod_sub(a, b):
    return (a - b) if a >= b else (a + MOD - b)

def hit_mod(k, x, y, ascending):
    if x == y: return 0
    if ascending:
        a = mod_sub(y, x)
        b = (x + y + MOD - 2) % MOD
        return (a * b) % MOD
    a = mod_sub(x, y)
    two_k = (2 * k) % MOD
    b = mod_sub(two_k, (x + y) % MOD)
    return (a * b) % MOD

class OrientationIndex:
    def __init__(self):
        self.triples = [
            (0, 1, 2), (0, 2, 1), (1, 0, 2),
            (1, 2, 0), (2, 0, 1), (2, 1, 0)
        ]
        self.index_by_tuple = {t: i for i, t in enumerate(self.triples)}

def next_transition_counts(prev, ori, mod=0):
    nxt = [zero_matrix() for _ in range(6)]
    for id_ in range(6):
        f, t, a = ori.triples[id_]
        id1 = ori.index_by_tuple[(f, a, t)]
        id2 = ori.index_by_tuple[(a, t, f)]
        
        cur = add_matrix(prev[id1], prev[id2], mod)
        if mod == 0:
            cur[a][f] += 1
            cur[f][t] += 1
            cur[t][a] += 1
        else:
            cur[a][f] = (cur[a][f] + 1) % mod
            cur[f][t] = (cur[f][t] + 1) % mod
            cur[t][a] = (cur[t][a] + 1) % mod
        nxt[id_] = cur
    return nxt

def E_mod(c, k, a, b, cc):
    pos = [a, b, cc]
    out = hit_mod(k, b, a, False)
    for i in range(3):
        for j in range(3):
            if c[i][j] == 0: continue
            ascending = (i < j)
            h = hit_mod(k, pos[i], pos[j], ascending)
            out = (out + c[i][j] * h) % MOD
    return out

def solve_sum_last9(n_max):
    ori = OrientationIndex()
    canonical = ori.index_by_tuple[(0, 2, 1)]
    
    cur_mod = [zero_matrix() for _ in range(6)]
    for id_ in range(6):
        f, t, a = ori.triples[id_]
        cur_mod[id_] = base_matrix_for_orientation(f, t)
        
    p3, p6, p9, p10 = 1, 1, 1, 1
    total = 0
    
    for n in range(1, n_max + 1):
        if n > 1:
            cur_mod = next_transition_counts(cur_mod, ori, MOD)
            
        p3 = (p3 * 3) % MOD
        p6 = (p6 * 6) % MOD
        p9 = (p9 * 9) % MOD
        p10 = (p10 * 10) % MOD
        
        e = E_mod(cur_mod[canonical], p10, p3, p6, p9)
        total = (total + e) % MOD
        
    return total

def solve():
    return f"{solve_sum_last9(10000):09d}"

if __name__ == '__main__':
    print(solve())
