import math

def compute_totients(n_max):
    phi = list(range(n_max + 1))
    for p in range(2, n_max + 1):
        if phi[p] == p:
            for multiple in range(p, n_max + 1, p):
                phi[multiple] -= phi[multiple] // p
    return phi

def central_binomial(n):
    return math.comb(2 * n, n)

def compute_n_upper_bound(limit):
    n = 1
    best = 0
    while True:
        bound = central_binomial(n) // (2 * n)
        if bound > limit:
            break
        best = n
        n += 1
    return best

def compute_m_upper_bound(limit):
    factorial = 1
    best = 1
    m = 2
    while True:
        if factorial > limit:
            break
        best = m
        factorial *= m
        m += 1
    return best

def f_value(m, n, phi, fact, fact_powers):
    total = m * n
    sum_val = 0
    
    for l in range(1, n + 1):
        if n % l != 0:
            continue
            
        slice_len = n // l
        numerator = fact[total // l]
        denominator = fact_powers[slice_len][m]
        multinomial = numerator // denominator
        
        sum_val += phi[l] * multinomial
        
    return sum_val // total

def solve(limit=1000000000000000):
    n_upper = compute_n_upper_bound(limit)
    m_upper = compute_m_upper_bound(limit)
    
    max_factorial_needed = m_upper * n_upper
    fact = [1] * (max_factorial_needed + 1)
    for i in range(1, max_factorial_needed + 1):
        fact[i] = fact[i - 1] * i
        
    phi = compute_totients(n_upper)
    
    fact_powers = [[1] * (m_upper + 1) for _ in range(n_upper + 1)]
    for n in range(n_upper + 1):
        fact_powers[n][0] = 1
        for m in range(1, m_upper + 1):
            fact_powers[n][m] = fact_powers[n][m - 1] * fact[n]
            
    answer = 0
    for m in range(2, m_upper + 1):
        for n in range(1, n_upper + 1):
            val = f_value(m, n, phi, fact, fact_powers)
            if val <= limit:
                answer += val
                
    return str(answer)

if __name__ == '__main__':
    print(solve())
