def tet(r):
    if r < 0: return 0
    return (r + 1) * (r + 2) * (r + 3) // 6

def choose2(t):
    if t < 2: return 0
    return t * (t - 1) // 2

def choose3(t):
    if t < 3: return 0
    return t * (t - 1) * (t - 2) // 6

def fix_identity(n):
    total = 0
    for p in range(-n, n + 1):
        T = (n - p) // 2
        A0 = max(1, 1 - p)
        E0 = max(1, p + 1)
        base = 2 * A0 + E0
        if T < base: continue
        R = T - base
        total += tet(R)
    return total

def fix_reflection_even(n):
    total = 0
    if n < 6: return 0
    bmax = (n - 3) // 3
    for b in range(1, bmax + 1):
        M = n - 3 * b
        Amax = (M - 1) // 2
        if Amax <= 0: continue
        Asplit = (n - 4 * b + 1) // 3
        m = min(Amax, max(0, Asplit))
        
        if m >= 1:
            sum_a = m * (m + 1) // 2
            total += sum_a + (b - 1) * m
        else:
            m = 0
            
        if Amax > m:
            cnt = Amax - m
            sum_a = Amax * (Amax + 1) // 2 - m * (m + 1) // 2
            total += M * cnt - 2 * sum_a
            
    return total

def fix_reflection_odd(n):
    T = n // 2
    if T < 3: return 0
    amax = (T - 1) // 2
    return amax * (T - (amax + 1))

def H(n):
    id_val = fix_identity(n)
    r1 = n // 6
    T3 = n // 3
    r2 = choose2(T3)
    T2 = n // 2
    r3 = choose3(T2)
    fe = fix_reflection_even(n)
    fo = fix_reflection_odd(n)
    
    num = id_val + 2 * r1 + 2 * r2 + r3 + 3 * fe + 3 * fo
    return num // 12

def solve():
    return str(H(55106))

if __name__ == '__main__':
    print(solve())
