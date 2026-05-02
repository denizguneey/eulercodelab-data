import math

def solve():
    MOD = 1000000007
    n = 1000000000000

    # Lehmer prime counting
    SLIMIT = 5000000
    is_p = bytearray(b'\x01') * (SLIMIT + 1); is_p[0] = is_p[1] = 0
    for i in range(2, int(SLIMIT**0.5)+1):
        if is_p[i]:
            for j in range(i*i, SLIMIT+1, i): is_p[j] = 0
    primes_list = [i for i in range(2, SLIMIT+1) if is_p[i]]
    pi_arr = [0]*(SLIMIT+1)
    for i in range(2, SLIMIT+1): pi_arr[i] = pi_arr[i-1] + is_p[i]

    cache = {}
    def phi_f(x, s):
        if s == 0: return x
        if s == 1: return x - x//2
        if s == 2: return x - x//2 - x//3 + x//6
        if s == 3: return x - x//2 - x//3 - x//5 + x//6 + x//10 + x//15 - x//30
        if x <= SLIMIT and primes_list[s-1]**2 > x:
            return pi_arr[x] - s + 1
        key = (x, s)
        if key in cache: return cache[key]
        r = phi_f(x, s-1) - phi_f(x // primes_list[s-1], s-1)
        cache[key] = r; return r

    lc = {}
    def isqrt(x):
        r = int(math.isqrt(x))
        while (r+1)*(r+1) <= x: r += 1
        while r*r > x: r -= 1
        return r
    def icbrt(x):
        r = int(round(x**(1/3)))
        while (r+1)**3 <= x: r += 1
        while r > 0 and r**3 > x: r -= 1
        return r
    def iroot4(x):
        r = int(round(x**0.25))
        while (r+1)**4 <= x: r += 1
        while r > 0 and r**4 > x: r -= 1
        return r

    def lehmer(x):
        if x <= SLIMIT: return pi_arr[x]
        if x in lc: return lc[x]
        a = lehmer(iroot4(x)); b = lehmer(isqrt(x)); c = lehmer(icbrt(x))
        s = phi_f(x, a) + (b+a-2)*(b-a+1)//2
        for i in range(a+1, b+1):
            p = primes_list[i-1]; w = x // p; s -= lehmer(w)
            if i <= c:
                bi = lehmer(isqrt(w))
                for j in range(i, bi+1):
                    pj = primes_list[j-1]; s -= lehmer(w//pj) - (j-1)
        lc[x] = s; return s

    n_mod = n % MOD; ans = 0
    y = min(n, 100000000)

    # Segmented sieve for primes up to y
    root = int(y**0.5); base_primes = [p for p in primes_list if p <= root]
    SEG = 1000000
    for low in range(2, y+1, SEG):
        high = min(y, low+SEG-1); mark = bytearray(b'\x01') * (high-low+1)
        for p in base_primes:
            start = max(p*p, ((low+p-1)//p)*p)
            if start > high: continue
            for v in range(start, high+1, p): mark[v-low] = 0
        for p in range(low, high+1):
            if p < 2 or not mark[p-low]: continue
            pw = p
            while pw <= n:
                q = n // pw; q_mod = q % MOD
                term = (n_mod * q_mod - q_mod * q_mod) % MOD
                ans = (ans + 2 * term) % MOD
                if pw > n // p: break
                pw *= p

    if y < n:
        qmax = n // (y+1)
        for q in range(1, qmax+1):
            l = n//(q+1)+1; r = n//q
            if r <= y: continue
            if l <= y: l = y+1
            if l > r: continue
            cnt = lehmer(r) - lehmer(l-1)
            if cnt:
                q_mod = q % MOD
                term = (n_mod * q_mod - q_mod * q_mod) % MOD
                ans = (ans + 2 * term % MOD * (cnt % MOD)) % MOD

    return str(ans % MOD)

if __name__ == '__main__':
    print(solve())
