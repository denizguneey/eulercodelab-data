import concurrent.futures

MOD = 10**9 + 7

def power(b, e):
    return pow(b, e, MOD)

def get_stable(k, n):
    s = 1 << k
    if n == s:
        return 1
    t1 = (n - s + 2) % MOD
    exp = n - s - 1
    return (t1 * power(2, exp)) % MOD

def solve_bit(k, n):
    s = 1 << k
    if n < s:
        return 0
    es = 1 << (k + 1)
    if n < es:
        return get_stable(k, n)
    
    dp = [0] * (n + 1)
    for i in range(s, es):
        dp[i] = get_stable(k, i)
        
    c_sum = 0
    ub = 1 << k
    if ub > 2:
        for i in range(es - 2, es - ub, -1):
            c_sum = (c_sum + dp[i]) % MOD
            
    for i in range(es, n + 1):
        t1 = (3 * dp[i - 1]) % MOD
        t3 = (4 * dp[i - ub]) % MOD
        t4 = (4 * dp[i - ub - 1]) % MOD
        val = (t1 - c_sum - t3 + t4) % MOD
        dp[i] = (val + 2 * MOD) % MOD
        
        if ub > 2:
            c_sum = (c_sum + dp[i - 1]) % MOD
            c_sum = (c_sum - dp[i - ub + 1] + MOD) % MOD
            
    return dp[n]

def process_k(args):
    k, n = args
    return k, solve_bit(k, n)

def solve_X(n):
    tot = 0
    if n % 2 != 0:
        tot = (power(2, n - 1) - 1 + MOD) % MOD
        
    tasks = []
    for k in range(1, 20):
        if (1 << k) > n:
            break
        tasks.append((k, n))
        
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = dict(executor.map(process_k, tasks))
        
    for k, n_k in tasks:
        val = results[k]
        term = (val * power(2, k)) % MOD
        tot = (tot + term) % MOD
        
    return tot

def run_checkpoints():
    assert solve_X(2) == 2
    assert solve_X(4) == 14
    assert solve_X(10) == 1418

def solve():
    return str(solve_X(10000))

if __name__ == "__main__":
    run_checkpoints()
    print(solve())
