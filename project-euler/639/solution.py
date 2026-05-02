import math

MOD = 1000000007
MAIN_N = 1000000000000
K_MAX = 50

def mod_pow(a, e):
    return pow(a, e, MOD)

def add_mod(a, b):
    return (a + b) % MOD

def sub_mod(a, b):
    return (a - b) % MOD

def mul_mod(a, b):
    return (a * b) % MOD

def primes_up_to(n):
    if n < 2: return []
    is_prime = bytearray(n + 1)
    for i in range(n + 1): is_prime[i] = 1
    is_prime[0] = is_prime[1] = 0
    primes = []
    for i in range(2, n + 1):
        if not is_prime[i]: continue
        primes.append(i)
        if i * i <= n:
            for j in range(i * i, n + 1, i):
                is_prime[j] = 0
    return primes

class FaulhaberData:
    def __init__(self, max_k):
        self.K = max_k
        self.coeff = [[] for _ in range(max_k + 1)]
        fact = [1] * (max_k + 2)
        inv_fact = [1] * (max_k + 2)
        inv = [0] * (max_k + 3)
        for i in range(1, max_k + 2): fact[i] = (fact[i - 1] * i) % MOD
        inv_fact[max_k + 1] = mod_pow(fact[max_k + 1], MOD - 2)
        for i in range(max_k + 1, 0, -1):
            inv_fact[i - 1] = (inv_fact[i] * i) % MOD
        for i in range(1, max_k + 3):
            inv[i] = mod_pow(i, MOD - 2)
            
        def ncr(n, r):
            if r < 0 or r > n: return 0
            return (fact[n] * inv_fact[r] * inv_fact[n - r]) % MOD
            
        B = [0] * (max_k + 1)
        B[0] = 1
        if max_k >= 1: B[1] = (MOD + 1) // 2
        
        for k in range(2, max_k + 1, 2):
            s = 0
            for i in range(k):
                t = (ncr(k, i) * B[i]) % MOD
                t = (t * inv[k - i + 1]) % MOD
                s = (s + t) % MOD
            B[k] = (1 - s) % MOD
            
        for k in range(1, max_k + 1):
            v = [0] * (k + 2)
            for i in range(1, k):
                t = (B[k + 1 - i] * ncr(k, i)) % MOD
                t = (t * inv[k + 1 - i]) % MOD
                v[i] = t
            v[k] = (MOD + 1) // 2
            v[k + 1] = inv[k + 1]
            self.coeff[k] = v
            
    def eval_poly(self, n, k):
        v = self.coeff[k]
        n_mod = n % MOD
        m = 1
        acc = 0
        for c in v:
            acc = (acc + m * c) % MOD
            m = (m * n_mod) % MOD
        return acc

def build_val_data(n):
    lim = int(math.sqrt(n))
    P = primes_up_to(lim)
    lP = len(P)
    V = [[] for _ in range(lP + 1)]
    V[lP] = [n]
    
    S = set()
    
    def collect_powerful(out, m, i, n_val):
        out.append(m)
        if P[i] * m > n_val: return
        collect_powerful(out, m * P[i], i, n_val)
        for j in range(i + 1, lP):
            p = P[j]
            mm = m * p * p
            if mm > n_val: return
            collect_powerful(out, mm, j, n_val)
            
    for i in range(lP - 1, -1, -1):
        arr = [1]
        p = P[i]
        collect_powerful(arr, p * p, i, n)
        for x in arr:
            S.add(n // x)
            
        cur = sorted(list(S), reverse=True)
        V[i] = cur
        
    return P, V

def solve_total(n, K_val):
    F = FaulhaberData(K_val)
    P, V = build_val_data(n)
    lP = len(P)
    V0 = V[0]
    
    idx = {}
    for i, vl in enumerate(V0):
        idx[vl] = i
        
    Vidx = [[] for _ in range(lP + 1)]
    for i in range(lP + 1):
        vec = V[i]
        Vidx[i] = [idx[x] for x in vec]
        
    total = 0
    for k in range(1, K_val + 1):
        Svals = [0] * len(V0)
        for i_v in Vidx[0]:
            Svals[i_v] = F.eval_poly(V0[i_v], k)
            
        for i in range(lP):
            p = P[i]
            p2 = p * p
            pk = mod_pow(p % MOD, k)
            t = (pk * (pk - 1)) % MOD
            
            vec = V[i + 1]
            idv = Vidx[i + 1]
            
            for pos in range(len(vec)):
                x = vec[pos]
                if x < p2: break
                
                idx_x = idv[pos]
                cur = Svals[idx_x]
                
                pp = p2
                while pp <= x:
                    it_val = idx.get(x // pp)
                    if it_val is not None:
                        cur = (cur - t * Svals[it_val]) % MOD
                    if pp > x // p: break
                    pp *= p
                Svals[idx_x] = cur
                
        total = (total + Svals[idx[n]]) % MOD
        
    return total

def solve():
    return str(solve_total(MAIN_N, K_MAX))

if __name__ == '__main__':
    print(solve())
