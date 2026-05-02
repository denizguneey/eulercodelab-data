import math

def mul_mod(a, b, mod):
    return (a * b) % mod

def pow_mod(base, exp, mod):
    return pow(base, exp, mod)

def tonelli_shanks(n, p):
    if n == 0:
        return 0
    if p == 2:
        return n
    if pow_mod(n, (p - 1) // 2, p) != 1:
        return 0
    if (p % 4) == 3:
        return pow_mod(n, (p + 1) // 4, p)
        
    q = p - 1
    s = 0
    while (q % 2) == 0:
        q //= 2
        s += 1
        
    z = 2
    while pow_mod(z, (p - 1) // 2, p) != p - 1:
        z += 1
        
    c = pow_mod(z, q, p)
    x = pow_mod(n, (q + 1) // 2, p)
    t = pow_mod(n, q, p)
    m = s
    
    while t != 1:
        i = 1
        t2i = mul_mod(t, t, p)
        while i < m and t2i != 1:
            t2i = mul_mod(t2i, t2i, p)
            i += 1
            
        b = pow_mod(c, 1 << (m - i - 1), p)
        x = mul_mod(x, b, p)
        t = mul_mod(t, mul_mod(b, b, p), p)
        c = mul_mod(b, b, p)
        m = i
        
    return x

def solve_343(limit):
    lpf_small = [0] * (limit + 2)
    primes = []
    
    for i in range(2, limit + 2):
        if lpf_small[i] == 0:
            for j in range(i, limit + 2, i):
                lpf_small[j] = i
            if i <= limit:
                primes.append(i)
                
    rem = [0] * (limit + 1)
    lpf_q = [1] * (limit + 1)
    
    for k in range(1, limit + 1):
        rem[k] = k * k - k + 1
        
    for p in primes:
        if p == 2:
            continue
        roots = []
        if p == 3:
            roots.append(2)
        else:
            neg_three = (2 * p - 3) % p
            if pow_mod(neg_three, (p - 1) // 2, p) != 1:
                continue
            sq = tonelli_shanks(neg_three, p)
            inv2 = (p + 1) // 2
            r1 = ((1 + sq) % p * inv2) % p
            r2 = ((1 + p - sq) % p * inv2) % p
            roots.append(r1)
            if r2 != r1:
                roots.append(r2)
                
        for root in roots:
            k = root
            if k == 0:
                k += p
            for j in range(k, limit + 1, p):
                val = rem[j]
                if val % p != 0:
                    continue
                while val % p == 0:
                    val //= p
                rem[j] = val
                lpf_q[j] = p
                
    total = 0
    for k in range(1, limit + 1):
        rem_val = rem[k]
        if rem_val > 1:
            lpf_q[k] = max(lpf_q[k], rem_val)
        lpf_kp1 = lpf_small[k + 1]
        largest = max(lpf_kp1, lpf_q[k])
        total += largest - 1
        
    return total

def solve():
    ans = solve_343(2000000)
    return str(ans)

if __name__ == '__main__':
    print(solve())
