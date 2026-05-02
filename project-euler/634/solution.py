import math

def isqrt(x):
    if x < 0: return 0
    return math.isqrt(x)

def icbrt(x):
    if x <= 0: return 0
    r = int(x ** (1.0/3.0))
    while (r + 1)**3 <= x: r += 1
    while r**3 > x: r -= 1
    return r

def iroot6(x):
    if x <= 0: return 0
    r = int(x ** (1.0/6.0))
    while (r + 1)**6 <= x: r += 1
    while r**6 > x: r -= 1
    return r

def primes_upto(n):
    if n < 2: return []
    is_comp = [False] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if not is_comp[i]:
            primes.append(i)
            if i * i <= n:
                for j in range(i * i, n + 1, i):
                    is_comp[j] = True
    return primes

def mobius_upto(n):
    mu = [0] * (n + 1)
    if n >= 1: mu[1] = 1
    lp = [0] * (n + 1)
    pr = []
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            pr.append(i)
            mu[i] = -1
        for p in pr:
            if p > lp[i] or i * p > n: break
            lp[i * p] = p
            if p == lp[i]:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu

def count_cubefree_upto(n):
    D = icbrt(n)
    mu = mobius_upto(D)
    s = 0
    for d in range(1, D + 1):
        if mu[d] == 0: continue
        d3 = d * d * d
        s += mu[d] * (n // d3)
    return s

def solve():
    N = 9000000000000000000
    vmax = icbrt(N)
    sqfree = [True] * (vmax + 1)
    sqfree[0] = False
    
    P = isqrt(vmax)
    pr = primes_upto(P)
    for p in pr:
        p2 = p * p
        for m in range(p2, vmax + 1, p2):
            sqfree[m] = False
            
    powerful = 0
    squarefree_count = 0
    for b in range(1, vmax + 1):
        if not sqfree[b]: continue
        squarefree_count += 1
        b3 = b * b * b
        q = N // b3
        powerful += isqrt(q)
        
    sqrtN = isqrt(N)
    cubefree_count = count_cubefree_upto(sqrtN)
    
    r6 = iroot6(N)
    prime6 = len(primes_upto(r6))
    
    ans = powerful - squarefree_count - cubefree_count - prime6 + 1
    return str(ans)

if __name__ == '__main__':
    print(solve())
