import math
from collections import defaultdict

def gcd_int(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm_int(a, b):
    return (a // gcd_int(a, b)) * b

def g_value(n):
    largest_prime_factor = [0] * (n + 1)
    for p in range(2, n + 1):
        if largest_prime_factor[p] != 0:
            continue
        for v in range(p, n + 1, p):
            largest_prime_factor[v] = p
            
    histograms = [defaultdict(float) for _ in range(n + 1)]
    count = 1.0
    for i in range(n + 1):
        if i > 0:
            count /= i
        histograms[i][1] = count
        
    for p in range(n, 1, -1):
        if largest_prime_factor[p] != p:
            continue
            
        for c in range(p, n + 1, p):
            if largest_prime_factor[c] != p:
                continue
                
            nxt = [defaultdict(float) for _ in range(n + 1)]
            count_rhs = 1.0
            multiplicity = 0
            
            while multiplicity * c <= n:
                rhs_len = multiplicity * c
                rhs_lcm = 1 if multiplicity == 0 else c
                
                for lhs_len in range(n - rhs_len + 1):
                    total = lhs_len + rhs_len
                    h = histograms[lhs_len]
                    nh = nxt[total]
                    
                    for l, count_val in h.items():
                        lcm_val = lcm_int(l, rhs_lcm)
                        nh[lcm_val] += count_val * count_rhs
                        
                multiplicity += 1
                count_rhs /= float(c * multiplicity)
                
            histograms = nxt
            
        for length in range(n + 1):
            h = histograms[length]
            squashed = defaultdict(float)
            for l, c_val in h.items():
                while l % p == 0:
                    l //= p
                    c_val *= p * p
                squashed[l] += c_val
            histograms[length] = squashed
            
    ans = 0.0
    for l, c_val in histograms[n].items():
        ans += l * l * c_val
        
    return ans

def solve():
    ans = g_value(350)
    # Output scientific format matching C++
    return f"{ans:.9e}"

if __name__ == '__main__':
    print(solve())
