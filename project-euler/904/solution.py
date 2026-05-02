import math
from typing import List

class Fraction:
    def __init__(self, p, q):
        self.p = p
        self.q = q

def tan_theta_from_u(u):
    u2 = u * u
    return 3.0 * u * (u2 - 1.0) / ((u2 + 1.0) * (u2 + 1.0))

def farey_prev(lo, hi, N):
    k = (N + hi.q) // lo.q
    return Fraction(k * lo.p - hi.p, k * lo.q - hi.q)

def farey_next(lo, hi, N):
    k = (N + lo.q) // hi.q
    return Fraction(k * hi.p - lo.p, k * hi.q - lo.q)

def farey_bounds(x, N):
    a = []
    y = x
    for _ in range(64):
        ai = int(math.floor(y))
        a.append(ai)
        frac = y - ai
        if abs(frac) < 1e-15:
            break
        y = 1.0 / frac

    ps = []
    qs = []
    p_minus2 = 0
    p_minus1 = 1
    q_minus2 = 1
    q_minus1 = 0

    for ai in a:
        p = ai * p_minus1 + p_minus2
        q = ai * q_minus1 + q_minus2
        ps.append(p)
        qs.append(q)
        if q > N:
            break
        p_minus2 = p_minus1
        p_minus1 = p
        q_minus2 = q_minus1
        q_minus1 = q

    idx = 0
    while idx < len(qs) and qs[idx] <= N:
        idx += 1

    if idx == 0:
        return Fraction(0, 1), Fraction(1, 0)

    if idx == len(qs):
        return Fraction(ps[-1], qs[-1]), Fraction(ps[-1], qs[-1])

    p_prev = ps[idx - 1]
    q_prev = qs[idx - 1]
    p_prevprev = ps[idx - 2] if idx >= 2 else 1
    q_prevprev = qs[idx - 2] if idx >= 2 else 0

    t = (N - q_prevprev) // q_prev
    p_cand = p_prevprev + t * p_prev
    q_cand = q_prevprev + t * q_prev

    if p_prev / q_prev < x:
        return Fraction(p_prev, q_prev), Fraction(p_cand, q_cand)
    else:
        return Fraction(p_cand, q_cand), Fraction(p_prev, q_prev)

def is_valid_fraction(f, L):
    if f.q <= 0 or f.p <= 0:
        return False
    if f.p <= f.q:
        return False
    if ((f.p + f.q) & 1) == 0:
        return False
    if math.gcd(f.p, f.q) != 1:
        return False
    return f.p * f.p + f.q * f.q <= L

def find_valid_lower(lo, hi, N, L):
    if lo.p <= lo.q:
        return Fraction(0, 0)
    for _ in range(100000):
        if is_valid_fraction(lo, L):
            return lo
        prev = farey_prev(lo, hi, N)
        hi = lo
        lo = prev
        if lo.q == 0:
            break
    return Fraction(0, 0)

def find_valid_upper(lo, hi, N, L):
    for _ in range(100000):
        if is_valid_fraction(hi, L):
            return hi
        nxt = farey_next(lo, hi, N)
        lo = hi
        hi = nxt
        if hi.q == 0:
            break
    return Fraction(0, 0)

def evaluate_fraction(f, t_alpha, L):
    if f.p == 0 or f.q == 0:
        return None
    m = f.p
    n = f.q
    m2 = m * m
    n2 = n * n
    a = m2 - n2
    b = 2 * m * n
    c = m2 + n2
    k = L // c
    if k == 0:
        return None

    t = 3.0 * a * b / (2.0 * c * c)
    diff = abs(t - t_alpha) / (1.0 + t * t_alpha)

    sum_val = k * (a + b + c)
    area = k * k * a * b
    return {'diff': diff, 'sum': sum_val, 'area': area}

def best_candidate_for_u(u_target, t_alpha, L):
    if u_target <= 1.0:
        return None

    R = math.sqrt(L)
    denom = math.sqrt(1.0 + u_target * u_target)
    N = int(math.floor(R / denom))
    if N < 1:
        N = 1

    lo, hi = farey_bounds(u_target, N)
    lo_valid = find_valid_lower(lo, hi, N, L)
    hi_valid = find_valid_upper(lo, hi, N, L)

    best = None
    if lo_valid.q != 0:
        best = evaluate_fraction(lo_valid, t_alpha, L)

    if hi_valid.q != 0:
        cand = evaluate_fraction(hi_valid, t_alpha, L)
        if best is None:
            best = cand
        elif cand is not None:
            eps = 1e-15
            if cand['diff'] + eps < best['diff']:
                best = cand
            elif abs(cand['diff'] - best['diff']) <= eps:
                if cand['area'] > best['area']:
                    best = cand

    return best

def compute_f(alpha_deg, L):
    kPi = math.acos(-1.0)
    kUMin = 1.0 + math.sqrt(2.0)
    kTMax = 0.75

    alpha_rad = alpha_deg * kPi / 180.0
    t_alpha = math.tan(alpha_rad)

    u_low = 1.0
    u_high = kUMin
    if t_alpha < kTMax:
        low = 1.0
        high = kUMin
        for _ in range(100):
            mid = 0.5 * (low + high)
            if tan_theta_from_u(mid) < t_alpha:
                low = mid
            else:
                high = mid
        u_low = 0.5 * (low + high)

        low = kUMin
        high = max(kUMin + 1.0, 3.0 / t_alpha + 2.0)
        while tan_theta_from_u(high) > t_alpha:
            high *= 2.0
        for _ in range(100):
            mid = 0.5 * (low + high)
            if tan_theta_from_u(mid) > t_alpha:
                low = mid
            else:
                high = mid
        u_high = 0.5 * (low + high)

    best = best_candidate_for_u(u_low, t_alpha, L)
    alt = best_candidate_for_u(u_high, t_alpha, L)

    if best is None:
        best = alt
    elif alt is not None:
        eps = 1e-15
        if alt['diff'] + eps < best['diff']:
            best = alt
        elif abs(alt['diff'] - best['diff']) <= eps:
            if alt['area'] > best['area']:
                best = alt

    return best['sum'] if best else 0

def solve():
    N = 45000
    L = 10000000000
    
    total = 0
    for i in range(1, N + 1):
        alpha = i ** (1/3)
        total += compute_f(alpha, L)
        
    return str(total)

if __name__ == "__main__":
    print(solve())
