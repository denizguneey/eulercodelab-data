def solve():
    MOD = 1000000007

    fact = [1] * 51
    for i in range(1, 51): fact[i] = (fact[i - 1] * i) % MOD
    ifact = [1] * 51
    ifact[50] = pow(fact[50], MOD - 2, MOD)
    for i in range(50, 0, -1): ifact[i - 1] = (ifact[i] * i) % MOD

    def binom_small(n, k):
        if k < 0 or k > n: return 0
        return fact[n] * ifact[k] * ifact[n - k] % MOD

    def C(a, b, q):
        if a < 0 or b < 0: return 0
        if a == 0 or b == 0: return 1
        if q == 1: return binom_small(a + b, a)

        k = min(a, b)
        m = a + b - k
        qm = pow(q, m, MOD)
        
        denom = 1
        numer = 1
        qj = 1
        for j in range(1, k + 1):
            qj = (qj * q) % MOD
            denom = (denom * (1 - qj)) % MOD
            numer = (numer * (1 - (qm * qj) % MOD)) % MOD
            
        return (numer * pow(denom, MOD - 2, MOD)) % MOD

    ans = 0
    ten = 1
    for k in range(1, 8):
        ten *= 10
        n = ten + k
        ans = (ans + C(n, n, k)) % MOD
        
    return str((ans % MOD + MOD) % MOD)

if __name__ == '__main__':
    print(solve())
