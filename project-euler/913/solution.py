import math
from collections import defaultdict

def sieve_primes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[p]:
            for q in range(p * p, limit + 1, p):
                is_prime[q] = False
    return [i for i, prime in enumerate(is_prime) if prime]

def factorize(n, primes):
    factors = []
    for p in primes:
        if p * p > n:
            break
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            factors.append((p, e))
    if n > 1:
        factors.append((n, 1))
    return factors

def add_factorization(acc, n, primes):
    if n <= 1:
        return
    for p, e in factorize(n, primes):
        acc[p] += e

def order_prime_power(base, p, k, primes, factor_cache):
    mod = p ** k
    phi = (p ** (k - 1)) * (p - 1)
    
    if p - 1 not in factor_cache:
        factor_cache[p - 1] = dict(factorize(p - 1, primes))
    fac = dict(factor_cache[p - 1])
    
    if k > 1:
        fac[p] = fac.get(p, 0) + k - 1
        
    ord_val = phi
    for q, e in fac.items():
        for _ in range(e):
            if ord_val % q != 0:
                break
            cand = ord_val // q
            if pow(base, cand, mod) == 1:
                ord_val = cand
            else:
                break
    return ord_val

def swaps_fourth_power_dims(n, m, primes, factor_cache, t_factor_cache):
    uu = n * m
    N = uu ** 4
    g = m ** 4
    
    if uu not in t_factor_cache:
        acc = defaultdict(int)
        add_factorization(acc, uu - 1, primes)
        add_factorization(acc, uu + 1, primes)
        add_factorization(acc, uu * uu + 1, primes)
        t_factor_cache[uu] = acc
    factors = t_factor_cache[uu].items()
    
    data = []
    for p, e in factors:
        phi = [1] * (e + 1)
        ord_arr = [1] * (e + 1)
        for k in range(1, e + 1):
            phi[k] = (p ** (k - 1)) * (p - 1)
            ord_arr[k] = order_prime_power(g, p, k, primes, factor_cache)
        data.append({'exp': e, 'phi': phi, 'ord': ord_arr})
        
    cycles_mod_set = [0]
    
    def dfs(idx, phi_cur, ord_cur):
        if idx == len(data):
            cycles_mod_set[0] += phi_cur // ord_cur
            return
        pd = data[idx]
        for k in range(pd['exp'] + 1):
            phi_next = phi_cur * pd['phi'][k]
            ord_next = math.lcm(ord_cur, pd['ord'][k])
            dfs(idx + 1, phi_next, ord_next)
            
    dfs(0, 1, 1)
    return N - 1 - cycles_mod_set[0]

def solve():
    primes = sieve_primes(100000)
    factor_cache = {}
    t_factor_cache = {}
    
    ans = 0
    for n in range(2, 101):
        for m in range(n, 101):
            ans += swaps_fourth_power_dims(n, m, primes, factor_cache, t_factor_cache)
            
    return str(ans)

if __name__ == "__main__":
    print(solve())
