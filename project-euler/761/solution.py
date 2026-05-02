import math

def clamp(x, lo, hi):
    if x < lo: return lo
    if x > hi: return hi
    return x

def lambda_regular(n):
    theta = math.pi / n
    tan_theta = math.tan(theta)
    
    K = -1
    for k in range(n + 1):
        ktheta = k * theta
        val = math.sin(ktheta) - (k + n) * tan_theta * math.cos(ktheta)
        if val < 0.0:
            K = k
        else:
            break
            
    if K < 0:
        K = 0
        
    ktheta = K * theta
    denom = (K + n) * tan_theta
    arg = 2.0 * math.sin(ktheta) / denom - math.cos(ktheta)
    arg = clamp(arg, -1.0, 1.0)
    
    alpha = 0.5 * (ktheta + math.acos(arg))
    return 1.0 / math.cos(alpha)

def solve():
    hexagon = lambda_regular(6)
    return f"{hexagon:.8f}"

if __name__ == "__main__":
    print(solve())
