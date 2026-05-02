import sys
import math
from multiprocessing import Pool, cpu_count

def gcd(a, b):
    a = abs(a)
    b = abs(b)
    while b:
        a, b = b, a % b
    return a

def gcd3(a, b, c):
    return gcd(gcd(a, b), c)

def pow_gauss(x, y, n):
    rx, ry = 1, 0
    for _ in range(n):
        nx = rx * x - ry * y
        ny = rx * y + ry * x
        rx, ry = nx, ny
    return rx, ry

def denom_required(p, q, A, B, D):
    e = p - q
    aq_x, aq_y = pow_gauss(A, B, q)
    aec_x, aec_y = pow_gauss(A, -B, e)
    
    Deq = D ** (e - q)
    ux = e * aq_x * Deq + q * aec_x
    uy = e * aq_y * Deq + q * aec_y
    
    De = D ** e
    g0 = gcd3(De, ux, uy)
    
    den = De // g0
    return den, ux, uy, g0

def variations(a, b):
    return [
        (a, b), (a, -b), (-a, b), (-a, -b),
        (b, a), (b, -a), (-b, a), (-b, -a)
    ]

def primitive_triples(Cmax):
    out = []
    mlim = int(math.sqrt(Cmax)) + 2
    for m in range(2, mlim + 1):
        for n in range(1, m):
            if (m - n) % 2 == 0: continue
            if math.gcd(m, n) != 1: continue
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
            if c > Cmax: continue
            out.append((a, b, c))
    return out

def sieve_mu_phi(N):
    mu = [0] * (N + 1)
    phi = [0] * (N + 1)
    primes = []
    comp = bytearray(N + 1)
    
    mu[1] = 1
    phi[1] = 1
    
    for i in range(2, N + 1):
        if not comp[i]:
            primes.append(i)
            phi[i] = i - 1
            mu[i] = -1
        for p in primes:
            v = i * p
            if v > N: break
            comp[v] = 1
            if i % p == 0:
                phi[v] = phi[i] * p
                mu[v] = 0
                break
            else:
                phi[v] = phi[i] * (p - 1)
                mu[v] = -mu[i]
                
    return mu, phi

pool_mu = None
def init_worker(shared_mu):
    global pool_mu
    pool_mu = shared_mu

def worker_B(args):
    d_start, d_end, N = args
    mu = pool_mu
    local = [0] * (N + 1)
    for d in range(d_start, d_end + 1):
        md = mu[d]
        if md == 0:
            continue
        coef = md * d
        for p in range(d, N + 1, d):
            m = (p - 1) // (2 * d)
            local[p] += coef * (m * (m + 1) // 2)
    return local

def compute_B_parallel(N, mu):
    threads = max(1, cpu_count())
    threads = min(threads, 8)
    
    tasks = []
    block = N // threads
    cur = 1
    for t in range(threads):
        start = cur
        end = N if t == threads - 1 else cur + block - 1
        tasks.append((start, end, N))
        cur = end + 1
        
    with Pool(threads, initializer=init_worker, initargs=(mu,)) as pool:
        locals_res = pool.map(worker_B, tasks)
        
    B = [0] * (N + 1)
    for p in range(1, N + 1):
        B[p] = sum(loc[p] for loc in locals_res)
        
    return B

def compute_T(N):
    mu, phi = sieve_mu_phi(N)
    B = compute_B_parallel(N, mu)
    
    total = 0
    for p in range(3, N + 1):
        A = phi[p] // 2
        if A == 0: continue
        Bsum = B[p]
        
        if p % 2 != 0:
            inner = 4 * p * A - 2 * Bsum
        else:
            if p % 4 == 0:
                inner = 4 * p * A
            else:
                inner = 4 * p * A - 4 * Bsum
                
        M = N // p
        total += inner * (M * (M + 1) // 2)
        
    Dmax = int(math.sqrt(N // 3)) + 2
    triples = primitive_triples(Dmax)
    
    maxPextra = 12
    for p in range(3, min(N, maxPextra) + 1):
        M = N // p
        for q in range(1, (p + 1) // 2):
            if math.gcd(p, q) != 1: continue
            
            for a, b, D in triples:
                for A, Bv in variations(a, b):
                    den, ux, uy, g0 = denom_required(p, q, A, Bv, D)
                    if den > M: continue
                    
                    bx = ux // g0
                    by = uy // g0
                    base_abs = abs(bx) + abs(by)
                    
                    mmax = M // den
                    total += base_abs * (mmax * (mmax + 1) // 2)
                    
    return total

def solve():
    return str(compute_T(1000000))

if __name__ == '__main__':
    print(solve())
