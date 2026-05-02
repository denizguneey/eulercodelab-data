import math

kLast = 1000000000

def sieve_is_prime(n):
    is_prime = bytearray([1] * (n + 1))
    if n >= 0: is_prime[0] = 0
    if n >= 1: is_prime[1] = 0
    
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for m in range(p * p, n + 1, p):
                is_prime[m] = 0
        p += 1
    return is_prime

best_log_value = -1e300
best_mod_value = 0
best_L = 0

def evaluate_L(M, is_prime, L, fac):
    global best_log_value, best_mod_value, best_L
    
    divisors = [1]
    for p, e in fac:
        cur_len = len(divisors)
        pe = 1
        for i in range(1, e + 1):
            pe *= p
            for j in range(cur_len):
                divisors.append(divisors[j] * pe)
                
    v2 = 0
    for q, e in fac:
        if q == 2:
            v2 = e
            break
            
    exp2 = 1 if v2 == 0 else v2 + 2
    
    logN = exp2 * math.log(2.0)
    modN = pow(2, exp2, kLast)
    
    for d in divisors:
        p = d + 1
        if p == 2: continue
        if p > M + 1: continue
        if not is_prime[p]: continue
        
        exp = 1
        for q, e in fac:
            if q == p:
                exp = e + 1
                break
                
        logN += exp * math.log(p)
        modN = (modN * pow(p, exp, kLast)) % kLast
        
    if logN > best_log_value:
        best_log_value = logN
        best_mod_value = modN
        best_L = L

def dfs_generate(primes, M, is_prime, idx, max_exp, cur, fac):
    evaluate_L(M, is_prime, cur, fac)
    if idx >= len(primes):
        return
        
    p = primes[idx]
    val = cur
    for e in range(1, max_exp + 1):
        if val > M // p:
            break
        val *= p
        fac.append((p, e))
        dfs_generate(primes, M, is_prime, idx + 1, e, val, fac)
        fac.pop()

def solve_last9(bound_minus_1):
    global best_log_value, best_mod_value, best_L
    best_log_value = -1e300
    best_mod_value = 0
    best_L = 0
    
    M = bound_minus_1
    is_prime = sieve_is_prime(M + 1)
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
    
    fac = []
    dfs_generate(primes, M, is_prime, 0, 60, 1, fac)
    
    return (best_mod_value + 1) % kLast

def solve():
    last9 = solve_last9(20000000 - 1)
    return f"{last9:09d}"

if __name__ == '__main__':
    print(solve())
