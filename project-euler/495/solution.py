import multiprocessing
import collections

MOD = 1000000007

def power(base, exp):
    return pow(base, exp, MOD)

def modInverse(n):
    return power(n, MOD - 2)

factorial = [1] * 101
invFactorial = [1] * 101

def precomputeFactorials():
    for i in range(1, 101):
        factorial[i] = (factorial[i - 1] * i) % MOD
        invFactorial[i] = modInverse(factorial[i])

def generatePartitions(target, minVal, current, result):
    if target == 0:
        result.append(list(current))
        return
    for i in range(minVal, target + 1):
        current.append(i)
        generatePartitions(target - i, i, current, result)
        current.pop()

def getFactorialExponents(n):
    exponents = {}
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, n + 1):
        if is_prime[p]:
            for i in range(2 * p, n + 1, p):
                is_prime[i] = False
            count = 0
            p_pow = p
            while p_pow <= n:
                count += n // p_pow
                p_pow *= p
            exponents[p] = count
    return exponents

def worker(args):
    precomputeFactorials()
    start, end, partitions, prime_counts, max_exponent = args
    local_sum = 0
    dp = [0] * (max_exponent + 1)
    
    for i in range(start, end):
        p = partitions[i]
        
        part_counts = collections.Counter(p)
        term_coeff = 1
        
        for val in p:
            inv_val = modInverse(val)
            sign = 1 if ((val - 1) % 2 == 0) else -1
            term = (sign * inv_val) % MOD
            if term < 0: term += MOD
            term_coeff = (term_coeff * term) % MOD
            
        for val, count in part_counts.items():
            term_coeff = (term_coeff * invFactorial[count]) % MOD
            
        for i_dp in range(max_exponent + 1): dp[i_dp] = 0
        dp[0] = 1
        
        for val in p:
            for j in range(val, max_exponent + 1):
                dp[j] = (dp[j] + dp[j - val])
                if dp[j] >= MOD: dp[j] -= MOD
                
        S_lambda = 1
        for exp, freq in prime_counts.items():
            ways = dp[exp]
            if ways == 0:
                S_lambda = 0
                break
            S_lambda = (S_lambda * power(ways, freq)) % MOD
            
        total_term = (term_coeff * S_lambda) % MOD
        local_sum = (local_sum + total_term) % MOD
        
    return local_sum

def solveW(n_val, k_val, isFactorial):
    precomputeFactorials()
    prime_counts = collections.defaultdict(int)
    max_exponent = 0
    
    raw_exponents = getFactorialExponents(n_val)
        
    for prime, exp in raw_exponents.items():
        prime_counts[exp] += 1
        if exp > max_exponent:
            max_exponent = exp
            
    partitions = []
    generatePartitions(k_val, 1, [], partitions)
    
    num_threads = multiprocessing.cpu_count()
    if num_threads == 0: num_threads = 4
    
    part_count = len(partitions)
    chunk_size = (part_count + num_threads - 1) // num_threads
    
    tasks = []
    for t in range(num_threads):
        start = t * chunk_size
        end = min(start + chunk_size, part_count)
        if start < end:
            tasks.append((start, end, partitions, prime_counts, max_exponent))
            
    if num_threads == 1:
        total_W = worker(tasks[0])
    else:
        with multiprocessing.Pool(num_threads) as pool:
            results = pool.map(worker, tasks)
        total_W = sum(results) % MOD
        
    return total_W

def solve():
    return str(solveW(10000, 30, True))

if __name__ == '__main__':
    print(solve())
