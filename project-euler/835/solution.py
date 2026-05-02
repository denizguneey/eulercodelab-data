import math

def solve():
    MOD = 1234567891; exp10 = 10000000000

    def mod_pow(a, e, m=MOD):
        r = 1; a %= m
        while e > 0:
            if e & 1: r = r*a%m
            a = a*a%m; e >>= 1
        return r

    # Family I
    half = exp10 // 2
    s = mod_pow(10, half); inv2 = (MOD+1)//2; inv3 = mod_pow(3, MOD-2)
    q = s * inv2 % MOD
    part = q * ((q+1)%MOD) % MOD * ((4*q%MOD + MOD - 1)%MOD) % MOD * inv3 % MOD
    part = (part + MOD - 2) % MOD
    sumI = part

    # Family II: p_k = 6*p_{k-1} - p_{k-2}, matrix exponentiation
    def mat_mul(A, B):
        C = [[0]*3 for _ in range(3)]
        for i in range(3):
            for k in range(3):
                if A[i][k] == 0: continue
                for j in range(3): C[i][j] = (C[i][j] + A[i][k]*B[k][j]) % MOD
        return C
    def mat_pow(base, exp):
        res = [[1 if i==j else 0 for j in range(3)] for i in range(3)]
        while exp > 0:
            if exp & 1: res = mat_mul(res, base)
            base = mat_mul(base, base); exp >>= 1
        return res

    # Find K_max: p_k ~ alpha * lambda^k
    sqrt2 = math.sqrt(2); lam = 3 + 2*sqrt2
    p1, p2 = 12, 70
    alpha = (p2 - p1*(3-2*sqrt2)) / (lam*(lam-(3-2*sqrt2)))
    log10_lam = math.log10(lam); log10_alpha = math.log10(alpha)
    K = int((exp10 - log10_alpha) / log10_lam)
    while (K+1)*log10_lam + log10_alpha <= exp10: K += 1
    while K > 0 and K*log10_lam + log10_alpha > exp10: K -= 1

    if K <= 0: sumII = 0
    elif K == 1: sumII = 12
    else:
        A = [[6, MOD-1, 0], [1, 0, 0], [6, MOD-1, 1]]
        P = mat_pow(A, K-2); v = [70, 12, 82]
        sumII = sum(P[2][j]*v[j] for j in range(3)) % MOD

    ans = (sumI + sumII + MOD - 12) % MOD
    return str(ans)

if __name__ == '__main__':
    print(solve())
