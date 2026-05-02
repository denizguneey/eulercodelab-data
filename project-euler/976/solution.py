import sys

MOD = 1234567891

def power(base, exp):
    return pow(base, exp, MOD)

class Comb:
    def __init__(self, maxn):
        self.maxn = maxn
        self.fact = [1] * (maxn + 1)
        
        for i in range(1, maxn + 1):
            self.fact[i] = (self.fact[i - 1] * i) % MOD
            
        self.invfact = [1] * (maxn + 1)
        self.invfact[maxn] = power(self.fact[maxn], MOD - 2)
        
        for i in range(maxn, 0, -1):
            self.invfact[i - 1] = (self.invfact[i] * i) % MOD
            
    def nCk(self, n, k):
        if k < 0 or k > n:
            return 0
        return (self.fact[n] * self.invfact[k] % MOD) * self.invfact[n - k] % MOD

def solve_N_eq_K_div4(N):
    if N % 4 != 0:
        print("[FATAL] This solver expects N % 4 == 0", file=sys.stderr)
        sys.exit(1)
        
    No = N // 2
    Na = N // 4
    maxFac = 2 * N
    
    C = Comb(maxFac)
    inv2 = (MOD + 1) // 2
    
    total_even = 0
    for m in range(No + 1):
        k = 2 * m
        n = N + k - 1
        total_even += C.nCk(n, k)
    total_even %= MOD
        
    L1_raw = 0
    for r in range(Na + 1):
        a = C.nCk(No, 2 * r)
        b = C.nCk(3 * No - r, No - r)
        L1_raw += a * b
    L1_raw %= MOD
    L1 = (inv2 * L1_raw) % MOD
    
    L2 = (inv2 * C.nCk(5 * Na, No)) % MOD
    
    lost_even = (L1 + L2) % MOD
    
    Wodd_raw = 0
    for r in range(Na):
        a = C.nCk(No, 2 * r + 1)
        b = C.nCk(3 * No - 1 - r, No - 1 - r)
        Wodd_raw += a * b
    Wodd_raw %= MOD
    win_odd = (inv2 * Wodd_raw) % MOD
    
    ans = (total_even - lost_even + win_odd) % MOD
    if ans < 0: ans += MOD
    return ans

def solve():
    return str(solve_N_eq_K_div4(10000000))

if __name__ == "__main__":
    print(solve())
