import math

kPi = 3.141592653589793238462643383279502884

def harmonic_approx(n):
    n2 = n * n
    return math.log(n) + 0.5772156649 + 1.0 / (2.0 * n) - 1.0 / (12.0 * n2) + \
           1.0 / (120.0 * n2 * n2) - 1.0 / (252.0 * n2 * n2 * n2)

def tan_phi(n, hn):
    return math.sqrt(n / hn - 0.25) / (n + 0.5)

def atan_poly(x):
    x2 = x * x
    return x - x * x2 / 3.0 + x * x2 * x2 / 5.0

def integral_block(k, f_n, f_n_der2):
    return 2.0 * k * f_n + f_n_der2 * k * k * k / 3.0

def coins_needed_exact(loops):
    target = 2.0 * kPi * loops
    harmonic = 1.0
    radius = 1.0
    tan_gamma = 0.0
    accumulated = 0.0
    n = 1
    
    while accumulated <= target:
        r2 = radius * radius
        root = math.sqrt(4.0 - r2)
        tan_beta = root / radius
        tan_theta = (tan_beta - tan_gamma) / (1.0 + tan_beta * tan_gamma)
        accumulated += math.atan(tan_theta)
        
        nl = float(n)
        tan_gamma = (nl * radius * root) / (nl * r2 + 2.0)
        
        m = n + 1
        harmonic += 1.0 / m
        radius = math.sqrt(harmonic / m)
        n += 1
        
    return n

def coins_needed_approx(loops):
    total_angle = -0.16103076705762 / 180.0 * kPi
    n = 0
    harmonic = 0.0
    initial = 1000000
    k = 20000
    
    for i in range(initial):
        n += 1
        harmonic += 1.0 / n
        total_angle += atan_poly(tan_phi(n, harmonic))
        
    center = n + k + 1
    block_sum = 0.0
    stage1_target = loops * 2.0 * kPi - kPi / 2.0
    
    while total_angle < stage1_target:
        f_nm2k = atan_poly(tan_phi(center - 2 * k, harmonic_approx(center - 2.0 * k)))
        f_nmk = atan_poly(tan_phi(center - k, harmonic_approx(center - 1.0 * k)))
        f_n = atan_poly(tan_phi(center, harmonic_approx(center)))
        f_npk = atan_poly(tan_phi(center + k, harmonic_approx(center + 1.0 * k)))
        f_np2k = atan_poly(tan_phi(center + 2 * k, harmonic_approx(center + 2.0 * k)))
        
        f_n_der2 = (f_npk + f_nmk - 2.0 * f_n) / (k * k)
        f_npk_der = (-f_n + f_np2k) / (2.0 * k)
        f_nmk_der = (f_n - f_nm2k) / (2.0 * k)
        
        block_sum = integral_block(k, f_n, f_n_der2) + (f_nmk + f_npk) / 2.0 + (f_npk_der - f_nmk_der) / 12.0
        
        total_angle += block_sum
        center += 2 * k + 1
        
    center -= 2 * k + 1
    total_angle -= block_sum
    n = center - k
    harmonic = harmonic_approx(n)
    
    d_theta = math.atan(math.sqrt(4.0 * n / harmonic - 1.0))
    d_phi = atan_poly(tan_phi(n, harmonic))
    stage2_target = loops * 2.0 * kPi
    
    while total_angle + d_theta < stage2_target:
        total_angle += d_phi
        n += 1
        harmonic += 1.0 / n
        d_phi = atan_poly(tan_phi(n, harmonic))
        d_theta = math.atan(math.sqrt(4.0 * n / harmonic - 1.0))
        
    return n + 1

def solve():
    return str(coins_needed_approx(2020))

if __name__ == "__main__":
    print(solve())
