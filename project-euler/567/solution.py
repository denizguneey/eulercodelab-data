import math

def harmonic_asymptotic(n):
    gamma = 0.577215664901532860606512090082402431
    nn = float(n)
    inv = 1.0 / nn
    inv2 = inv * inv
    return math.log(nn) + gamma + 0.5 * inv - (1.0 / 12.0) * inv2

def B_large(n):
    K = min(n - 1, 200)
    S = 0.0
    pow2 = 1.0
    for j in range(K + 1):
        S += pow2 / float(n - j)
        pow2 *= 0.5
    return S

def S_large(m):
    Hm = harmonic_asymptotic(m)
    Bm = B_large(m)
    two_ln2 = 2.0 * math.log(2.0)
    return 4.0 * Hm - 2.0 * Bm - two_ln2

def solve():
    m = 123456789
    ans = S_large(m)
    return f"{ans:.8f}"

if __name__ == '__main__':
    print(solve())
