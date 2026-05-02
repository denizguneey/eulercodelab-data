import sys
import collections

MOD = 1000000007

def mod_pow(a, e):
    r = 1
    a %= MOD
    while e > 0:
        if e & 1: r = (r * a) % MOD
        a = (a * a) % MOD
        e >>= 1
    return r

def build_dfa():
    def get_id(a, b, p):
        return p * 25 + a * 5 + b
        
    nfa_states = 50
    nfa = [[0] * 5 for _ in range(nfa_states)]
    
    for p in range(2):
        for a in range(5):
            for b in range(5):
                sid = get_id(a, b, p)
                for c in range(5):
                    mask = 0
                    if c >= a + b:
                        remaining = c - a - b
                        for use_pair in range(2):
                            if use_pair and p: continue
                            if use_pair and remaining < 2: continue
                            rem2 = remaining - 2 * use_pair
                            for q in range(5):
                                if q > rem2: break
                                if (rem2 - q) % 3 != 0: continue
                                ns = get_id(q, a, p or use_pair)
                                mask |= (1 << ns)
                    nfa[sid][c] = mask
                    
    start_mask = 1 << get_id(0, 0, 0)
    index_map = {start_mask: 0}
    masks = [start_mask]
    q = collections.deque([start_mask])
    trans = []
    
    while q:
        mask = q.popleft()
        cur = index_map[mask]
        if cur >= len(trans):
            trans.append([0] * 5)
            
        for c in range(5):
            next_mask = 0
            tmp = mask
            while tmp:
                i = (tmp & -tmp).bit_length() - 1
                tmp &= tmp - 1
                next_mask |= nfa[i][c]
                
            if next_mask not in index_map:
                nxt = len(index_map)
                index_map[next_mask] = nxt
                masks.append(next_mask)
                q.append(next_mask)
            else:
                nxt = index_map[next_mask]
            trans[cur][c] = nxt
            
    acc0_bit = 1 << get_id(0, 0, 0)
    acc1_bit = 1 << get_id(0, 0, 1)
    
    accept0 = [i for i, m in enumerate(masks) if (m & acc0_bit)]
    accept1 = [i for i, m in enumerate(masks) if (m & acc1_bit)]
    
    return trans, accept0, accept1

