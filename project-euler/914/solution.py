import math

def isqrt(x):
    return math.isqrt(x)

def best_for_n(R, n):
    C = 2 * R
    nn = n * n
    if nn >= C:
        return 0
        
    t = C - 1 - nn
    m = isqrt(t)
    if m <= n:
        return 0
        
    if ((m ^ n) & 1) == 0:
        m -= 1
        
    while m > n and math.gcd(m, n) != 1:
        m -= 2
        
    if m <= n:
        return 0
        
    return n * (m - n)

def fast_F(R):
    C = 2 * R
    sqrt2 = math.sqrt(2.0)
    denom = 4.0 + 2.0 * sqrt2
    Cld = float(C - 1)
    
    n0 = round(math.sqrt(Cld / denom))
    if n0 == 0:
        n0 = 1
        
    best = 0
    kWindow = 4096
    for d in range(-kWindow, kWindow + 1):
        ni = n0 + d
        if ni <= 0:
            continue
        cand = best_for_n(R, ni)
        if cand > best:
            best = cand
            
    def ub_real(n):
        if n <= 0:
            return 0.0
        t = Cld - n * n
        if t <= 0:
            return 0.0
        return n * (math.sqrt(t) - n)
        
    n0ld = float(n0)
    nmaxld = math.sqrt(Cld / 2.0)
    
    left = n0ld
    right = n0ld
    
    if ub_real(n0ld) > float(best):
        lo = 0.0
        hi = n0ld
        for _ in range(140):
            mid = (lo + hi) * 0.5
            if ub_real(mid) > float(best):
                hi = mid
            else:
                lo = mid
        left = hi
        
        lo = n0ld
        hi = nmaxld
        for _ in range(140):
            mid = (lo + hi) * 0.5
            if ub_real(mid) > float(best):
                lo = mid
            else:
                hi = mid
        right = lo
        
    L = 1
    if left > 16.0:
        L = int(math.floor(left)) - 16
        
    n_max = isqrt((C - 1) // 2)
    Rn = int(math.ceil(right)) + 16
    if Rn > n_max:
        Rn = n_max
        
    for n in range(L, Rn + 1):
        nn = n * n
        if nn >= C:
            break
        mmax = isqrt(C - 1 - nn)
        if mmax <= n:
            continue
        ub = n * (mmax - n)
        if ub <= best:
            continue
            
        cand = best_for_n(R, n)
        if cand > best:
            best = cand
            
    return best

def solve():
    return str(fast_F(1000000000000000000))

if __name__ == "__main__":
    print(solve())
