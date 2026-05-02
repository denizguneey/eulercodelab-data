import math

MOD = 1001001011

def v2(x):
    c = 0
    while (x & 1) == 0:
        x >>= 1
        c += 1
    return c

def build_cycle_types(n, fact):
    types = []
    
    def build_rec(remaining, min_part, current):
        if remaining == 0:
            mult = [0] * (n + 1)
            valuations = []
            for length in current:
                mult[length] += 1
                valuations.append(v2(length))
                
            denom = 1
            for length in range(1, n + 1):
                m = mult[length]
                if m == 0: continue
                denom *= (length ** m)
                denom *= fact[m]
                
            perm_count = fact[n] // denom
            types.append({
                'mult': mult,
                'valuations': valuations,
                'perm_count': perm_count
            })
            return
            
        for part in range(min_part, remaining + 1):
            current.append(part)
            build_rec(remaining - part, part, current)
            current.pop()
            
    build_rec(n, 1, [])
    return types

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.forced = [0] * n
        
    def find(self, x):
        r = x
        while self.parent[r] != r:
            r = self.parent[r]
        curr = x
        while self.parent[curr] != curr:
            p = self.parent[curr]
            self.parent[curr] = r
            curr = p
        return r
        
    def unite(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b: return
        if self.rank[a] < self.rank[b]:
            a, b = b, a
        self.parent[b] = a
        self.forced[a] |= self.forced[b]
        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1
            
    def set_forced(self, a):
        r = self.find(a)
        self.forced[r] = 1

def parity_rank(rows_v2, cols_v2):
    r = len(rows_v2)
    s = len(cols_v2)
    vars = r + s
    dsu = DSU(vars)
    
    for i in range(r):
        for j in range(s):
            if rows_v2[i] == cols_v2[j]:
                dsu.unite(i, r + j)
            elif rows_v2[i] > cols_v2[j]:
                dsu.set_forced(i)
            else:
                dsu.set_forced(r + j)
                
    seen = [0] * vars
    free_components = 0
    for v in range(vars):
        root = dsu.find(v)
        if seen[root]: continue
        seen[root] = 1
        if not dsu.forced[root]:
            free_components += 1
            
    return vars - free_components

def orbit_count(a, b, gcd_tbl, n):
    o = 0
    for p in range(1, n + 1):
        mp = a['mult'][p]
        if mp == 0: continue
        for q in range(1, n + 1):
            mq = b['mult'][q]
            if mq == 0: continue
            o += mp * mq * gcd_tbl[p][q]
    return o

def compute_c_exact(n):
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i
        
    types = build_cycle_types(n, fact)
    
    gcd_tbl = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            gcd_tbl[i][j] = math.gcd(i, j)
            
    total = 0
    tcount = len(types)
    for i in range(tcount):
        a = types[i]
        for j in range(tcount):
            b = types[j]
            o = orbit_count(a, b, gcd_tbl, n)
            rk = parity_rank(a['valuations'], b['valuations'])
            exp = o - rk
            total += a['perm_count'] * b['perm_count'] * (1 << exp)
            
    denom = fact[n] * fact[n]
    return total // denom

def solve():
    c20 = compute_c_exact(20)
    return str(c20 % MOD)

if __name__ == '__main__':
    print(solve())
