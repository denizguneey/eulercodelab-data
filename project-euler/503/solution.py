import math

def solve_expected_score(n):
    next_value = (float(n) + 1.0) / 2.0
    for t in range(n - 1, 0, -1):
        slope = (float(n) + 1.0) / (float(t) + 1.0)
        cutoff = next_value / slope
        k = int(math.floor(cutoff + 1e-15))
        if k < 0: k = 0
        if k > t: k = t
        
        sum_ranks = float(k) * (k + 1.0) / 2.0
        stop_expectation = slope * sum_ranks
        continue_expectation = float(t - k) * next_value
        next_value = (stop_expectation + continue_expectation) / float(t)
        
    return next_value

def solve():
    ans = solve_expected_score(1000000)
    return f"{ans:.10f}"

if __name__ == '__main__':
    print(solve())
