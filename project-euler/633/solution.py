def solve():
    import math
    
    K = 7
    P_MAX = 10000000
    
    is_comp = [False] * (P_MAX // 2 + 1)
    primes = [2]
    
    for i in range(3, int(math.isqrt(P_MAX)) + 1, 2):
        if is_comp[i // 2]: continue
        for j in range(i * i, P_MAX + 1, i * 2):
            is_comp[j // 2] = True
            
    for i in range(3, P_MAX + 1, 2):
        if not is_comp[i // 2]:
            primes.append(i)
            
    c = [0.0] * (K + 1)
    c[0] = 1.0
    
    for p in primes:
        a = 1.0 / (float(p) * float(p))
        b = 1.0 - a
        for k in range(K, 0, -1):
            c[k] = c[k] * b + c[k - 1] * a
        c[0] *= b
        
    def fmt5(v):
        e = 0
        m = float(v)
        while m >= 10.0:
            m /= 10.0
            e += 1
        while m < 1.0:
            m *= 10.0
            e -= 1
            
        scale = 10000.0
        mr = math.floor(m * scale + 0.5) / scale
        if mr >= 10.0:
            mr /= 10.0
            e += 1
            
        return "{:.4f}e{}".format(mr, e)

    return fmt5(c[7])

if __name__ == '__main__':
    print(solve())
