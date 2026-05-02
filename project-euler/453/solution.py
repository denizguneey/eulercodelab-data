import sys
import math
from multiprocessing import Pool, cpu_count

MOD = 135707531

def mod_pow(base, exp):
    return pow(base, exp, MOD)

def mod_inv(x):
    return mod_pow(x, MOD - 2)

class ModStats:
    def __init__(self):
        self.c3 = 0
        self.c4 = 0
        self.sumg = 0
        self.sum_area2 = 0

def process_chunk(chunk):
    start_dx, end_dx, n, m, g_mod, g1_mod, comb2_mod, g2_mod, mx_mod, ny_mod, dx2_mod, dy2_mod = chunk
    c3 = 0
    c4 = 0
    sumg = 0
    sum_area2 = 0
    
    for dx in range(start_dx, end_dx + 1):
        mx = mx_mod[dx]
        dx2 = dx2_mod[dx]
        for dy in range(1, n + 1):
            g = math.gcd(dx, dy)
            w = (mx * ny_mod[dy]) % MOD
            pairs = (w * 2) % MOD
            
            sumg = (sumg + pairs * g_mod[g]) % MOD
            if g >= 2: c3 = (c3 + pairs * g1_mod[g]) % MOD
            if g >= 3: c4 = (c4 + pairs * comb2_mod[g]) % MOD
            
            dy2 = dy2_mod[dy]
            term = (dx2 + dy2) % MOD
            term = (term + 11 * dx2 * dy2) % MOD
            term = (term - g2_mod[g] + MOD) % MOD
            
            sum_area2 = (sum_area2 + w * term) % MOD
            
    return c3, c4, sumg, sum_area2

def compute_q_mod(m, n):
    max_g = max(m, n)
    g_mod = [g % MOD for g in range(max_g + 1)]
    g1_mod = [max(0, g - 1) % MOD for g in range(max_g + 1)]
    g2_mod = [(g * g) % MOD for g in range(max_g + 1)]
    comb2_mod = [0] * (max_g + 1)
    for g in range(2, max_g + 1):
        comb2_mod[g] = ((g - 1) * (g - 2) // 2) % MOD
        
    mx_mod = [(m + 1 - dx) % MOD for dx in range(m + 1)]
    ny_mod = [(n + 1 - dy) % MOD for dy in range(n + 1)]
    dx2_mod = [(dx % MOD) * (dx % MOD) % MOD for dx in range(m + 1)]
    dy2_mod = [(dy % MOD) * (dy % MOD) % MOD for dy in range(n + 1)]
    
    c3 = 0
    c4 = 0
    sumg = 0
    sum_area2 = 0
    
    n_plus_1_mod = (n + 1) % MOD
    m_plus_1_mod = (m + 1) % MOD
    
    for dx in range(1, m + 1):
        g = dx
        pairs = (n_plus_1_mod * mx_mod[dx]) % MOD
        sumg = (sumg + pairs * g_mod[g]) % MOD
        if g >= 2: c3 = (c3 + pairs * g1_mod[g]) % MOD
        if g >= 3: c4 = (c4 + pairs * comb2_mod[g]) % MOD
        
    for dy in range(1, n + 1):
        g = dy
        pairs = (m_plus_1_mod * ny_mod[dy]) % MOD
        sumg = (sumg + pairs * g_mod[g]) % MOD
        if g >= 2: c3 = (c3 + pairs * g1_mod[g]) % MOD
        if g >= 3: c4 = (c4 + pairs * comb2_mod[g]) % MOD
        
    threads = max(1, cpu_count())
    tasks = []
    chunk_size = max(1, m // threads)
    start_dx = 1
    while start_dx <= m:
        end_dx = min(m, start_dx + chunk_size - 1)
        tasks.append((start_dx, end_dx, n, m, g_mod, g1_mod, comb2_mod, g2_mod, mx_mod, ny_mod, dx2_mod, dy2_mod))
        start_dx = end_dx + 1
        
    with Pool(threads) as pool:
        results = pool.map(process_chunk, tasks)
        
    for res in results:
        c3 = (c3 + res[0]) % MOD
        c4 = (c4 + res[1]) % MOD
        sumg = (sumg + res[2]) % MOD
        sum_area2 = (sum_area2 + res[3]) % MOD
        
    sum_area2 = (sum_area2 * mod_inv(3)) % MOD
    
    N = ((m + 1) % MOD) * ((n + 1) % MOD) % MOD
    C2 = N * (N - 1) % MOD * mod_inv(2) % MOD
    C3n = N * (N - 1) % MOD * (N - 2) % MOD * mod_inv(6) % MOD
    C4n = N * (N - 1) % MOD * (N - 2) % MOD * (N - 3) % MOD * mod_inv(24) % MOD
    
    S_coll = ((N - 3 + MOD) % MOD * c3 - 3 * c4) % MOD
    S_coll = (S_coll + MOD) % MOD
    
    line_sum = (2 * C2 + 6 * c3 + 4 * c4) % MOD
    sumB = (N * sumg - line_sum) % MOD
    sumB = (sumB + MOD) % MOD
    
    ans = C4n
    ans = (ans - S_coll + MOD) % MOD
    ans = (ans + 2 * C3n) % MOD
    ans = (ans - 2 * c3 + MOD) % MOD
    ans = (ans + sum_area2) % MOD
    ans = (ans - sumB + MOD) % MOD
    
    return ans

def solve():
    return str(compute_q_mod(12345, 6789))

if __name__ == '__main__':
    print(solve())
