def series_sum(n, r):
    total = 0.0
    power = 1.0
    for k in range(1, n + 1):
        total += (900.0 - 3.0 * k) * power
        power *= r
    return total

def solve(n=5000, target=-600000000000.0):
    lo = 1.0
    hi = 1.2
    
    for _ in range(200):
        mid = (lo + hi) / 2.0
        s = series_sum(n, mid)
        if s > target:
            lo = mid
        else:
            hi = mid
            
    ans = (lo + hi) / 2.0
    return f"{ans:.12f}"

if __name__ == '__main__':
    print(solve())
