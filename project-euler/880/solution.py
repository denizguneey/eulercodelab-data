import math
import sys

MOD = 1031 * 1031 * 1031 + 2

def isqrt_u64(n):
    return math.isqrt(n)

def icbrt_u64(n):
    if n < 0:
        return -icbrt_u64(-n)
    x = int(math.floor(n ** (1.0/3.0)))
    while (x + 1) ** 3 <= n:
        x += 1
    while x ** 3 > n:
        x -= 1
    return x

def i4rt_u64(n):
    x = int(math.floor(n ** 0.25))
    while (x + 1) ** 4 <= n:
        x += 1
    while x ** 4 > n:
        x -= 1
    return x

def precompute_cube_free(limit):
    spf = list(range(limit + 1))
    for i in range(2, math.isqrt(limit) + 1):
        if spf[i] == i:
            for j in range(i * i, limit + 1, i):
                if spf[j] == j:
                    spf[j] = i

    cf = [0] * (limit + 1)
    if limit >= 1:
        cf[1] = 1
    for n in range(2, limit + 1):
        x = n
        res = 1
        while x > 1:
            p = spf[x]
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            r = e % 3
            if r == 1:
                res *= p
            elif r == 2:
                res *= p * p
        cf[n] = res
    return cf

def sumsq_mod(n):
    t = n * (n + 1) * (2 * n + 1) // 6
    return t % MOD

def solve_H_mod(N):
    q_max = i4rt_u64(4 * N)
    
    max_p_even2 = 0
    if N >= 4:
        c = icbrt_u64(N // 4)
        if c > 1:
            max_p_even2 = (c - 1) // 2

    max_p_odd1 = 0
    c = icbrt_u64(N)
    if c > 1:
        max_p_odd1 = (c - 1) // 4
        
    max_p = max(max_p_even2, max_p_odd1)
    
    limit = max(4 * max_p, 2 * q_max) + 16
    cube_free = precompute_cube_free(limit)

    ans = 0

    for q in range(1, q_max + 1):
        if q % 2 != 0:
            Ndiv = N // q
            c = icbrt_u64(Ndiv)
            if c <= q:
                continue
            p_max = (c - q) // 4
            if p_max == 0:
                continue
                
            dx = cube_free[q]
            
            for p in range(1, p_max + 1):
                if math.gcd(p, q) != 1:
                    continue
                if p == 2 * q:
                    continue
                    
                t = q + 4 * p
                t3 = t * t * t
                X0 = q * t3
                
                u = p - 2 * q
                Y0 = 4 * p * u * u * u
                
                absY = abs(Y0)
                max0 = X0 if X0 > absY else absY
                if max0 > N:
                    continue
                    
                dy = cube_free[4 * p]
                if dx == dy:
                    continue
                    
                mmax = isqrt_u64(N // max0)
                s2 = sumsq_mod(mmax)
                
                absSum = (X0 + absY) % MOD
                ans = (ans + absSum * s2) % MOD
        else:
            Ndiv = N // (2 * q)
            c = icbrt_u64(Ndiv)
            halfq = q // 2
            if c <= halfq:
                continue
            p_max = (c - halfq) // 2
            if p_max == 0:
                continue
                
            dx = cube_free[2 * q]
            
            for p in range(1, p_max + 1):
                if math.gcd(p, q) != 1:
                    continue
                if p == 2 * q:
                    continue
                    
                t = halfq + 2 * p
                t3 = t * t * t
                X0 = 2 * q * t3
                
                u = p - 2 * q
                Y0 = p * u * u * u
                
                absY = abs(Y0)
                max0 = X0 if X0 > absY else absY
                if max0 > N:
                    continue
                    
                dy = cube_free[p]
                if dx == dy:
                    continue
                    
                mmax = isqrt_u64(N // max0)
                s2 = sumsq_mod(mmax)
                
                absSum = (X0 + absY) % MOD
                ans = (ans + absSum * s2) % MOD

    return ans % MOD

def solve():
    return str(solve_H_mod(10**15))

if __name__ == "__main__":
    print(solve())
