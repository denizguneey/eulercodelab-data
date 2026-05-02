def pow_leq(a, e, lim):
    r = 1
    for _ in range(e):
        r *= a
        if r > lim:
            return False
    return True

def floor_root(n, e):
    if e <= 1:
        return n
    lo = 1
    hi = min(n, 1000000000) + 1
    while lo + 1 < hi:
        mid = lo + (hi - lo) // 2
        if pow_leq(mid, e, n):
            lo = mid
        else:
            hi = mid
    return lo

def max_a_for(N, p):
    lo = 1
    hi = 1000000000 + 1
    while lo + 1 < hi:
        mid = lo + (hi - lo) // 2
        r = 1
        for _ in range(p):
            r *= mid
            if r > N:
                break
        if r + mid <= N:
            lo = mid
        else:
            hi = mid
    return lo

def sum_chain(A, e):
    if A < 2:
        return 0
    total = A - 1
    t = e
    while t <= 60:
        r = floor_root(A, t)
        if r < 2:
            break
        total += (r - 1)
        if t > 60 // e:
            break
        t *= e
    return total

def compute_D(N):
    Nm2 = N - 2
    p_max = 1
    v = 2
    while (v << 1) <= Nm2:
        v <<= 1
        p_max += 1
        
    A = [0] * (p_max + 1)
    for p in range(2, p_max + 1):
        A[p] = max_a_for(N, p)
        
    ans = 0
    for p in range(2, p_max + 1):
        ans += sum_chain(A[p], p)
        
    for e in range(2, p_max + 1):
        p = e * e
        L = 2
        while p <= p_max:
            amax = A[p]
            if amax >= 2:
                ans += (L - 1) * (amax - 1)
            ans += sum_chain(amax, e)
            if p > p_max // e:
                break
            p *= e
            L += 1
            
    return ans

def solve():
    return str(compute_D(1000000000000000000))

if __name__ == '__main__':
    print(solve())
