MOD = 1000000007

def mod_pow(a, e):
    return pow(a, e, MOD)

class Comb:
    def __init__(self, n):
        self.fact = [1] * (n + 1)
        self.ifact = [1] * (n + 1)
        for i in range(1, n + 1):
            self.fact[i] = (self.fact[i - 1] * i) % MOD
        self.ifact[n] = mod_pow(self.fact[n], MOD - 2)
        for i in range(n, 0, -1):
            self.ifact[i - 1] = (self.ifact[i] * i) % MOD
            
    def C(self, n, k):
        if k < 0 or k > n: return 0
        return (self.fact[n] * self.ifact[k] % MOD) * self.ifact[n - k] % MOD

def F30(n, cb):
    ans = 0
    ans = (ans + cb.C(n + 10, 10)) % MOD
    if n >= 1:
        ans = (ans + 19 * cb.C(n + 9, 10)) % MOD
    if n >= 2:
        ans = (ans + 33 * cb.C(n + 8, 10)) % MOD
    if n >= 3:
        ans = (ans + 6 * cb.C(n + 7, 10)) % MOD
    return ans

def solve():
    N = 10001
    cb = Comb(N + 10)
    return str(F30(N, cb))

if __name__ == '__main__':
    print(solve())
