import math
import sys

def floor_log2(x):
    r = 0
    while x > 1:
        x >>= 1
        r += 1
    return r

def pow_leq(base, exp, limit):
    res = 1
    for _ in range(exp):
        res *= base
        if res > limit: return False
    return True

def int_nth_root(n, k):
    if k == 1 or n <= 1: return n
    approx = int(math.pow(n, 1.0 / k))
    r = max(1, approx)
    while pow_leq(r + 1, k, n): r += 1
    while not pow_leq(r, k, n): r -= 1
    return r

def mobius_sieve(nmax):
    mu = [0] * (nmax + 1)
    primes = []
    mu[1] = 1
    spf = [0] * (nmax + 1)
    for i in range(2, nmax + 1):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
            mu[i] = -1
        for p in primes:
            v = p * i
            if v > nmax: break
            spf[v] = p
            if i % p == 0:
                mu[v] = 0
                break
            mu[v] = -mu[i]
    return mu

def power_free_count_upto(M, mu):
    if M < 2: return 0
    L = floor_log2(M)
    max_d = min(L, len(mu) - 1)
    total = 0
    for d in range(1, max_d + 1):
        md = mu[d]
        if md == 0: continue
        root = int_nth_root(M, d)
        if root >= 2:
            total += md * (root - 1)
    return total

def build_coprime_table(L, mu):
    F = [[0] * (L + 1) for _ in range(L + 1)]
    for A in range(1, L + 1):
        for B in range(1, L + 1):
            m = min(A, B)
            total = 0
            for d in range(1, m + 1):
                md = mu[d]
                if md == 0: continue
                total += md * (A // d) * (B // d)
            F[A][B] = total
    return F

def build_countA(N, mu, L):
    roots = [0] * (L + 2)
    for k in range(1, L + 1):
        roots[k] = int_nth_root(N, k)
    roots[L + 1] = 1

    pf = [0] * (L + 2)
    for k in range(1, L + 2):
        pf[k] = power_free_count_upto(roots[k], mu)

    countA = [0] * (L + 1)
    for A in range(1, L + 1):
        countA[A] = pf[A] - pf[A + 1]
    return countA

def compute_D_mod(N, mod):
    L = floor_log2(N)
    mu = mobius_sieve(L)
    coprime = build_coprime_table(L, mu)
    countA = build_countA(N, mu, L)

    irrational = 0
    for A in range(1, L + 1):
        ca = countA[A]
        if ca == 0: continue
        ca_mod = ca % mod
        for B in range(1, L + 1):
            cb = countA[B]
            if cb == 0: continue
            if A == B:
                if ca < 2: continue
                pairs = (ca_mod * ((ca - 1) % mod)) % mod
            else:
                pairs = (ca_mod * (cb % mod)) % mod
            term = (pairs * (coprime[A][B] % mod)) % mod
            irrational = (irrational + term) % mod
            
    rational = coprime[L][L] % mod
    return (rational + irrational) % mod

def solve():
    N = 1000000000000000000
    mod = 1000000000
    ans = compute_D_mod(N, mod)
    return "{:09d}".format(ans)

if __name__ == '__main__':
    print(solve())
