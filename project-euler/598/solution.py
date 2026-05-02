import sys
import math

def primes_up_to(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(2, n + 1) if is_prime[i]]

def exp_in_fact(n, p):
    e = 0
    while n > 0:
        n //= p
        e += n
    return e

def solve_factorial(n):
    ps = primes_up_to(n)
    exps = [exp_in_fact(n, p) for p in ps]
    
    all_even = all(e % 2 == 0 for e in exps)
    
    bigP = [2, 3, 5, 7]
    
    max_val = max(exps) + 1 if exps else 1
    basis = primes_up_to(max_val)
    P = len(basis)
    p2idx = {p: i for i, p in enumerate(basis)}
    
    fac = [[0] * P for _ in range(max_val + 1)]
    for x in range(2, max_val + 1):
        m = x
        for i, p in enumerate(basis):
            if p * p > m: break
            while m % p == 0:
                fac[x][i] += 1
                m //= p
        if m > 1:
            fac[x][p2idx[m]] += 1
            
    idx2 = p2idx.get(2, -1)
    idx3 = p2idx.get(3, -1)
    idx5 = p2idx.get(5, -1)
    idx7 = p2idx.get(7, -1)
    
    big_indices = [i for i, p in enumerate(basis) if p > 7]
    
    diffs = []
    for bp in bigP:
        if bp > n:
            diffs.append([])
            continue
            
        e = exp_in_fact(n, bp)
        E = e + 2
        v = []
        for y in range(1, e + 2):
            z = E - y
            dv = [fac[y][i] - fac[z][i] for i in range(P)]
            v.append(dv)
        diffs.append(v)
        
    while len(diffs) < 4:
        diffs.append([])
        
    pair01 = []
    for a in diffs[0]:
        for b in diffs[1]:
            s = [a[i] + b[i] for i in range(P)]
            pair01.append(s)
            
    pair23 = []
    for a in diffs[2]:
        for b in diffs[3]:
            s = [a[i] + b[i] for i in range(P)]
            pair23.append(s)
            
    map1 = {}
    for a in pair01:
        for b in pair23:
            ok = True
            for i in big_indices:
                if a[i] + b[i] != 0:
                    ok = False
                    break
            if not ok: continue
            
            d2 = a[idx2] + b[idx2]
            d3 = a[idx3] + b[idx3]
            d5 = a[idx5] + b[idx5]
            d7 = a[idx7] + b[idx7]
            key = (d2, d3, d5, d7)
            map1[key] = map1.get(key, 0) + 1
            
    map2 = {}
    map2[(0, 0, 0, 0)] = 1
    
    for i in range(len(ps)):
        p = ps[i]
        if p <= 7: continue
        e = exps[i]
        E = e + 2
        
        deltas = []
        for y in range(1, e + 2):
            z = E - y
            deltas.append((
                fac[y][idx2] - fac[z][idx2],
                fac[y][idx3] - fac[z][idx3],
                fac[y][idx5] - fac[z][idx5],
                fac[y][idx7] - fac[z][idx7]
            ))
            
        nxt = {}
        for kv, cnt in map2.items():
            d2, d3, d5, d7 = kv
            for dd in deltas:
                nk = (d2 + dd[0], d3 + dd[1], d5 + dd[2], d7 + dd[3])
                nxt[nk] = nxt.get(nk, 0) + cnt
        map2 = nxt
        
    M = 0
    for kv, cnt in map1.items():
        d2, d3, d5, d7 = kv
        need = (-d2, -d3, -d5, -d7)
        if need in map2:
            M += cnt * map2[need]
            
    fixed = 1 if all_even else 0
    ans = (M + fixed) // 2
    return ans
    
def solve():
    return str(solve_factorial(100))

if __name__ == '__main__':
    print(solve())
