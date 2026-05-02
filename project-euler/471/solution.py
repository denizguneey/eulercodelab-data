import sys
import math
from decimal import Decimal, getcontext

# Set sufficient precision for asymptotic expansion
getcontext().prec = 60

def harmonic_asymptotic(n_val):
    if n_val == 0:
        return Decimal(0)
    
    # H_n = log(n) + gamma + 1/(2n) - 1/(12n^2) + 1/(120n^4) - 1/(252n^6) ...
    euler_gamma = Decimal('0.57721566490153286060651209008240243104215933593992')
    
    x = Decimal(n_val)
    inv = Decimal(1) / x
    inv2 = inv * inv
    inv4 = inv2 * inv2
    inv6 = inv4 * inv2
    inv8 = inv4 * inv4
    inv10 = inv8 * inv2
    
    log_x = Decimal(math.log(n_val))
    # Python decimal ln is .ln()
    log_x = x.ln()

    res = log_x + euler_gamma + inv / Decimal(2) \
          - inv2 / Decimal(12) + inv4 / Decimal(120) \
          - inv6 / Decimal(252) + inv8 / Decimal(240) \
          - Decimal(5) * inv10 / Decimal(660)
          
    return res

def harmonic_range(left, right):
    if left > right:
        return Decimal(0)
    
    kDirectHarmonicLimit = 5_000_000
    width = right - left + 1
    
    if right <= kDirectHarmonicLimit or width <= kDirectHarmonicLimit:
        total = Decimal(0)
        for k in range(left, right + 1):
            total += Decimal(1) / Decimal(k)
        return total
    
    return harmonic_asymptotic(right) - harmonic_asymptotic(left - 1)

def compute_g_fast(n):
    if n < 3:
        return Decimal(0)
        
    q = n // 2
    m = (n - 1) // 2
    left = n - m
    right = n - 1
    
    qd = Decimal(q)
    md = Decimal(m)
    nd = Decimal(n)
    ld = Decimal(left)
    rd = Decimal(right)
    
    part_low = qd * (Decimal(2) * qd * qd + Decimal(3) * qd - Decimal(5)) / Decimal(36)
    part_high_poly = md * (md + Decimal(1)) * (md + Decimal(2)) / Decimal(6)
    
    harmonic = harmonic_range(left, right)
    
    acoef = nd * (Decimal(2) * nd + Decimal(1)) * (nd + Decimal(1))
    bcoef = -(Decimal(6) * nd * nd + Decimal(6) * nd + Decimal(1))
    ccoef = Decimal(6) * nd + Decimal(3)
    
    sum_k = (ld + rd) * md / Decimal(2)
    sum_k2 = (rd * (rd + Decimal(1)) * (Decimal(2) * rd + Decimal(1)) -
             (ld - Decimal(1)) * ld * (Decimal(2) * ld - Decimal(1))) / Decimal(6)
             
    rational_tail = acoef * harmonic + bcoef * md + ccoef * sum_k - Decimal(2) * sum_k2
    
    return part_low + part_high_poly - rational_tail / Decimal(6)

def to_scientific_10_significant(value):
    if value == Decimal(0):
        return "0.000000000e0"
        
    negative = value < 0
    x = -value if negative else value
    
    exponent = int(math.floor(math.log10(float(x))))
    mantissa = x / (Decimal(10) ** exponent)
    
    # Scale exactly like C++: floor(mantissa * 10^9 + 0.5)
    scaled = math.floor(float(mantissa) * 1_000_000_000.0 + 0.5)
    if scaled >= 10_000_000_000:
        scaled //= 10
        exponent += 1
        
    lead = scaled // 1_000_000_000
    frac = scaled % 1_000_000_000
    
    sign_str = "-" if negative else ""
    return f"{sign_str}{lead}.{frac:09d}e{exponent}"

def solve():
    n = 100_000_000_000
    ans = compute_g_fast(n)
    return to_scientific_10_significant(ans)

if __name__ == '__main__':
    print(solve())
