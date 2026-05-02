def valuation_counts(n):
    count = [0] * 64
    for k in range(63):
        a = n >> k
        if a == 0: break
        b = n >> (k + 1)
        count[k] = a - b
    return count

def solve_n(n):
    mod = 1234567890
    count = valuation_counts(n)
    
    losing_mod = 0
    for i in range(64):
        if count[i] == 0: continue
        for j in range(64):
            if count[j] == 0: continue
            k = i ^ j
            if k >= 64 or count[k] == 0: continue
            
            term = (count[i] % mod) * (count[j] % mod) % mod
            term = (term * (count[k] % mod)) % mod
            losing_mod = (losing_mod + term) % mod
            
    n_mod = n % mod
    total_mod = (n_mod * n_mod % mod) * n_mod % mod
    
    return (total_mod + mod - losing_mod) % mod

def solve():
    return str(solve_n(123456787654321))

if __name__ == '__main__':
    print(solve())
