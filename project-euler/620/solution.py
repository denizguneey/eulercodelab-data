import math

def clamp_ld(x, lo, hi):
    if x < lo: return lo
    if x > hi: return hi
    return x

def safe_floor(x):
    EPS = 1e-13
    y = x + EPS
    f = math.floor(y)
    
    while f + 1 <= y:
        f += 1
    while f > y:
        f -= 1
    return f

def g_value(s, p, q, PI, TWO_PI):
    A = s + p
    B = s + q
    D = p + q - TWO_PI
    
    # Using normal floats (which are C doubles) should yield sufficient precision.
    A_sq = float(A * A)
    B_sq = float(B * B)
    D_sq = D * D
    
    x_beta = clamp_ld((B_sq + D_sq - A_sq) / (2.0 * float(B) * D), -1.0, 1.0)
    x_delta = clamp_ld((A_sq + D_sq - B_sq) / (2.0 * float(A) * D), -1.0, 1.0)
    
    beta = math.acos(x_beta)
    delta = math.acos(x_delta)
    
    m_max = (float(B) * beta - float(A) * delta) / PI
    t = safe_floor(m_max)
    
    g = A + t
    return g if g > 0 else 0

def solve():
    n = 500
    PI = math.pi
    TWO_PI = 2.0 * PI
    
    total = 0
    for s in range(5, n + 1):
        m = n - s
        max_p = (m - 1) // 2
        if max_p < 5:
            continue
            
        for p in range(5, max_p + 1):
            max_q = m - p
            for q in range(p + 1, max_q + 1):
                total += g_value(s, p, q, PI, TWO_PI)
                
    return str(total)

if __name__ == '__main__':
    print(solve())
