import math

def sieve_primes(n):
    if n < 2: return []
    is_prime = bytearray(n + 1)
    for i in range(2, n + 1):
        is_prime[i] = 1
    for i in range(2, math.isqrt(n) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = 0
    return [i for i in range(2, n + 1) if is_prime[i]]

def max_prime_power_leq_n(n, prime):
    val = prime
    while val <= n // prime:
        val *= prime
    return val

def highest_power_with_limit(prime, limit):
    if limit < prime: return 0
    val = prime
    while val <= limit // prime:
        val *= prime
    return val

def hungarian_max_weight_bipartite(left_size, right_size, weights):
    if left_size == 0 or right_size == 0: return 0
    
    n = left_size
    m = right_size
    
    INF = 10**18
    u = [0] * (n + 1)
    v = [0] * (m + 1)
    p = [0] * (m + 1)
    way = [0] * (m + 1)
    
    for i in range(1, n + 1):
        p[0] = i
        j0 = 0
        minv = [INF] * (m + 1)
        used = bytearray(m + 1)
        
        while True:
            used[j0] = 1
            i0 = p[j0]
            delta = INF
            j1 = 0
            
            for j in range(1, m + 1):
                if not used[j]:
                    cost = -weights[(i0 - 1) * m + (j - 1)]
                    cur = cost - u[i0] - v[j]
                    if cur < minv[j]:
                        minv[j] = cur
                        way[j] = j0
                    if minv[j] < delta:
                        delta = minv[j]
                        j1 = j
                        
            for j in range(m + 1):
                if used[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                else:
                    minv[j] -= delta
                    
            j0 = j1
            if p[j0] == 0:
                break
                
        while True:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1
            if j0 == 0:
                break
                
    min_cost = 0
    for j in range(1, m + 1):
        if p[j] != 0:
            min_cost += -weights[(p[j] - 1) * m + (j - 1)]
            
    return -min_cost

def solve_n(n):
    all_primes = sieve_primes(n)
    
    max_prime_powers = []
    baseline_sum = 1
    for p in all_primes:
        power = max_prime_power_leq_n(n, p)
        max_prime_powers.append(power)
        baseline_sum += power
        
    split = math.isqrt(n)
    small_primes = []
    small_prime_powers = []
    large_primes = []
    large_prime_powers = []
    
    for i in range(len(all_primes)):
        p = all_primes[i]
        power = max_prime_powers[i]
        if p <= split:
            small_primes.append(p)
            small_prime_powers.append(power)
        else:
            large_primes.append(p)
            large_prime_powers.append(power)
            
    left_size = len(small_primes)
    large_size = len(large_primes)
    right_size = large_size + left_size
    
    weights = [0] * (left_size * right_size)
    
    for si in range(left_size):
        p = small_primes[si]
        p_power = small_prime_powers[si]
        for li in range(large_size):
            q = large_primes[li]
            q_power = large_prime_powers[li]
            if p * q > n:
                break
                
            best_p_factor = highest_power_with_limit(p, n // q)
            if best_p_factor == 0:
                continue
                
            pair_value = best_p_factor * q
            if pair_value <= p_power + q_power:
                continue
                
            gain = pair_value - p_power - q_power
            idx = si * right_size + li
            weights[idx] = max(weights[idx], gain)
            
    max_gain = hungarian_max_weight_bipartite(left_size, right_size, weights)
    return baseline_sum + max_gain

def solve():
    n = 200000
    ans = solve_n(n)
    return str(ans)

if __name__ == '__main__':
    print(solve())
