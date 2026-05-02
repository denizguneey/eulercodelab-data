import math
from decimal import Decimal, getcontext

def solve():
    getcontext().prec = 100
    # K = pi / (3 * 2^19)
    pi = Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')
    K = pi / Decimal(3 * (2**19))
    
    K2 = K * K
    K3 = K2 * K
    K4 = K3 * K
    K5 = K4 * K
    sinK = K - K3/6 + K5/120
    cosK = Decimal(1) - K2/2 + K4/24
    sqrt3 = Decimal(3).sqrt()
    
    # We want minimal a such that C < pi/3 + K
    # cos(C) > cos(pi/3 + K)
    # 1/2 - (2a+1)/(2a^2) > cos(pi/3 + K)
    # (2a+1)/(2a^2) < 1/2 - cos(pi/3 + K) = V
    
    cos_pi3_plus_K = Decimal('0.5')*cosK - (sqrt3/Decimal(2))*sinK
    V = Decimal('0.5') - cos_pi3_plus_K
    
    a_exact = (Decimal(1) + (Decimal(1) + Decimal(2)*V).sqrt()) / (Decimal(2)*V)
    a = int(math.floor(a_exact)) + 1
    
    # Perimeter is 3a + 1
    return 3 * a + 1

if __name__ == "__main__":
    print(solve())
