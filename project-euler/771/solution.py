import math

MOD = 1000000007

def count_intervals(terms):
    if terms < 5: return 0
    a = terms - 4
    b = terms - 3
    return (a * b // 2) % MOD

def floor_root4(n):
    approx = int(math.floor(math.pow(n, 0.25)))
    while (approx + 1)**4 <= n: approx += 1
    while approx**4 > n: approx -= 1
    return approx

def sieve_phi(n):
    phi = list(range(n + 1))
    for i in range(2, n + 1):
        if phi[i] == i:
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i
    return phi

def count_geometric(n, root4):
    if root4 < 2: return 0
    phi = sieve_phi(root4)
    total = 0
    for p in range(2, root4 + 1):
        pk = p**4
        while pk <= n:
            div = n // pk
            total = (total + phi[p] * div) % MOD
            pk *= p
    return total

def count_terms(n, a0, a1, m, plus):
    terms = 2
    while True:
        a2 = (m * a1 + a0) if plus else (m * a1 - a0)
        if a2 <= a1 or a2 > n: break
        terms += 1
        a0, a1 = a1, a2
    return terms

def count_consecutive(n):
    if n < 5: return 0
    a = n - 4
    b = n - 3
    return (a * b // 2) % MOD

def count_hybrid(n):
    if n < 54: return 0
    terms = 1
    v = 2
    while v <= n:
        terms += 1
        v *= 3
    if terms < 5: return 0
    return (terms - 4) % MOD

def count_sporadic(n):
    last_terms = [6, 9, 9, 16, 12, 20, 48, 60, 9, 16]
    return sum(1 for v in last_terms if v <= n) % MOD

def compute_g(n):
    if n < 5: return 0
    root4 = floor_root4(n)
    ans = 0
    
    ans = (ans + count_consecutive(n)) % MOD
    ans = (ans + count_geometric(n, root4)) % MOD
    
    for m in range(3, root4 + 1):
        terms = count_terms(n, 1, m, m, False)
        ans = (ans + count_intervals(terms)) % MOD
        
    ans = (ans + count_intervals(count_terms(n, 1, 2, 3, False))) % MOD
    ans = (ans + count_intervals(count_terms(n, 1, 3, 4, False))) % MOD
    
    ans = (ans + count_intervals(count_terms(n, 1, 2, 1, True))) % MOD
    for m in range(2, root4 + 1):
        terms = count_terms(n, 1, m, m, True)
        ans = (ans + count_intervals(terms)) % MOD
        
    ans = (ans + count_intervals(count_terms(n, 1, 3, 2, True))) % MOD
    
    ans = (ans + count_hybrid(n)) % MOD
    ans = (ans + count_sporadic(n)) % MOD
    
    return ans

def solve():
    return str(compute_g(10**18))

if __name__ == "__main__":
    print(solve())
