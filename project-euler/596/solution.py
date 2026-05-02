import math
from multiprocessing import Pool, cpu_count

MOD = 1000000007
INV2 = 500000004

def worker_part1(args):
    start, end, N = args
    ans = 0
    for i in range(start, end):
        ans += i * (N // i)
    return ans % MOD

def worker_part2(args):
    start, end, M, N = args
    ans = 0
    for q in range(start, end):
        l = N // (q + 1) + 1
        r = N // q
        if r <= M: continue
        if l <= M: l = M + 1
        if l > r: continue
        
        cnt = (r - l + 1) % MOD
        lr = (l + r) % MOD
        s = (lr * cnt * INV2) % MOD
        ans = (ans + (q % MOD) * s) % MOD
    return ans % MOD

def S_mod(N):
    if N == 0: return 0
    M = math.isqrt(N)
    
    threads = max(1, cpu_count())
    
    tasks1 = []
    chunk1 = (M + threads - 1) // threads
    for t in range(threads):
        s = 1 + t * chunk1
        e = min(M + 1, 1 + (t + 1) * chunk1)
        if s < e:
            tasks1.append((s, e, N))
            
    qmax = N // (M + 1)
    tasks2 = []
    chunk2 = (qmax + threads - 1) // threads
    for t in range(threads):
        s = 1 + t * chunk2
        e = min(qmax + 1, 1 + (t + 1) * chunk2)
        if s < e:
            tasks2.append((s, e, M, N))
            
    ans = 0
    if len(tasks1) + len(tasks2) > 2:
        with Pool(threads) as pool:
            ans1 = pool.map(worker_part1, tasks1)
            ans2 = pool.map(worker_part2, tasks2)
        ans = (sum(ans1) + sum(ans2)) % MOD
    else:
        for t in tasks1:
            ans = (ans + worker_part1(t)) % MOD
        for t in tasks2:
            ans = (ans + worker_part2(t)) % MOD
            
    return ans % MOD

def T_mod(r):
    N = r * r
    sN = S_mod(N)
    sN4 = S_mod(N // 4)
    term = (sN - (4 * sN4) % MOD) % MOD
    if term < 0: term += MOD
    
    t = (1 + 8 * term) % MOD
    return t

def solve():
    return str(T_mod(100000000))

if __name__ == '__main__':
    print(solve())
