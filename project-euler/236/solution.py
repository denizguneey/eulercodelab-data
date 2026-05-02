import math

NUM_PRODUCTS = 5
A = [5248, 1312, 2624, 5760, 3936]
B = [640, 1888, 3776, 3776, 5664]

GROUPS = 3
GROUP_PRODUCTS = [[0, -1, -1], [1, 2, 4], [3, -1, -1]]
GROUP_SIZE = [1, 3, 1]
GROUP_B_NUM = [5, 59, 59]
GROUP_A_DEN = [41, 41, 90]

SA = 18880
SB = 15744

def reduce_fraction(u, v):
    if v < 0:
        u = -u
        v = -v
    g = math.gcd(abs(u), abs(v))
    return (u // g, v // g)

def floor_div(a, b):
    return a // b

def ceil_div(a, b):
    return -((-a) // b)

def extended_gcd(a, b):
    if b == 0:
        return (1 if a >= 0 else -1, 0, abs(a))
    x1, y1, g = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return (x, y, g)

def tighten_range(p, q, low, high, t_low, t_high):
    if low > high:
        return False, t_low, t_high
    if q == 0:
        if p >= low and p <= high:
            return True, t_low, t_high
        return False, t_low, t_high

    if q > 0:
        l = ceil_div(low - p, q)
        r = floor_div(high - p, q)
    else:
        l = ceil_div(high - p, q)
        r = floor_div(low - p, q)

    if l > r:
        return False, t_low, t_high
        
    if l > t_low:
        t_low = l
    if r < t_high:
        t_high = r
        
    return t_low <= t_high, t_low, t_high

def exists_bounded_linear(c1, l1, h1, c2, l2, h2, rhs):
    if l1 > h1 or l2 > h2:
        return False
    if c1 == 0 and c2 == 0:
        return rhs == 0
    if c1 == 0:
        if rhs % c2 != 0:
            return False
        s2 = rhs // c2
        return l2 <= s2 <= h2
    if c2 == 0:
        if rhs % c1 != 0:
            return False
        s1 = rhs // c1
        return l1 <= s1 <= h1

    x0, y0, g = extended_gcd(c1, c2)
    if rhs % g != 0:
        return False

    scale = rhs // g
    step1 = c2 // g
    step2 = -c1 // g

    base1 = x0 * scale
    base2 = y0 * scale

    t_low = -10**20
    t_high = 10**20

    success, t_low, t_high = tighten_range(base1, step1, l1, h1, t_low, t_high)
    if not success:
        return False
    success, t_low, t_high = tighten_range(base2, step2, l2, h2, t_low, t_high)
    if not success:
        return False
        
    return t_low <= t_high

def generate_candidates():
    candidates = []
    for a in range(1, A[0] + 1):
        for b in range(1, B[0] + 1):
            m_u, m_v = reduce_fraction(41 * b, 5 * a)
            if m_u > m_v:
                candidates.append((m_u, m_v))
    
    # Sort correctly by fraction value
    def fraction_key(m):
        return m[0] / m[1]
        
    candidates = sorted(list(set(candidates)), key=fraction_key)
    return candidates

def candidate_works(m):
    m_u, m_v = m
    if m_u <= m_v:
        return False

    min_sum = [1, 3, 1]
    max_sum = [0, 0, 0]
    coef = [0, 0, 0]

    for g in range(GROUPS):
        N, D = reduce_fraction(m_u * GROUP_B_NUM[g], m_v * GROUP_A_DEN[g])

        upper_sum = 0
        for j in range(GROUP_SIZE[g]):
            idx = GROUP_PRODUCTS[g][j]
            upper = min(A[idx] // D, B[idx] // N)
            if upper < 1:
                return False
            upper_sum += upper
            
        max_sum[g] = upper_sum
        coef[g] = m_v * SB * D - m_u * SA * N

    for s0 in range(min_sum[0], max_sum[0] + 1):
        rhs = - (coef[0] * s0)
        if exists_bounded_linear(coef[1], min_sum[1], max_sum[1], coef[2], min_sum[2], max_sum[2], rhs):
            return True

    return False

def solve():
    candidates = generate_candidates()
    solutions = []
    
    for cand in candidates:
        if candidate_works(cand):
            solutions.append(cand)
            
    best = solutions[-1]
    return f"{best[0]}/{best[1]}"

if __name__ == '__main__':
    print(solve())
