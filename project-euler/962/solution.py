import math

def solve():
    limit = 1000000

    def isqrt_f(x):
        if x <= 0: return 0
        r = int(math.isqrt(x))
        while (r+1)*(r+1)<=x: r+=1
        while r*r>x: r-=1
        return r
    def isqrt_c(x):
        if x<=0: return 0
        r = isqrt_f(x)
        if r*r < x: r += 1
        return r
    def cbrt_f(x):
        lo = 0; hi = int(x**(1/3))+5
        while hi*hi*hi <= x: hi += 1
        while lo+1 < hi:
            mid = (lo+hi)//2
            if mid*mid*mid <= x: lo = mid
            else: hi = mid
        return lo

    # SPF sieve
    n2 = 2*limit*limit; k_max = cbrt_f(n2)+2
    mx = max(k_max, limit//6+5)
    spf = list(range(mx+1)); spf[0] = 0; spf[1] = 1
    for i in range(2, int(mx**0.5)+1):
        if spf[i] != i: continue
        for j in range(i*i, mx+1, i):
            if spf[j] == j: spf[j] = i

    # Squarefree parts
    sf = [1]*(k_max+1); sf[0] = 0
    for x in range(1, k_max+1):
        t = x; val = 1
        while t > 1:
            p = spf[t]; c = 0
            while t%p==0: t//=p; c ^= 1
            if c: val *= p
        sf[x] = val

    # Factor tables
    def factorize(x):
        fs = []; t = x
        while t > 1:
            p = spf[t]; e = 0
            while t%p==0: t//=p; e += 1
            fs.append((p, e))
        return fs
    factors = [[] for _ in range(mx+1)]
    for x in range(2, mx+1): factors[x] = factorize(x)

    def count_for_k(k):
        L = limit // k
        if L < 2: return 0
        sub = 0; v_min = (k+1)//2
        for v in range(v_min, k):
            if math.gcd(v, k) != 1: continue
            u = k - v; sf_u = sf[u]; W = v * sf_u
            if W > L*L: continue
            wf = list(factors[v])
            if sf_u != 1: wf += [(pe[0], 1) for pe in factors[sf_u]]
            wf.sort()
            r_max = (u * L) // (u + 2*v)
            for r in range(1, r_max+1):
                rf = factors[r]; s0 = 1; i = j = 0; ok = True
                while i < len(wf) or j < len(rf):
                    if j == len(rf) or (i < len(wf) and wf[i][0] < rf[j][0]):
                        p, e = wf[i]; a = 0; i += 1
                    elif i == len(wf) or rf[j][0] < wf[i][0]:
                        p, a = rf[j]; e = 0; j += 1
                    else:
                        p, e = wf[i]; a = rf[j][1]; i += 1; j += 1
                    b0 = e-a if a < e else (a-e)&1
                    if b0 > 0:
                        s0 *= p**b0
                        if s0 > L: ok = False; break
                if not ok: continue
                s_min = ((u+2*v)*r + u-1)//u
                if s_min > L: continue
                ratio_min = (s_min+s0-1)//s0
                n_min = isqrt_c(ratio_min); n_max = isqrt_f(L//s0)
                if n_min > n_max: continue
                if s0 & 1 == 0:
                    if r & 1 == 0: sub += n_max-n_min+1
                    continue
                wp = r & 1
                if (n_min & 1) != wp: n_min += 1
                if n_min <= n_max: sub += (n_max-n_min)//2+1
        return sub

    total = sum(count_for_k(k) for k in range(2, k_max+1))
    return str(total)

if __name__ == '__main__':
    print(solve())
