import math

MOD = 282475249

def floor_div_phi(n):
    if n == 0:
        return 0
    radicand = 5 * n * n
    floor_n_sqrt5 = math.isqrt(radicand)
    return (floor_n_sqrt5 - n) // 2

def triangular_mod(n, mod_val, inv2):
    return (n % mod_val) * ((n + 1) % mod_val) % mod_val * inv2 % mod_val

def square_sum_mod(n, mod_val, inv6):
    a = n % mod_val
    b = (n + 1) % mod_val
    c = (2 * (n % mod_val) + 1) % mod_val
    return a * b % mod_val * c % mod_val * inv6 % mod_val

def beatty_sums_mod(n, mod_val, inv2, inv6):
    if n == 0:
        return (0, 0, 0)
        
    m = floor_div_phi(n)
    child_g, child_p, child_q = beatty_sums_mod(m, mod_val, inv2, inv6)
    
    n_mod = n % mod_val
    m_mod = m % mod_val
    tri_m = triangular_mod(m, mod_val, inv2)
    sq_m = square_sum_mod(m, mod_val, inv6)
    
    g = (n_mod * m_mod - tri_m - child_g) % mod_val
    
    q = (n_mod * m_mod * m_mod - 2 * sq_m - 2 * child_p + tri_m + child_g) % mod_val
    
    first = n_mod * m_mod % mod_val * ((n + 1) % mod_val) % mod_val * inv2 % mod_val
    numerator = (sq_m + 2 * child_p + child_q + tri_m + child_g) % mod_val
    second = numerator * inv2 % mod_val
    p = (first - second) % mod_val
    
    return ((g + mod_val) % mod_val, (p + mod_val) % mod_val, (q + mod_val) % mod_val)

def solve_mod(n, mod_val):
    inv2 = pow(2, -1, mod_val)
    inv6 = pow(6, -1, mod_val)
    
    cutoff = floor_div_phi(n + 1)
    sums_g, sums_p, sums_q = beatty_sums_mod(cutoff, mod_val, inv2, inv6)
    
    prefix_numerator = (4 * sums_p + sums_q + sums_g) % mod_val
    prefix = prefix_numerator * inv2 % mod_val
    
    if cutoff == n:
        return prefix
        
    n_mod = n % mod_val
    count_mod = (n - cutoff) % mod_val
    
    sum_x = (triangular_mod(n, mod_val, inv2) - triangular_mod(cutoff, mod_val, inv2)) % mod_val
    sum_x2 = (square_sum_mod(n, mod_val, inv6) - square_sum_mod(cutoff, mod_val, inv6)) % mod_val
    
    n2_plus_n = (n_mod * n_mod + n_mod) % mod_val
    coeff = (2 * n_mod - 1) % mod_val
    
    term1 = count_mod * n2_plus_n % mod_val
    term2 = coeff * sum_x % mod_val
    term3 = 3 * sum_x2 % mod_val
    
    tail_numerator = (term1 + term2 - term3) % mod_val
    tail = tail_numerator * inv2 % mod_val
    
    ans = (prefix + tail) % mod_val
    return (ans + mod_val) % mod_val

def solve():
    target_n = 10000000000000000
    mod_val = 282475249
    ans = solve_mod(target_n, mod_val)
    return str(ans)

if __name__ == '__main__':
    print(solve())
