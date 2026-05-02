import math

def digamma(x):
    if x <= 0.0 or not math.isfinite(x):
        return float('nan')
        
    res = 0.0
    while x < 10.0:
        res -= 1.0 / x
        x += 1.0
        
    inv = 1.0 / x
    inv2 = inv * inv
    
    series = inv2 * (-1.0 / 12.0
             + inv2 * (1.0 / 120.0
             + inv2 * (-1.0 / 252.0
             + inv2 * (1.0 / 240.0
             + inv2 * (-1.0 / 132.0
             + inv2 * (691.0 / 32760.0))))))
             
    res += math.log(x) - 0.5 * inv + series
    return res

def solve():
    N = 100000000000000
    sqrt3 = math.sqrt(3.0)
    c = (3.0 + sqrt3) / 6.0
    
    K = 60
    num = [0] * (K + 1)
    den = [0] * (K + 1)
    
    num[2] = 7
    num[3] = 35
    num[4] = 121
    
    den[2] = 11
    den[3] = 73
    den[4] = 395
    den[5] = 1933
    
    for n in range(5, K + 1):
        num[n] = 3 * num[n - 1] + 3 * num[n - 2] - num[n - 3]
    for n in range(6, K + 1):
        den[n] = 8 * den[n - 1] - 18 * den[n - 2] + 8 * den[n - 3] - den[n - 4]
        
    E = 0.0
    for n in range(2, K + 1):
        s = float(num[n]) / float(den[n])
        E += s - 1.0 / (float(n) - c)
        
    x_big = float(N) + 1.0 - c
    x_small = 2.0 - c
    
    ans = digamma(x_big) - digamma(x_small) + E
    return "{:.8f}".format(ans)

if __name__ == "__main__":
    print(solve())
