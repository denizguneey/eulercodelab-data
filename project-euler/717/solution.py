def g_value(p):
    e = pow(2, p, p - 1)
    r = pow(2, e, p)
    t = (r * ((p + 1) // 2)) % p
    
    mod = p * p
    two_p_mod = pow(2, p, mod)
    u = (t * two_p_mod) % mod
    
    if u < r:
        u += mod
    u -= r
    return u // p

def solve():
    n = 10000000
    is_prime = bytearray([1] * n)
    if n > 0: is_prime[0] = 0
    if n > 1: is_prime[1] = 0
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = 0
                
    total_sum = 0
    for p in range(3, n, 2):
        if is_prime[p]:
            total_sum += g_value(p)
            
    return str(total_sum)

if __name__ == "__main__":
    print(solve())
