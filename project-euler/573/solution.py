import math

def compute_expected(n):
    if n <= 1:
        return 1.0
        
    c = math.pow((n - 1) / n, n - 1)
    total = 1.0 + c
    
    for k in range(1, n - 1):
        m = n - k
        log_r = k * math.log1p(1.0 / k) + (m - 1) * math.log1p(-1.0 / m)
        c *= math.exp(log_r)
        total += c
        
    return total

def solve():
    ans = compute_expected(1000000)
    return f"{ans:.4f}"

if __name__ == '__main__':
    print(solve())
