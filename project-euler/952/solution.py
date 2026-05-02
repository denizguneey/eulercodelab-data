def mod_pow(base, exp, mod):
    return pow(base, exp, mod)

def v_p_factorial(n, p):
    e = 0
    while n > 0:
        n //= p
        e += n
    return e

def v2_int(x):
    v = 0
    while (x & 1) == 0:
        x >>= 1
        v += 1
    return v

def build_spf_and_primes(n):
    spf = [0] * (n + 1)
    primes = []
    
    for i in range(2, n + 1):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
        for p in primes:
            v = p * i
            if v > n or p > spf[i]:
                break
            spf[v] = p
            
    return spf, primes

def factorize_int(x, spf):
    fac = []
    while x > 1:
        p = spf[x]
        e = 0
        while x > 1 and spf[x] == p:
            x //= p
            e += 1
        fac.append((p, e))
    return fac

def compute_R_mod(p, n, out_mod):
    spf, primes = build_spf_and_primes(n)
    max_exp = [0] * (n + 1)
    
    for q in primes:
        if q > n:
            break
            
        e = v_p_factorial(n, q)
        
        if q == 2:
            exp2 = 0
            if e >= 2:
                if (p & 3) == 1:
                    u = v2_int(p - 1)
                    exp2 = 0 if e <= u else (e - u)
                else:
                    v = v2_int(p + 1)
                    exp2 = 1 if e <= v else (e - v)
            if exp2 > max_exp[2]:
                max_exp[2] = exp2
            continue
            
        t = q - 1
        fac_qm1 = factorize_int(q - 1, spf)
        base_q = p % q
        
        for r, cnt in fac_qm1:
            for _ in range(cnt):
                if t % r == 0 and mod_pow(base_q, t // r, q) == 1:
                    t //= r
                else:
                    break
                    
        tmp = t
        for r, _ in fac_qm1:
            cnt = 0
            while tmp % r == 0:
                tmp //= r
                cnt += 1
            if cnt > max_exp[r]:
                max_exp[r] = cnt
                
        s = 1
        if e > 1:
            mod_q2 = q * q
            if mod_pow(p % mod_q2, t, mod_q2) == 1:
                s = 2
                if e > 2:
                    base = p
                    exp = t
                    mod = q * q * q
                    for k in range(3, e + 1):
                        if mod_pow(base, exp, mod) == 1:
                            s = k
                            mod *= q
                        else:
                            break
                            
        extra = e - s
        if extra > max_exp[q]:
            max_exp[q] = extra
            
    ans = 1 % out_mod
    for r in range(2, n + 1):
        if max_exp[r] > 0:
            ans = (ans * mod_pow(r, max_exp[r], out_mod)) % out_mod
            
    return ans

def solve():
    return str(compute_R_mod(1000000007, 10000000, 1000000007))

if __name__ == "__main__":
    assert compute_R_mod(7, 4, 1000000007) == 2
    assert compute_R_mod(1000000007, 12, 1000000007) == 17280
    print(solve())
