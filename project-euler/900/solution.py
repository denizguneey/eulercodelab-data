MOD = 900497239

def mod_mul(a, b):
    return (a * b) % MOD

def mod_pow(base, exp):
    return pow(base, exp, MOD)

def mod_inv(a):
    return pow(a, MOD - 2, MOD)

def compute_S_closed(N):
    inv3 = mod_inv(3)
    inv7 = mod_inv(7)

    pow4N = mod_pow(4, N)
    sumA = (pow4N - 1 + MOD) % MOD
    sumA = mod_mul(sumA, inv3)

    sumC = (mod_pow(2, N + 1) - 2) % MOD
    if sumC < 0:
        sumC += MOD

    K = N // 2
    pow8K = mod_pow(8, K)
    geo = mod_mul((pow8K - 1 + MOD) % MOD, inv7)
    sumB = mod_mul(3, geo)
    if N % 2 == 1:
        sumB = (sumB + pow8K) % MOD

    ans = (sumA + sumB - sumC) % MOD
    if ans < 0:
        ans += MOD
    return ans

def solve():
    return str(compute_S_closed(10000))

if __name__ == "__main__":
    print(solve())
