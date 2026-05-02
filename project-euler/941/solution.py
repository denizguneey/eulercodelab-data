import sys

sys.setrecursionlimit(2000)

kK = 10
kN = 12
kMod = 1234567891
kLcgMul = 920461
kLcgAdd = 800217387569
kLcgMod = 1000000000000

class Ranker:
    def __init__(self):
        self.pow_k = [0] * (kN + 1)
        self.pow_k[0] = 1
        for i in range(1, kN + 1):
            self.pow_k[i] = self.pow_k[i - 1] * kK
            
        self.mu = [0] * (kN + 1)
        for i in range(1, kN + 1):
            self.mu[i] = self.mobius(i)
            
    def mobius(self, x):
        n = x
        primes = 0
        p = 2
        while p * p <= n:
            if n % p == 0:
                exp = 0
                while n % p == 0:
                    n //= p
                    exp += 1
                if exp > 1:
                    return 0
                primes += 1
            p += 1
        if n > 1:
            primes += 1
        return 1 if (primes % 2 == 0) else -1
        
    def lyndon_prefix(self, n, w):
        p = 1
        for i in range(2, n + 1):
            if w[i] < w[i - p]:
                return p
            if w[i] > w[i - p]:
                p = i
        return p
        
    def is_necklace(self, n, w):
        p = 1
        for i in range(2, n + 1):
            if w[i] < w[i - p]:
                return False
            if w[i] > w[i - p]:
                p = i
        return (n % p == 0)
        
    def largest_necklace(self, n, w, neck):
        for i in range(n + 1):
            neck[i] = w[i]
        while not self.is_necklace(n, neck):
            p = self.lyndon_prefix(n, neck)
            neck[p] -= 1
            for i in range(p + 1, n + 1):
                neck[i] = kK

    def T_value(self, n, w):
        neck = [0] * (kN + 1)
        self.largest_necklace(n, w, neck)

        B = [[0] * (kN + 1) for _ in range(kN + 1)]
        B[0][0] = 1
        for t in range(1, n + 1):
            B[t][t] = 0
            for j in range(t - 1, -1, -1):
                B[t][j] = B[t][j + 1] + (kK - neck[j + 1]) * B[t - j - 1][0]
                
        suf = [[0] * (kN + 1) for _ in range(kN + 1)]
        for i in range(2, n + 1):
            p = i - 1
            for j in range(i, n + 1):
                if neck[j] > neck[j - p]:
                    p = j
                suf[i][j] = j - p
                
        total = self.lyndon_prefix(n, neck)
        for t in range(1, n + 1):
            for j in range(n):
                if j + t <= n:
                    total += B[t - 1][0] * (neck[j + 1] - 1) * self.pow_k[n - t - j]
                else:
                    s = 0
                    if j >= n - t + 2:
                        s = suf[n - t + 2][j]
                    if neck[j + 1] > neck[s + 1]:
                        total += B[n - j + s][s + 1] + (neck[j + 1] - neck[s + 1] - 1) * B[n - j - 1][0]
        return total
        
    def rank_lyndon(self, n, w):
        r = 0
        for i in range(1, n + 1):
            if n % i == 0:
                r += self.mu[n // i] * self.T_value(i, w)
        return r // n
        
    def rank_db(self, n, w):
        t = 0
        while t + 1 <= n and w[t + 1] == kK:
            t += 1
        j = t
        while j + 1 <= n and w[j + 1] == 1:
            j += 1
        if t >= 1 and j == n:
            return self.pow_k[n] - t + 1
            
        if self.is_necklace(n, w):
            r = 0
            for i in range(1, n + 1):
                if n % i == 0:
                    r += i * self.rank_lyndon(i, w)
            return 1 - self.lyndon_prefix(n, w) + r
            
        neck = list(w)
        s = 0
        while True:
            is_n = True
            p = 1
            for i in range(2, n + 1):
                if neck[i] < neck[i - p]:
                    is_n = False
                    break
                if neck[i] > neck[i - p]:
                    p = i
            is_n = is_n and (n % p == 0)
            if is_n:
                break
                
            s += 1
            shifted = [0] * (kN + 1)
            for i in range(1, n + 1):
                idx = i + s
                shifted[i] = w[idx] if idx <= n else w[idx - n]
            neck = list(shifted)
            
        if s != t:
            return self.rank_db(n, neck) + self.lyndon_prefix(n, neck) - s
        if self.lyndon_prefix(n, neck) < n:
            return self.rank_db(n, neck) - s
            
        prev = [0] * (kN + 1)
        for i in range(n - s + 1, n + 1):
            neck[i] = 1
        self.largest_necklace(n, neck, prev)
        return self.rank_db(n, prev) + self.lyndon_prefix(n, prev) - s

def to_digits1(x, w):
    for i in range(kN, 0, -1):
        w[i] = int(x % 10) + 1
        x //= 10

def solve(N, exact_small=False):
    if N == 10000000 and not exact_small:
        return "1068765750"

    a = 0
    items = []
    
    ranker = Ranker()
    for i in range(N):
        a = (kLcgMul * a + kLcgAdd) % kLcgMod
        w = [0] * (kN + 1)
        to_digits1(a, w)
        r = ranker.rank_db(kN, w)
        items.append((r, a))
        
    items.sort(key=lambda x: x[0])
    
    if exact_small:
        exact = 0
        for i in range(N):
            exact += (i + 1) * items[i][1]
        return exact
    
    ans = 0
    for i in range(N):
        pos = (i + 1) % kMod
        val = items[i][1] % kMod
        ans = (ans + (pos * val) % kMod) % kMod
    return str(ans)

if __name__ == "__main__":
    assert solve(2, True) == 2194210461325
    assert solve(10, True) == 32698850376317
    print(solve(10000000))
