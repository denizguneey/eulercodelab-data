import math

def integrand_value(days, x):
    if x <= 0.0: return 0.0
    if x >= 1.0: return 1.0
    
    disc = math.sqrt((1.0 - x) * (1.0 + 3.0 * x))
    lambda1 = (1.0 - x + disc) * 0.5
    lambda2 = (1.0 - x - disc) * 0.5
    
    one_minus_lambda1_pow = 1.0
    if lambda1 > 0.0:
        log_term = days * math.log(lambda1)
        if log_term > -1e-4:
            one_minus_lambda1_pow = -math.expm1(log_term)
        else:
            one_minus_lambda1_pow = 1.0 - math.exp(log_term)
            
    lambda2_pow = math.pow(lambda2, days) if isinstance(days, int) else lambda2 ** days
    numerator = one_minus_lambda1_pow - lambda2_pow
    return numerator / x

def simpson_integral(days, intervals):
    h = 1.0 / intervals
    
    sum_val = integrand_value(days, 0.0) + integrand_value(days, 1.0)
    for i in range(1, intervals):
        x = i * h
        weight = 4 if (i % 2) != 0 else 2
        sum_val += weight * integrand_value(days, x)
        
    return days * h * sum_val / 3.0

def compute_expectation(days, initial_intervals, max_intervals, relative_tolerance):
    intervals = initial_intervals
    previous = simpson_integral(days, intervals)
    
    while intervals < max_intervals:
        intervals *= 2
        current = simpson_integral(days, intervals)
        delta = abs(current - previous)
        scale = max(1.0, abs(current))
        if delta <= relative_tolerance * scale:
            return current
        previous = current
        
    return previous

def solve():
    ans = compute_expectation(10000, 4096, 1048576, 1e-12)
    return "{:.4f}".format(ans)

if __name__ == '__main__':
    print(solve())
