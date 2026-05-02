def solve():
    MOD = 987654321
    N = 10**18

    def mod_add(a, b): return (a + b) % MOD
    def mod_sub(a, b): return (a - b) % MOD
    def mod_mul(a, b): return a * b % MOD

    memoP = {}
    memoS = {}

    def P(n):
        if n <= 1: return 1
        if n in memoP: return memoP[n]
        m = n // 2
        res = 2 * (1 + m - P(m))
        memoP[n] = res
        return res

    def S(n):
        if n == 0: return 0
        if n == 1: return 1 % MOD
        if n in memoS: return memoS[n]
        m = n // 2
        Sm = S(m)
        if n & 1:
            term = mod_mul(2, mod_mul(m % MOD, (m + 3) % MOD))
            sub4 = mod_mul(4, Sm)
            res = mod_add(1, mod_sub(term, sub4))
        else:
            mm = m % MOD
            term2m2 = mod_mul(2, mod_mul(mm, mm))
            term4m = mod_mul(4, mm)
            base = mod_sub(mod_add(term2m2, term4m), 1)
            sub4 = mod_mul(4, Sm)
            add2P = mod_mul(2, P(m) % MOD)
            res = mod_add(mod_sub(base, sub4), add2P)
        memoS[n] = res
        return res

    import sys
    sys.setrecursionlimit(200)
    return str(S(N) % MOD)

if __name__ == '__main__':
    print(solve())
