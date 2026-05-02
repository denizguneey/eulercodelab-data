def trim_poly(poly):
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly

def divide_poly(a, b):
    da = len(a) - 1
    db = len(b) - 1
    q = [0] * max(0, da - db + 1)
    
    a = list(a) 
    for i in range(da, db - 1, -1):
        coef = a[i]
        if coef == 0:
            continue
        q[i - db] = coef
        for j in range(db + 1):
            a[i - db + j] -= coef * b[j]
    return trim_poly(q)

def cyclotomic(n):
    phi = [[] for _ in range(n + 1)]
    phi[1] = [-1, 1]
    for k in range(2, n + 1):
        poly = [0] * (k + 1)
        poly[0] = -1
        poly[k] = 1
        for d in range(1, k):
            if k % d == 0:
                poly = divide_poly(poly, phi[d])
        phi[k] = trim_poly(poly)
    return phi[n]

def multiply_by_x(v, rel):
    d = len(v)
    res = [0] * d
    for i in range(d - 1):
        res[i + 1] += v[i]
    h = v[d - 1]
    if h != 0:
        for i in range(d):
            res[i] -= h * rel[i]
    return res

def count_zero_sums(S, m):
    phi = cyclotomic(S)
    d = len(phi) - 1
    rel = phi[:d]
    
    powers = [[0] * d for _ in range(S)]
    powers[0][0] = 1
    for i in range(1, S):
        powers[i] = multiply_by_x(powers[i - 1], rel)
        
    mid = S // 2
    right_n = S - mid
    
    left_sums = {}
    
    for mask in range(1 << mid):
        cnt = bin(mask).count('1')
        if cnt > m:
            continue
        
        sum_arr = [0] * d
        for k in range(mid):
            if (mask >> k) & 1:
                pv = powers[k]
                for i in range(d):
                    sum_arr[i] += pv[i]
                    
        key = tuple(sum_arr)
        if key not in left_sums:
            left_sums[key] = [0] * (m + 1)
        left_sums[key][cnt] += 1
        
    total = [0] * (m + 1)
    
    for mask in range(1 << right_n):
        cnt = bin(mask).count('1')
        if cnt > m:
            continue
            
        sum_arr = [0] * d
        for k in range(right_n):
            if (mask >> k) & 1:
                pv = powers[mid + k]
                for i in range(d):
                    sum_arr[i] -= pv[i]
                    
        key = tuple(sum_arr)
        counts = left_sums.get(key)
        if counts:
            for lc in range(m - cnt + 1):
                ways = counts[lc]
                if ways:
                    total[lc + cnt] += ways
                    
    return total

def radical(n):
    res = 1
    x = n
    p = 2
    while p * p <= x:
        if x % p == 0:
            res *= p
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        res *= x
    return res

def multiply_poly(A, B, max_deg):
    res = [0] * (min(max_deg, len(A) + len(B) - 2) + 1)
    for i, a in enumerate(A):
        if a == 0: continue
        for j, b in enumerate(B):
            if b == 0: continue
            if i + j <= max_deg:
                res[i + j] += a * b
    return res

def solve_chandelier(n, m):
    if m < 0 or m > n: return 0
    if m == 0: return 1
    
    S = radical(n)
    G = n // S
    
    counts = count_zero_sums(S, m)
    P = counts[:(m + 1)]
    
    Final = [1]
    for _ in range(G):
        Final = multiply_poly(Final, P, m)
        
    return Final[m] if m < len(Final) else 0

def solve():
    ans = solve_chandelier(360, 20)
    return str(ans)

if __name__ == "__main__":
    print(solve())
