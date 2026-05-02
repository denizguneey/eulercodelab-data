class MertensPrefix:
    def __init__(self, lim):
        self.limit = lim
        self.pref_mu = [0] * (lim + 1)
        
        mu = [0] * (lim + 1)
        primes = []
        composite = [False] * (lim + 1)
        
        mu[1] = 1
        for i in range(2, lim + 1):
            if not composite[i]:
                primes.append(i)
                mu[i] = -1
            for p in primes:
                v = i * p
                if v > lim:
                    break
                composite[v] = True
                if i % p == 0:
                    mu[v] = 0
                    break
                mu[v] = -mu[i]
                
        for i in range(1, lim + 1):
            self.pref_mu[i] = self.pref_mu[i - 1] + mu[i]
            
        self.memo_mu = {}
        self.memo_odd_mu = {}

    def mu_prefix(self, n):
        if n <= self.limit:
            return self.pref_mu[n]
        if n in self.memo_mu:
            return self.memo_mu[n]

        ans = 1
        l = 2
        while l <= n:
            q = n // l
            r = n // q
            ans -= (r - l + 1) * self.mu_prefix(q)
            l = r + 1

        self.memo_mu[n] = ans
        return ans

    def odd_mu_prefix(self, n):
        if n <= 0:
            return 0
        if n in self.memo_odd_mu:
            return self.memo_odd_mu[n]

        ans = 0
        cur = n
        while cur > 0:
            ans += self.mu_prefix(cur)
            cur >>= 1

        self.memo_odd_mu[n] = ans
        return ans

def sum_totients(n, mp):
    s = 0
    l = 1
    while l <= n:
        q = n // l
        r = n // q
        mu_seg = mp.mu_prefix(r) - mp.mu_prefix(l - 1)
        s += mu_seg * q * q
        l = r + 1
    return (s + 1) // 2

def f_odd_floor_sum(m):
    k = (m + 1) // 2
    p = k // 2
    if k % 2 == 1:
        return p * p
    return p * (p - 1)

def solve_fast(n):
    sieve_limit = 2000000
    mp = MertensPrefix(sieve_limit)

    total = sum_totients(n, mp) - 1

    losing_half = 0
    l = 1
    while l <= n:
        q = n // l
        r = n // q
        odd_mu_seg = mp.odd_mu_prefix(r) - mp.odd_mu_prefix(l - 1)
        losing_half += odd_mu_seg * f_odd_floor_sum(q)
        l = r + 1

    losing = 2 * losing_half
    return total - losing

def solve():
    return str(solve_fast(10**9))

if __name__ == "__main__":
    print(solve())
