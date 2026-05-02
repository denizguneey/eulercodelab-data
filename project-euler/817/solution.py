import math

kP = 1000000007

def M_for_target_digit(d, exp_leg, exp_sqrt, p2):
    a = kP - d
    leg = pow(a, exp_leg, kP)
    
    if leg == 1:
        r = pow(a, exp_sqrt, kP)
        return min(r, kP - r)
        
    L = p2 - d * kP
    width = kP
    
    while True:
        m = math.isqrt(L)
        if m * m < L:
            m += 1
            
        sq = m * m
        if sq <= L + width - 1:
            return m
            
        L += p2

def solve():
    exp_leg = (kP - 1) // 2
    exp_sqrt = (kP + 1) // 4
    p2 = kP * kP
    
    total = 0
    for d in range(1, 100001):
        total += M_for_target_digit(d, exp_leg, exp_sqrt, p2)
        
    return str(total)

if __name__ == "__main__":
    print(solve())