class MahjongCounter:
    def __init__(self, max_t):
        self.max_t = max_t
        self.max_tiles = 3 * max_t + 2
        self.max_len = 3 * max_t + 2
        self.max_blocks = max_t + 1
        self.stride = self.max_tiles + 1
        self.trans, self.accept0, self.accept1 = build_dfa()
        
        self.fact = [1] * (self.max_blocks + 1)
        self.inv_fact = [1] * (self.max_blocks + 1)
        for i in range(1, self.max_blocks + 1):
            self.fact[i] = (self.fact[i - 1] * i) % MOD
        self.inv_fact[self.max_blocks] = mod_pow(self.fact[self.max_blocks], MOD - 2)
        for i in range(self.max_blocks, 0, -1):
            self.inv_fact[i - 1] = (self.inv_fact[i] * i) % MOD
            
        self.build_block_counts()
        self.build_block_dp()

    def comb_small(self, N, k):
        if k < 0 or N < k: return 0
        res = 1
        for i in range(k):
            term = (N - i) % MOD
            if term < 0: term += MOD
            res = (res * term) % MOD
        res = (res * self.inv_fact[k]) % MOD
        return res

    def build_block_counts(self):
        S = len(self.trans)
        size = S * self.stride
        cur = [0] * size
        cur[0] = 1
        
        self.triple_blocks = []
        self.pair_blocks = []
        
        for L in range(1, self.max_len + 1):
            nxt = [0] * size
            for s in range(S):
                base = s * self.stride
                for m in range(self.max_tiles + 1):
                    val = cur[base + m]
                    if not val: continue
                    for c in range(1, 5):
                        nm = m + c
                        if nm > self.max_tiles: break
                        ns = self.trans[s][c]
                        idx = ns * self.stride + nm
                        nxt[idx] = (nxt[idx] + val) % MOD
                        
            sum0 = [0] * (self.max_tiles + 1)
            sum1 = [0] * (self.max_tiles + 1)
            
            for s in self.accept0:
                base = s * self.stride
                for m in range(self.max_tiles + 1):
                    sum0[m] = (sum0[m] + nxt[base + m]) % MOD
            for s in self.accept1:
                base = s * self.stride
                for m in range(self.max_tiles + 1):
                    sum1[m] = (sum1[m] + nxt[base + m]) % MOD
                    
            for M in range(self.max_tiles + 1):
                if sum0[M] and M % 3 == 0:
                    self.triple_blocks.append((L, M, sum0[M]))
                if sum1[M] and M % 3 == 2:
                    self.pair_blocks.append((L, M, sum1[M]))
                    
            cur = nxt

    def convolve_add(self, dp, blocks, out):
        if not blocks: return
        for Lb, Mb, cnt in blocks:
            Llimit = self.max_len - Lb
            Mlimit = self.max_tiles - Mb
            for L in range(Llimit + 1):
                base = L * self.stride
                out_base = (L + Lb) * self.stride + Mb
                for M in range(Mlimit + 1):
                    val = dp[base + M]
                    if not val: continue
                    idx = out_base + M
                    out[idx] = (out[idx] + val * cnt) % MOD

    def build_block_dp(self):
        size = (self.max_len + 1) * self.stride
        self.dp0 = [[0] * size for _ in range(self.max_blocks + 1)]
        self.dp1 = [[0] * size for _ in range(self.max_blocks + 1)]
        self.dp0[0][0] = 1
        
        for k in range(self.max_blocks):
            self.convolve_add(self.dp0[k], self.triple_blocks, self.dp0[k + 1])
            self.convolve_add(self.dp1[k], self.triple_blocks, self.dp1[k + 1])
            self.convolve_add(self.dp0[k], self.pair_blocks, self.dp1[k + 1])

    def poly_mul(self, a, b, t):
        res = [0] * (t + 1)
        for i in range(min(t + 1, len(a))):
            if not a[i]: continue
            for j in range(min(t + 1 - i, len(b))):
                if not b[j]: continue
                res[i + j] = (res[i + j] + a[i] * b[j]) % MOD
        return res

    def poly_pow(self, base, exp, t):
        res = [0] * (t + 1)
        res[0] = 1
        while exp > 0:
            if exp & 1: res = self.poly_mul(res, base, t)
            exp >>= 1
            if exp: base = self.poly_mul(base, base, t)
        return res

    def solve(self, n, s, t):
        if s == 0 or t > self.max_t: return 0
        
        A = [0] * (self.max_tiles + 1)
        B = [0] * (self.max_tiles + 1)
        
        for k in range(self.max_blocks + 1):
            for L in range(self.max_len + 1):
                N_val = n - L + 1
                if N_val < k: continue
                comb = self.comb_small(N_val, k)
                if comb == 0: continue
                
                base = L * self.stride
                dp0_k = self.dp0[k]
                dp1_k = self.dp1[k]
                
                for M in range(self.max_tiles + 1):
                    if dp0_k[base + M]:
                        A[M] = (A[M] + dp0_k[base + M] * comb) % MOD
                    if dp1_k[base + M]:
                        B[M] = (B[M] + dp1_k[base + M] * comb) % MOD
                        
        G = [0] * (t + 1)
        H = [0] * (t + 1)
        for k in range(t + 1):
            idxG = 3 * k
            idxH = 3 * k + 2
            if idxG <= self.max_tiles: G[k] = A[idxG]
            if idxH <= self.max_tiles: H[k] = B[idxH]
            
        Gpow = self.poly_pow(G, s - 1, t)
        total = 0
        for i in range(t + 1):
            total = (total + H[i] * Gpow[t - i]) % MOD
        total = (total * (s % MOD)) % MOD
        return total

def solve():
    n = 100000000
    s = 100000000
    t = 30
    counter = MahjongCounter(t)
    return str(counter.solve(n, s, t))

if __name__ == '__main__':
    print(solve())
