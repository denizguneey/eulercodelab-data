import math

def central_ratio_asymptotic(n):
    nn = float(n)
    inv = 1.0 / nn
    corr = 1.0 - inv / 8.0 + (inv * inv) / 128.0 + (5.0 * inv * inv * inv) / 1024.0 - (21.0 * inv * inv * inv * inv) / 32768.0
    return corr / math.sqrt(math.pi * nn)

def g_from_threshold(threshold):
    approx = int(math.floor(1.0 / (math.pi * threshold * threshold)))
    
    if approx < 100000:
        n = 0
        r = 1.0
        while r > threshold:
            n += 1
            r *= (2.0 * n - 1.0) / (2.0 * n)
        return n
        
    n = max(1, approx)
    r = central_ratio_asymptotic(n)
    
    while n > 1 and r <= threshold:
        r *= (2.0 * n) / (2.0 * n - 1.0)
        n -= 1
        
    while r > threshold:
        n += 1
        r *= (2.0 * n - 1.0) / (2.0 * n)
        
    return n

def solve():
    threshold = 1.0 / 19999.0
    ans = g_from_threshold(threshold)
    return str(ans)

if __name__ == "__main__":
    print(solve())
