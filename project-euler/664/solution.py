import math
from decimal import Decimal, getcontext

getcontext().prec = 50

kLogPhi = Decimal('1.61803398874989484820458683436563811772030917980576').ln()
kTailDrop = Decimal('120.0')

def log_term(n, d):
    dn = Decimal(n)
    dd = Decimal(d)
    return dn * dd.ln() - dd * kLogPhi

def build_window(n):
    approx = int(Decimal(n) / kLogPhi)
    if approx == 0:
        approx = 1

    scan_lo = max(1, approx - 6)
    scan_hi = approx + 6

    peak = scan_lo
    peak_log_term = log_term(n, peak)

    for d in range(scan_lo + 1, scan_hi + 1):
        val = log_term(n, d)
        if val > peak_log_term:
            peak_log_term = val
            peak = d

    left = peak
    while left > 1:
        next_val = log_term(n, left - 1)
        if (peak_log_term - next_val) > kTailDrop:
            break
        left -= 1

    right = peak
    while True:
        next_val = log_term(n, right + 1)
        if (peak_log_term - next_val) > kTailDrop:
            break
        right += 1

    return left, right, peak_log_term

def compute_f(n):
    if n == 0: return 4
    if n == 1: return 6
    left, right, peak_log_term = build_window(n)

    scaled_sum = Decimal('0')
    for d in range(left, right + 1):
        diff = log_term(n, d) - peak_log_term
        scaled_sum += diff.exp()

    log_series = peak_log_term + scaled_sum.ln()
    raw = log_series / kLogPhi

    # Using Python's math.ceil on float conversion for raw
    # Since 50 precision is used, converting to float and taking ceil matches C++ logic
    val = float(raw)
    return int(math.ceil(val - 1e-15)) + 3

def solve():
    ans = compute_f(1234567)
    return str(ans)

if __name__ == '__main__':
    print(solve())
