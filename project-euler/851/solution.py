import sys

kMod = 1000000007

def mod_add(a, b):
    a += b
    if a >= kMod: a -= kMod
    return a

def mod_sub(a, b):
    a -= b
    if a < 0: a += kMod
    return a

def mod_mul(a, b):
    return (a * b) % kMod

def mod_pow(a, e):
    r = 1 % kMod
    a %= kMod
    if a < 0: a += kMod
    while e > 0:
        if e & 1: r = mod_mul(r, a)
        a = mod_mul(a, a)
        e >>= 1
    return r

def mod_inv(a):
    return mod_pow(a, kMod - 2)

def sieve_primes(n):
    is_prime = [True] * (n + 1)
    if n >= 0: is_prime[0] = False
    if n >= 1: is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    primes = [i for i in range(2, n + 1) if is_prime[i]]
    return primes

def vp_factorial(n, p):
    e = 0
    while n:
        n //= p
        e += n
    return e

def factorial_mod(n):
    r = 1
    for i in range(2, n + 1):
        r = mod_mul(r, i)
    return r

def geom_sum(base, e):
    base %= kMod
    if base < 0: base += kMod
    if e < 0: return 0
    if base == 1: return (e + 1) % kMod
    num = mod_sub(mod_pow(base, e + 1), 1)
    den = mod_sub(base, 1)
    return mod_mul(num, mod_inv(den))

def sigma_k_factorial(pe, k):
    res = 1
    for p, e in pe:
        base = mod_pow(p, k)
        s = geom_sum(base, e)
        res = mod_mul(res, s)
    return res

def mat_mul(A, B):
    C = [0] * 4
    C[0] = (mod_mul(A[0], B[0]) + mod_mul(A[1], B[2])) % kMod
    C[1] = (mod_mul(A[0], B[1]) + mod_mul(A[1], B[3])) % kMod
    C[2] = (mod_mul(A[2], B[0]) + mod_mul(A[3], B[2])) % kMod
    C[3] = (mod_mul(A[2], B[1]) + mod_mul(A[3], B[3])) % kMod
    return C

def mat_pow(base, e):
    r = [1, 0, 0, 1]
    while e > 0:
        if e & 1: r = mat_mul(r, base)
        base = mat_mul(base, base)
        e >>= 1
    return r

def tau_prime_power(tau_p, p, e):
    if e == 0: return 1
    if e == 1: return tau_p
    p11 = mod_pow(p, 11)
    M = [tau_p, mod_sub(0, p11), 1, 0]
    P = mat_pow(M, e - 1)
    return (mod_mul(P[0], tau_p) + mod_mul(P[1], 1)) % kMod

def compute_sigma1_upto(N):
    sig = [0] * (N + 1)
    for d in range(1, N + 1):
        for m in range(d, N + 1, d):
            sig[m] += d
    for i in range(N + 1):
        sig[i] %= kMod
    return sig

def compute_tau_upto(N, sigma1):
    tau = [0] * (N + 1)
    tau[1] = 1
    neg24 = mod_sub(0, 24)
    for n in range(2, N + 1):
        s = 0
        for k in range(1, n):
            s = (s + sigma1[k] * tau[n - k]) % kMod
        inv = mod_inv(n - 1)
        tau[n] = mod_mul(mod_mul(neg24, s), inv)
    return tau

def compute_tau_factorial_serial(pe, tau_small):
    prod = 1
    for p, e in pe:
        tau_p = tau_small[p]
        t = tau_prime_power(tau_p, p, e)
        prod = mod_mul(prod, t)
    return prod

def solve():
    N = 10000
    primes = sieve_primes(N)
    pe = [(p, vp_factorial(N, p)) for p in primes]
    
    n_mod = factorial_mod(N)
    n_pow = [1] * 6
    for i in range(1, 6):
        n_pow[i] = mod_mul(n_pow[i - 1], n_mod)
        
    sig = {}
    ks = [1, 3, 5, 7, 9, 11]
    for k in ks:
        sig[k] = sigma_k_factorial(pe, k)
        
    sigma1_small = compute_sigma1_upto(N)
    tau_small = compute_tau_upto(N, sigma1_small)
    
    def norm(x):
        x %= kMod
        if x < 0: x += kMod
        return x
        
    tau_fact = compute_tau_factorial_serial(pe, tau_small)
    
    c2 = mod_mul(norm(-24), sig[1])
    c4 = mod_mul(240, sig[3])
    c6 = mod_mul(norm(-504), sig[5])
    c8 = mod_mul(480, sig[7])
    c10 = mod_mul(norm(-264), sig[9])
    factor12 = mod_mul(65520, mod_inv(691))
    c12 = mod_mul(factor12, sig[11])
    
    inv2 = mod_inv(2)
    inv5 = mod_inv(5)
    inv7 = mod_inv(7)
    inv24185 = mod_inv(24185)
    
    a1 = c2
    a2 = mod_add(c4, mod_mul(12, mod_mul(n_pow[1], c2)))
    
    a3 = c6
    a3 = mod_add(a3, mod_mul(9, mod_mul(n_pow[1], c4)))
    a3 = mod_add(a3, mod_mul(72, mod_mul(n_pow[2], c2)))
    
    a4 = c8
    a4 = mod_add(a4, mod_mul(8, mod_mul(n_pow[1], c6)))
    a4 = mod_add(a4, mod_mul(mod_mul(216, inv5), mod_mul(n_pow[2], c4)))
    a4 = mod_add(a4, mod_mul(288, mod_mul(n_pow[3], c2)))
    
    a5 = c10
    a5 = mod_add(a5, mod_mul(mod_mul(15, inv2), mod_mul(n_pow[1], c8)))
    a5 = mod_add(a5, mod_mul(mod_mul(240, inv7), mod_mul(n_pow[2], c6)))
    a5 = mod_add(a5, mod_mul(144, mod_mul(n_pow[3], c4)))
    a5 = mod_add(a5, mod_mul(864, mod_mul(n_pow[4], c2)))
    
    a6 = c12
    a6 = mod_add(a6, mod_mul(mod_mul(norm(-4608), inv24185), tau_fact))
    a6 = mod_add(a6, mod_mul(mod_mul(36, inv5), mod_mul(n_pow[1], c10)))
    a6 = mod_add(a6, mod_mul(30, mod_mul(n_pow[2], c8)))
    a6 = mod_add(a6, mod_mul(mod_mul(720, inv7), mod_mul(n_pow[3], c6)))
    a6 = mod_add(a6, mod_mul(mod_mul(2592, inv7), mod_mul(n_pow[4], c4)))
    a6 = mod_add(a6, mod_mul(mod_mul(10368, inv5), mod_mul(n_pow[5], c2)))
    
    S = 0
    S = mod_add(S, mod_mul(norm(-6), a1))
    S = mod_add(S, mod_mul(15, a2))
    S = mod_add(S, mod_mul(norm(-20), a3))
    S = mod_add(S, mod_mul(15, a4))
    S = mod_add(S, mod_mul(norm(-6), a5))
    S = mod_add(S, a6)
    
    inv2985984 = mod_inv(2985984)
    ans = mod_mul(S, inv2985984)
    
    return str(ans)

if __name__ == "__main__":
    print(solve())
