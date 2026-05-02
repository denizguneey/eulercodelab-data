import math

def f_exact_small(n, p):
    q = 1.0 - p
    tv = math.pow(q, n)
    te = math.pow(p, n)
    
    total = 0.0
    for m in range(n):
        weight = float(n + 1 - m)
        total += weight * (tv + te)
        
        mult = float(n + m) / float(m + 1)
        tv *= mult * p
        te *= mult * q
        
    return total / float(2 * n + 1)

def f_large_drift(n, p):
    q = 1.0 - p
    dominant = p if p > q else q
    
    two_n_plus_one = float(2 * n + 1)
    expected_questions = float(n) / dominant
    return (two_n_plus_one - expected_questions) / two_n_plus_one

def f(n, p):
    q = 1.0 - p
    drift_score = abs(1.0 - 2.0 * p) * math.sqrt(float(n) / (p * q))
    
    if n <= 2000 or drift_score < 15.0:
        return f_exact_small(n, p)
    return f_large_drift(n, p)

def solve():
    ans = f(100000000000, 0.4999)
    return format(ans, ".10f")

if __name__ == "__main__":
    print(solve())
