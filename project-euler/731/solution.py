def solve():
    kBase = 10000000000
    n = 10000000000000000
    n_plus_9 = n + 9
    
    p3 = [1]
    while p3[-1] <= n_plus_9 // 3:
        p3.append(p3[-1] * 3)
        
    limit = 0
    for i in range(1, len(p3)):
        if p3[i] <= n_plus_9:
            limit = i
            
    if limit == 0:
        return "0000000000"
        
    sum_q_mod = 0
    remainders = [0] * (limit + 1)
    
    for i in range(1, limit + 1):
        d = p3[i]
        m = n_plus_9 - d
        
        modulus = d * kBase
        s = pow(10, m, modulus)
        
        q = s // d
        r = s % d
        q_mod = q % kBase
        
        sum_q_mod = (sum_q_mod + q_mod) % kBase
        remainders[i] = r
        
    denom = p3[limit]
    numer = 0
    for i in range(1, limit + 1):
        scale = p3[limit - i]
        numer += remainders[i] * scale
        
    carry = numer // denom
    answer = (sum_q_mod + carry) % kBase
    
    return str(answer).zfill(10)

if __name__ == "__main__":
    print(solve())
