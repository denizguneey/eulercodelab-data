import sys

sys.setrecursionlimit(2000)
MOD = 1000000007

class Factor:
    def __init__(self, p, a):
        self.p = p
        self.a = a

class Elem:
    def __init__(self, v, w):
        self.v = v
        self.w = w

def primes_upto(n):
    is_prime = bytearray(n + 1)
    for i in range(len(is_prime)): is_prime[i] = 1
    if n >= 0: is_prime[0] = 0
    if n >= 1: is_prime[1] = 0
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for m in range(p * p, n + 1, p):
                is_prime[m] = 0
    return [i for i in range(2, n + 1) if is_prime[i]]

def factorial_factors(n):
    out = []
    primes = primes_upto(n)
    for p in primes:
        a = 0
        x = n
        while x:
            x //= p
            a += x
        out.append(Factor(p, a))
    return out

def mod_mul(a, b):
    return (a * b) % MOD

def gen_divs(fac, idx, cap, v, w, out):
    if idx == len(fac):
        out.append(Elem(v, w))
        return
    p = fac[idx].p
    a = fac[idx].a
    negp = (MOD - (p % MOD)) % MOD
    vv = v
    ww = w
    for e in range(a + 1):
        gen_divs(fac, idx + 1, cap, vv, ww, out)
        if e == a: break
        if vv > cap // p: break
        vv *= p
        ww = mod_mul(ww, negp)

def prefix_sum(X, A, B, prefB):
    j = len(B)
    ans = 0
    for a in A:
        if a.v > X: break
        lim = X // a.v
        while j > 0 and B[j - 1].v > lim:
            j -= 1
        ans = (ans + mod_mul(a.w, prefB[j])) % MOD
    return ans

def S_factorial_bounded(n, L, H):
    fac = factorial_factors(n)
    split = min(5, len(fac))
    fa = fac[:split]
    fb = fac[split:]

    A = []
    B = []
    gen_divs(fa, 0, H, 1, 1, A)
    gen_divs(fb, 0, H, 1, 1, B)

    A.sort(key=lambda x: x.v)
    B.sort(key=lambda x: x.v)

    prefB = [0] * (len(B) + 1)
    for i in range(len(B)):
        prefB[i + 1] = (prefB[i] + B[i].w) % MOD

    sumH = prefix_sum(H, A, B, prefB)
    Lm1 = L - 1
    sumL = 0 if L <= 1 else prefix_sum(Lm1, A, B, prefB)
    return (sumH + MOD - sumL) % MOD

def solve():
    L = 10**20
    H = 10**60
    ans = S_factorial_bounded(70, L, H)
    return str(ans)

if __name__ == '__main__':
    print(solve())
