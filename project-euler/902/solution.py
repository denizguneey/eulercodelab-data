import math
from typing import List

MOD = 1000000007
A = 1000000007

def compute_counts(Acyc: List[int], Bcyc: List[int], g: int) -> List[int]:
    s = len(Acyc)
    t = len(Bcyc)
    A_r = [[] for _ in range(g)]
    B_r = [[] for _ in range(g)]
    for i in range(s):
        A_r[i % g].append(Acyc[i])
    for i in range(t):
        B_r[i % g].append(Bcyc[i])
        
    for r in range(g):
        A_r[r].sort()
        B_r[r].sort()
        
    f = [[0] * g for _ in range(g)]
    for r in range(g):
        for rp in range(g):
            cnt = 0
            a = A_r[r]
            b = B_r[rp]
            j = 0
            b_len = len(b)
            for x in a:
                while j < b_len and b[j] < x:
                    j += 1
                cnt += j
            f[r][rp] = cnt
            
    counts = [0] * g
    for rd in range(g):
        total = 0
        for r in range(g):
            total += f[r][(r + rd) % g]
        counts[rd] = total
    return counts

def solve():
    m = 100
    n = m * (m + 1) // 2
    
    tau = [0] * (n + 1)
    tau_inv = [0] * (n + 1)
    sigma = [0] * (n + 1)
    pi = [0] * (n + 1)
    
    for i in range(1, n + 1):
        tau[i] = ((A * i) % n) + 1
        
    for i in range(1, n + 1):
        tau_inv[tau[i]] = i
        
    for i in range(1, n):
        sigma[i] = i + 1
        
    prev = 0
    for k in range(1, m + 1):
        t = k * (k + 1) // 2
        sigma[t] = prev + 1
        prev = t
        
    for i in range(1, n + 1):
        pi[i] = tau_inv[sigma[tau[i]]]
        
    cycles = []
    cycle_id = [-1] * (n + 1)
    pos_in = [-1] * (n + 1)
    visited = [False] * (n + 1)
    
    for i in range(1, n + 1):
        if visited[i]:
            continue
        cyc = []
        cur = i
        while not visited[cur]:
            visited[cur] = True
            pos_in[cur] = len(cyc)
            cycle_id[cur] = len(cycles)
            cyc.append(cur)
            cur = pi[cur]
        cycles.append(cyc)
        
    fact = [1] * (n + 1)
    weight = [0] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = (fact[i - 1] * i) % MOD
    for i in range(1, n + 1):
        weight[i] = fact[n - i]
        
    m_fact = 1
    for i in range(1, m + 1):
        m_fact = (m_fact * i) % MOD
        
    num_cycles = len(cycles)
    cycle_len = [len(c) for c in cycles]
    
    maxL = 1
    for i in range(num_cycles):
        for j in range(num_cycles):
            g = math.gcd(cycle_len[i], cycle_len[j])
            L = cycle_len[i] // g * cycle_len[j]
            if L > maxL: maxL = L
            
    inv = [1] * (maxL + 1)
    for i in range(2, maxL + 1):
        inv[i] = MOD - (MOD // i) * inv[MOD % i] % MOD
        
    pair_data = [[None] * num_cycles for _ in range(num_cycles)]
    for ci in range(num_cycles):
        for cj in range(num_cycles):
            s = cycle_len[ci]
            t = cycle_len[cj]
            g = math.gcd(s, t)
            L = s // g * t
            mul = (m_fact * inv[L]) % MOD
            counts = compute_counts(cycles[ci], cycles[cj], g)
            pair_data[ci][cj] = {'g': g, 'mul': mul, 'counts': counts}
            
    total = m_fact % MOD
    
    local = 0
    for i in range(1, n + 1):
        wi = weight[i]
        ci = cycle_id[i]
        pos_i = pos_in[i]
        for j in range(i + 1, n + 1):
            cj = cycle_id[j]
            pos_j = pos_in[j]
            pd = pair_data[ci][cj]
            g = pd['g']
            r = (pos_j - pos_i) % g
            if r < 0:
                r += g
            cnt = pd['counts'][r]
            add = (wi * (cnt * pd['mul'] % MOD)) % MOD
            local += add
            if local >= MOD:
                local -= MOD
                
    total += local
    total %= MOD
    return str(total)

if __name__ == "__main__":
    print(solve())
