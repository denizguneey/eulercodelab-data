import math
import sys

sys.setrecursionlimit(2000)

MOD = 1000000007
INV2 = 500000004

class PhiSummatory:
    def __init__(self, limit):
        self.limit = limit
        self.primes = []
        lp = [0] * (limit + 1)
        self.phi = [0] * (limit + 1)
        self.pref = [0] * (limit + 1)
        
        self.phi[1] = 1
        for i in range(2, limit + 1):
            if lp[i] == 0:
                lp[i] = i
                self.primes.append(i)
                self.phi[i] = i - 1
            for p in self.primes:
                if p > lp[i] or i * p > limit: break
                lp[i * p] = p
                if p == lp[i]:
                    self.phi[i * p] = self.phi[i] * p
                    break
                self.phi[i * p] = self.phi[i] * (p - 1)
                
        for i in range(1, limit + 1):
            self.pref[i] = (self.pref[i - 1] + self.phi[i]) % MOD
            
        self.memo = {}

    def sum_phi(self, n):
        if n <= self.limit: return self.pref[n]
        if n in self.memo: return self.memo[n]

        nn = n % MOD
        res = (nn * ((n + 1) % MOD)) % MOD
        res = (res * INV2) % MOD

        l = 2
        while l <= n:
            q = n // l
            r = n // q
            cnt = (r - l + 1) % MOD
            res = (res - cnt * self.sum_phi(q)) % MOD
            l = r + 1

        res = (res + MOD) % MOD
        self.memo[n] = res
        return res

def solve_impl(n, ph):
    ans = 0
    m = n // 2
    while m >= 2:
        add_val = (ph.sum_phi(m) - 1) % MOD
        ans = (ans + add_val) % MOD
        m //= 2
    return ans

def solve():
    ph = PhiSummatory(5000000)
    ans = solve_impl(100000000000, ph)
    return str(ans)

if __name__ == '__main__':
    print(solve())
