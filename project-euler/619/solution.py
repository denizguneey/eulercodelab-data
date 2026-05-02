import math
import sys

MOD = 1000000007

def sieve_spf(n):
    spf = [0] * (n + 1)
    for i in range(2, n + 1):
        if spf[i] == 0:
            spf[i] = i
            if i * i <= n:
                for j in range(i * i, n + 1, i):
                    if spf[j] == 0:
                        spf[j] = i
    spf[1] = 1
    return spf

def list_primes_from_spf(spf):
    primes = []
    for i in range(2, len(spf)):
        if spf[i] == i:
            primes.append(i)
    return primes

def rank_squarefree_vectors(a, b, spf, prime_id, num_primes):
    basis = [[] for _ in range(num_primes)]
    rank = 0
    
    for x in range(a, b + 1):
        n = x
        v = set()
        while n > 1:
            p = spf[n]
            cnt = 0
            while n % p == 0:
                n //= p
                cnt ^= 1
            if cnt:
                v.symmetric_difference_update([prime_id[p]])
                
        v = sorted(list(v))
        while v:
            piv = v[-1]
            if not basis[piv]:
                basis[piv] = v
                rank += 1
                break
                
            tmp = set(v)
            tmp.symmetric_difference_update(basis[piv])
            v = sorted(list(tmp))
            
    return rank

def C_mod(a, b, spf, prime_id, num_primes, mod):
    n = b - a + 1
    r = rank_squarefree_vectors(a, b, spf, prime_id, num_primes)
    nullity = n - r
    total = pow(2, nullity, mod)
    return (total + mod - 1) % mod

def solve():
    A = 1000000
    B = 1234567
    
    spf = sieve_spf(B)
    primes = list_primes_from_spf(spf)
    P = len(primes)
    
    prime_id = [-1] * (B + 1)
    for i in range(P):
        prime_id[primes[i]] = i
        
    ans = C_mod(A, B, spf, prime_id, P, MOD)
    return str(ans)

if __name__ == '__main__':
    # Increase recursion depth just in case though we are iterative
    sys.setrecursionlimit(2000)
    print(solve())
