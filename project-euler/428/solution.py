import math

def solve():
    target = 1000000000

    def isqrt(n):
        r = int(math.isqrt(n))
        while (r+1)*(r+1) <= n: r += 1
        while r*r > n: r -= 1
        return r

    limit = isqrt(target) + 5
    mu = [0] * (limit + 1)
    mu[1] = 1
    primes = []
    is_comp = [0] * (limit + 1)
    for i in range(2, limit + 1):
        if not is_comp[i]:
            primes.append(i); mu[i] = -1
        for p in primes:
            v = i * p
            if v > limit: break
            is_comp[v] = 1
            if i % p == 0: mu[v] = 0; break
            mu[v] = -mu[i]

    def sqfree_count(n):
        if n <= 0: return 0
        r = isqrt(n); s = 0
        for k in range(1, r + 1): s += mu[k] * (n // (k*k))
        return s

    cache_c6 = {}
    def S_c6(n):
        if n <= 0: return 0
        if n in cache_c6: return cache_c6[n]
        r = sqfree_count(n) - S_c6(n//2) - S_c6(n//3) - S_c6(n//6)
        cache_c6[n] = r; return r

    cache_a0 = {}
    def A0(n):
        if n <= 0: return 0
        if n in cache_a0: return cache_a0[n]
        res = 0; l = 1
        while l <= n:
            v = n // l; r = n // v
            res += v * (S_c6(r) - S_c6(l - 1))
            l = r + 1
        cache_a0[n] = res; return res

    def F_D(n, D):
        if n <= 0: return 0
        if D == 2: return 2*A0(n) + 2*A0(n//3)
        if D == 4: return 3*A0(n) + 3*A0(n//3) - A0(n//2) - A0(n//6)
        if D == 12: return 6*A0(n) - 2*A0(n//2)
        if D == 36: return 9*A0(n) - 3*A0(n//2) - 3*A0(n//3) + A0(n//6)
        return 0

    cache_sd = {}
    def S_D(n, D):
        if n <= 0: return 0
        k = (n, D)
        if k in cache_sd: return cache_sd[k]
        res = 0; l = 1
        while l <= n:
            v = n // l; r = n // v
            res += v * (F_D(r, D) - F_D(l - 1, D))
            l = r + 1
        cache_sd[k] = res; return res

    def chi_prefix(n):
        if n <= 0: return 0
        return 1 if n % 3 == 1 else 0

    cache_chisq = {}
    def S_chisq(n):
        if n <= 0: return 0
        if n in cache_chisq: return cache_chisq[n]
        r = isqrt(n); s = 0
        for k in range(1, r + 1):
            if k % 3 == 0: continue
            s += mu[k] * chi_prefix(n // (k*k))
        cache_chisq[n] = s; return s

    cache_fg = {}
    def F_G(n):
        if n <= 0: return 0
        if n in cache_fg: return cache_fg[n]
        res = 0; l = 1
        while l <= n:
            v = n // l; r = n // v
            res += v * (S_chisq(r) - S_chisq(l - 1))
            l = r + 1
        cache_fg[n] = res; return res

    def F1(n):
        if n <= 0: return 0
        return F_G(n) - F_G(n // 3)

    cache_sh = {}
    def S_h(n):
        if n <= 0: return 0
        if n in cache_sh: return cache_sh[n]
        res = 0; l = 1
        while l <= n:
            v = n // l; r = n // v
            if v % 3 == 1:
                res += F1(r) - F1(l - 1)
            l = r + 1
        cache_sh[n] = res; return res

    s2 = S_D(target, 2)
    s12 = S_D(target, 12)
    s4 = S_D(target, 4)
    s36_n3 = S_D(target // 3, 36)
    c_not3 = (s4 - s36_n3 - S_h(target)) // 2
    c_div3 = 0; m = target // 3; t = 1
    while m > 0:
        term = S_D(m, 4) - S_D(m // 3, 36)
        c_div3 += (2 * t - 1) * term
        t += 1; m //= 3
    return str(s2 + s12 + c_not3 + c_div3)

if __name__ == '__main__':
    print(solve())
