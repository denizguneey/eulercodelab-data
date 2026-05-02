MOD = 1008691207

def f_formula(n):
    if n <= 2: return 0
    fact = 1
    sum_fact = 1 if n >= 4 else 0
    
    upto = n - 4
    for i in range(1, upto + 1):
        fact = (fact * i) % MOD
        sum_fact = (sum_fact + fact) % MOD
        
    fn3 = 1 if n == 3 else 0
    fn2 = 0
    fn1 = 0
    fn = 0
    
    start = max(1, upto + 1)
    for i in range(start, n + 1):
        fact = (fact * i) % MOD
        if i == n - 3: fn3 = fact
        if i == n - 2: fn2 = fact
        if i == n - 1: fn1 = fact
        if i == n: fn = fact
        
    res = fn
    res = (res - 2 * fn1) % MOD
    res = (res - fn2) % MOD
    res = (res - fn3) % MOD
    res = (res + 2) % MOD
    res = (res + (n - 3) * sum_fact) % MOD
    
    if res < 0: res += MOD
    
    return res

def solve():
    return str(f_formula(100000000))

if __name__ == '__main__':
    print(solve())
