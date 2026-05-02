import math
import multiprocessing
import bisect

def max_inradius_for_perimeter(P):
    bound = P * math.sqrt(3.0) / 18.0
    r_max = int(math.floor(bound + 1e-12))
    return max(0, r_max)

def build_spf(limit):
    spf = [0] * (limit + 1)
    if limit >= 1:
        spf[1] = 1
    for i in range(2, limit + 1):
        if spf[i] == 0:
            spf[i] = i
            if i * i <= limit:
                for j in range(i * i, limit + 1, i):
                    if spf[j] == 0:
                        spf[j] = i
    return spf

def factorize(n, spf):
    factors = []
    while n > 1:
        p = spf[n]
        cnt = 0
        while n % p == 0:
            n //= p
            cnt += 1
        factors.append((p, cnt))
    return factors

def build_legs(r, r2, max_x, spf):
    factors = factorize(r, spf)
    divisors = [1]
    for p, cnt in factors:
        exp = 2 * cnt
        base_len = len(divisors)
        p_pow = 1
        for e in range(1, exp + 1):
            p_pow *= p
            for i in range(base_len):
                divisors.append(divisors[i] * p_pow)
                
    legs = []
    for d in divisors:
        if d > r:
            continue
        d2 = r2 // d
        if (d + d2) % 2 != 0:
            continue
        x = (d2 - d) // 2
        if x <= 0 or x > max_x:
            continue
        t = (d2 + d) // 2
        legs.append((x, t))
        
    legs.sort(key=lambda leg: leg[0])
    return legs

def init_worker(shared_P, shared_spf):
    global P_half, s_spf, P
    P = shared_P
    P_half = P // 2
    s_spf = shared_spf

def worker_chunk(args):
    start, end = args
    total = 0
    for r in range(start, end + 1):
        r2 = r * r
        legs = build_legs(r, r2, P_half, s_spf)
        if len(legs) < 2:
            continue
            
        xs = [l[0] for l in legs]
        ts = [l[1] for l in legs]
        n_legs = len(legs)
        
        for i in range(n_legs):
            x = xs[i]
            tx = ts[i]
            for j in range(i, n_legs):
                y = xs[j]
                ty = ts[j]
                denom = x * y - r2
                if denom <= 0:
                    continue
                    
                numer = r2 * (x + y)
                if numer % denom != 0:
                    continue
                    
                z_u = numer // denom
                max_z = P_half - x - y
                if max_z <= 0 or z_u > max_z:
                    continue
                    
                z = z_u
                if z < y:
                    continue
                    
                idx = bisect.bisect_left(xs, z)
                if idx == n_legs or xs[idx] != z:
                    continue
                    
                tz = ts[idx]
                p = 2 * (x + y + z)
                L = p + tx + ty + tz
                total += L
                
    return total

def compute_sum(P, spf, r_max, threads=None):
    if r_max <= 0:
        return 0
        
    if threads is None:
        threads = multiprocessing.cpu_count()
        
    if threads == 1 or r_max < 200:
        init_worker(P, spf)
        return worker_chunk((1, r_max))
        
    chunks = []
    chunk_size = (r_max + threads - 1) // threads
    for i in range(1, r_max + 1, chunk_size):
        chunks.append((i, min(r_max, i + chunk_size - 1)))
        
    with multiprocessing.Pool(processes=threads, initializer=init_worker, initargs=(P, spf)) as pool:
        results = pool.map(worker_chunk, chunks)
        
    return sum(results)

def solve():
    P = 10000000
    r_max = max_inradius_for_perimeter(P)
    spf = build_spf(r_max)
    ans = compute_sum(P, spf, r_max)
    return str(ans)

if __name__ == '__main__':
    print(solve())
