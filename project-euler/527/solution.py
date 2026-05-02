import math

def harmonic_asymptotic(n):
    kGamma = 0.577215664901532860606512090082402431
    inv = 1.0 / float(n)
    inv2 = inv * inv
    inv4 = inv2 * inv2
    return math.log(n) + kGamma + 0.5 * inv - (1.0 / 12.0) * inv2 + (1.0 / 120.0) * inv4

def harmonic_number(n):
    if n <= 1000000:
        s = 0.0
        for k in range(1, n + 1):
            s += 1.0 / k
        return s
    return harmonic_asymptotic(n)

def expected_random_binary_search(n):
    Hn = harmonic_number(n)
    nn = float(n)
    return 2.0 * (nn + 1.0) / nn * Hn - 3.0

def expected_standard_binary_search(n):
    h = n.bit_length() - 1
    two_h1 = 1 << (h + 1)
    nn = float(n)
    return float(h + 1) - (float(two_h1) - float(h + 2)) / nn

def solve():
    n = 10000000000
    B = expected_standard_binary_search(n)
    R = expected_random_binary_search(n)
    ans = R - B
    return f"{ans:.8f}"

if __name__ == '__main__':
    print(solve())
