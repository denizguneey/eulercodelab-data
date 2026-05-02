import math

def solve():
    MOD = 715827883; N = 1000000000000

    def tri(x): return x*(x+1)//2

    root = int(math.isqrt(N))
    while (root+1)*(root+1) <= N: root += 1
    while root*root > N: root -= 1

    # Min25 prime prefix sieve
    vals = []
    l = 1
    while l <= N:
        v = N // l; r = N // v; vals.append(v); l = r + 1

    idx_small = [0]*(root+1); idx_large = [0]*(root+1)
    m = len(vals)
    g_count = [0]*m; g_sum = [0]*m

    for i in range(m):
        v = vals[i]
        if v <= root: idx_small[v] = i
        else: idx_large[N//v] = i
        g_count[i] = v - 1; g_sum[i] = tri(v) - 1

    lp = [0]*(root+1); primes = []
    for i in range(2, root+1):
        if lp[i] == 0: lp[i] = i; primes.append(i)
        for p in primes:
            v = i*p
            if v > root or p > lp[i]: break
            lp[v] = p

    def vid(x):
        return idx_small[x] if x <= root else idx_large[N//x]

    for p in primes:
        p2 = p*p
        if p2 > N: break
        ipm1 = vid(p-1)
        i = 0
        while i < m and vals[i] >= p2:
            j = vid(vals[i]//p)
            g_count[i] -= g_count[j] - g_count[ipm1]
            g_sum[i] -= p * (g_sum[j] - g_sum[ipm1])
            i += 1

    answer = 0
    for p in primes:
        pe = p
        while pe <= N:
            x = N // pe
            s = tri(x) - p * tri(x // p)
            coef = pe - pe // p - 1
            v = coef * s % MOD
            answer = (answer + v) % MOD

            if pe > N // p: break
            pe *= p

    max_q = N // (root + 1)
    for q in range(1, max_q + 1):
        L = N // (q + 1) + 1; R = N // q
        if R <= root: break
        if L <= root: L = root + 1
        if L > R: continue
        cnt = g_count[vid(R)] - g_count[vid(L-1)]
        if cnt == 0: continue
        sp = g_sum[vid(R)] - g_sum[vid(L-1)]
        group = tri(q) * (sp - 2 * cnt)
        answer = (answer + group) % MOD

    return str(answer % MOD)

if __name__ == '__main__':
    print(solve())
