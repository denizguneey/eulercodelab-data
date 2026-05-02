import math

def isqrt_floor(x):
    if x < 0: return 0
    return math.isqrt(x)

def iroot6_floor(n):
    r = int(math.pow(n, 1.0 / 6.0))
    while (r + 1)**6 <= n: r += 1
    while r**6 > n: r -= 1
    return r

class Mobius:
    def __init__(self, n):
        self.N = n
        self.mu = [0] * (n + 1)
        self.pref_mu = [0] * (n + 1)
        self.pref_sqfree = [0] * (n + 1)
        
        primes = []
        lp = [0] * (n + 1)
        self.mu[1] = 1
        
        for i in range(2, n + 1):
            if lp[i] == 0:
                lp[i] = i
                primes.append(i)
                self.mu[i] = -1
            for p in primes:
                if p > lp[i] or i * p > n: break
                lp[i * p] = p
                if p == lp[i]:
                    self.mu[i * p] = 0
                    break
                self.mu[i * p] = -self.mu[i]
                
        for i in range(1, n + 1):
            self.pref_mu[i] = self.pref_mu[i - 1] + self.mu[i]
            self.pref_sqfree[i] = self.pref_sqfree[i - 1] + (1 if self.mu[i] != 0 else 0)

class MertensMemo:
    def __init__(self, mb):
        self.mb = mb
        self.memo = {}
        
    def M(self, n):
        if n <= self.mb.N: return self.mb.pref_mu[n]
        if n in self.memo: return self.memo[n]
        res = 1
        l = 2
        while l <= n:
            q = n // l
            r = n // q
            res -= (r - l + 1) * self.M(q)
            l = r + 1
        self.memo[n] = res
        return res

def squarefree_count(n, mb, mm):
    if n <= mb.N: return mb.pref_sqfree[n]
    r = isqrt_floor(n)
    s = 0
    for d in range(1, r + 1):
        s += mb.mu[d] * (n // (d * d))
    return s

def squarefree_even_count(n, mb, mm):
    Q = squarefree_count(n, mb, mm)
    M = mm.M(n)
    return (Q + M) // 2

def f(N):
    LIM = 1000000
    mb = Mobius(LIM)
    mm = MertensMemo(mb)
    
    amax = iroot6_floor(N)
    ans = 0
    for a in range(1, amax + 1):
        a6 = a**6
        t = N // a6
        s = isqrt_floor(t)
        bmax = isqrt_floor(s)
        ans += squarefree_even_count(bmax, mb, mm)
    return ans

def solve():
    N = 10**36
    ans = f(N)
    return str(ans)

if __name__ == '__main__':
    print(solve())
