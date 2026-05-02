import multiprocessing

def mul_mod(a, b, mod):
    return (a * b) % mod

def mod_pow(base, exp, mod):
    return pow(base, exp, mod)

def mod_inv_prime(a, p):
    return pow(a, p - 2, p)

def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    x = y1
    y = x1 - y1 * (a // b)
    return g, x, y

def mod_inv_coprime(a, mod):
    g, x, y = egcd(a, mod)
    return (x % mod + mod) % mod

def mod_sqrt(n, p):
    if p == 2:
        return True, n % p
    n %= p
    if n == 0:
        return True, 0
    if pow(n, (p - 1) // 2, p) != 1:
        return False, 0
    if p % 4 == 3:
        return True, pow(n, (p + 1) // 4, p)
        
    q = p - 1
    s = 0
    while (q & 1) == 0:
        q >>= 1
        s += 1
        
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1
        
    c = pow(z, q, p)
    x = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s
    while t != 1:
        i = 1
        t2 = mul_mod(t, t, p)
        while t2 != 1:
            t2 = mul_mod(t2, t2, p)
            i += 1
        b = pow(c, 1 << (m - i - 1), p)
        x = mul_mod(x, b, p)
        b2 = mul_mod(b, b, p)
        t = mul_mod(t, b2, p)
        c = b2
        m = i
    return True, x

def is_root_mod(n, a, b, mod):
    val1 = (n * n * n + b) % mod
    na = n + a
    val2 = (na * na * na + b) % mod
    return val1 == 0 and val2 == 0

def sieve_primes(limit):
    is_prime = [True] * (limit + 1)
    primes = []
    for i in range(2, limit + 1):
        if not is_prime[i]: continue
        primes.append(i)
        if i * i <= limit:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return primes

def factorize(n, primes):
    out = []
    tmp = n
    for p in primes:
        if p * p > tmp: break
        if tmp % p == 0:
            e = 0
            while tmp % p == 0:
                tmp //= p
                e += 1
            out.append([p, e])
    if tmp > 1:
        out.append([tmp, 1])
    return out

def add_factor(factors, p, e):
    for kv in factors:
        if kv[0] == p:
            kv[1] += e
            return
    factors.append([p, e])

def solutions_mod_p(p, a, b):
    sols = []
    if p <= 5 or (a % p) == 0:
        for n in range(p):
            if is_root_mod(n, a, b, p):
                sols.append(n)
        return sols

    if p == 3: return sols

    inv3 = mod_inv_prime(3, p)
    inv2 = mod_inv_prime(2, p)
    a_mod = a % p
    D = (p + p - mul_mod(a_mod, a_mod, p)) % p
    D = mul_mod(D, inv3, p)

    ok, sqrtD = mod_sqrt(D, p)
    if not ok: return sols

    roots = [sqrtD, (p - sqrtD) % p]
    for s in roots:
        tmp = (p + s - a_mod) % p
        n = mul_mod(tmp, inv2, p)
        if is_root_mod(n, a, b, p):
            if n not in sols:
                sols.append(n)
    return sols

def solve_prime_power(p, max_exp, a, b):
    sols = solutions_mod_p(p, a, b)
    if not sols: return 1, [0]

    mod = p
    for exp in range(1, max_exp):
        next_mod = mod * p
        nxt = []
        for r in sols:
            for t in range(p):
                n = r + t * mod
                if is_root_mod(n, a, b, next_mod):
                    nxt.append(n)
        if not nxt: break
        sols = nxt
        mod = next_mod

    return mod, sols

def crt(a, mod_a, b, mod_b):
    inv = mod_inv_coprime(mod_a % mod_b, mod_b)
    t = (b + mod_b - (a % mod_b)) % mod_b
    k = mul_mod(t, inv, mod_b)
    return a + mod_a * k

def compute_G(a, b, primes, a_pow6, b_term, a_factors):
    R = a_pow6[a] + b_term[b]
    factors = factorize(R, primes)
    for p, e in a_factors[a]:
        add_factor(factors, p, 3 * e)

    blocks = []
    for p, e in factors:
        mod, sols = solve_prime_power(p, e, a, b)
        if mod > 1:
            blocks.append((mod, sols))
            
    if not blocks: return 0

    blocks.sort(key=lambda x: len(x[1]))

    mod = 1
    residues = [0]
    for b_mod, b_sols in blocks:
        nxt = []
        for r in residues:
            for s in b_sols:
                nxt.append(crt(r, mod, s, b_mod))
        mod *= b_mod
        residues = nxt

    return min(residues)

def worker_func(idx, primes, a_pow6, b_term, a_factors, n):
    max_b = n
    a = idx // max_b + 1
    b = idx % max_b + 1
    return compute_G(a, b, primes, a_pow6, b_term, a_factors)

def solve():
    max_a = 18
    max_b = 1900
    primes = sieve_primes(200000)
    a_pow6 = [0] * (max_a + 1)
    a_factors = [[] for _ in range(max_a + 1)]
    for a in range(1, max_a + 1):
        a_pow6[a] = a**6
        a_factors[a] = factorize(a, primes)
        
    b_term = [0] * (max_b + 1)
    for b in range(1, max_b + 1):
        b_term[b] = 27 * b * b
        
    total_tasks = max_a * max_b
    threads = multiprocessing.cpu_count()
    if threads == 0: threads = 4
    
    tasks = [(i, primes, a_pow6, b_term, a_factors, max_b) for i in range(total_tasks)]
    with multiprocessing.Pool(threads) as pool:
        results = pool.starmap(worker_func, tasks)
        
    total_sum = sum(results)
    return str(total_sum)

if __name__ == '__main__':
    print(solve())
