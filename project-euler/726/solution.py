def solve():
    kMod = 1000000033
    limit = 10000
    
    f = [0] * (limit + 1)
    f[0] = 1
    
    prefix_a = 1
    power_part = 1
    factorial_tri = 1
    pow2 = 1
    tri = 0
    
    answer = 0
    for n in range(1, limit + 1):
        pow2 = (pow2 * 2) % kMod
        numer = (pow2 - 1) % kMod
        denom_inv = pow(2 * n - 1, kMod - 2, kMod)
        a_n = (numer * denom_inv) % kMod
        
        prefix_a = (prefix_a * a_n) % kMod
        power_part = (power_part * prefix_a) % kMod
        
        for i in range(n):
            tri += 1
            factorial_tri = (factorial_tri * tri) % kMod
            
        f[n] = (factorial_tri * power_part) % kMod
        answer = (answer + f[n]) % kMod
        
    return str(answer)

if __name__ == "__main__":
    print(solve())
