import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

def solve(sequence="UDDDUdddDDUDDddDdDddDDUDDdUUDd", lower_bound=1000000000000000):
    A = 1
    B = 0
    C = 1

    for step in reversed(sequence):
        if step == 'D':
            A = 3 * A
            B = 3 * B
        elif step == 'U':
            A = 3 * A
            B = 3 * B - 2 * C
            C = 4 * C
        elif step == 'd':
            A = 3 * A
            B = 3 * B + C
            C = 2 * C
            
    g = gcd(A, C)
    mod = C // g
    a_reduced = A // g
    
    a_mod = a_reduced % mod
    try:
        inv = pow(a_mod, -1, mod)
    except ValueError:
        return -1
        
    B_reduced = B // g
    rhs = (-B_reduced) % mod
    t0 = (rhs * inv) % mod
    
    n0 = (A * t0 + B) // C
    n_step = A // g
    t_step = mod
    
    k = 0
    if n0 <= lower_bound:
        k = (lower_bound - n0) // n_step + 1
        
    t_min = t0 + k * t_step
    if t_min <= 0:
        add = (-t_min) // t_step + 1
        k += add
        
    t = t0 + k * t_step
    return str((A * t + B) // C)

if __name__ == '__main__':
    print(solve())
