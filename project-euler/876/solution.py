import sys

def euclid_sum(a, b):
    if a < b:
        a, b = b, a
    total = 0
    while b != 0:
        total += a // b
        r = a % b
        a = b
        b = r
    return total

def compute_F_power(k, pow2, pow3, pow5):
    a = pow2[k] * pow3[k]
    b = pow2[k] * pow5[k]
    two_a = a * 2
    two_b = b * 2
    two_ab = (a + b) * 2

    N = pow2[2 * k + 2] * pow3[k] * pow5[k]

    total = 0

    for e2 in range(2 * k + 3):
        v2 = pow2[e2]
        for e3 in range(k + 1):
            v23 = v2 * pow3[e3]
            for e5 in range(k + 1):
                q = v23 * pow5[e5]
                p = N // q
                if q > p:
                    continue
                if (p + q) & 1:
                    continue

                s1 = euclid_sum(max(two_a, q), min(two_a, q))
                s2 = euclid_sum(max(two_b, q), min(two_b, q))
                f = min(s1, s2)

                total += f
                if p + q < two_ab:
                    total += f - 1

    return total

def solve():
    maxK = 18
    max_pow2 = 2 * maxK + 2
    
    pow2 = [1] * (max_pow2 + 1)
    for i in range(1, max_pow2 + 1):
        pow2[i] = pow2[i - 1] * 2

    pow3 = [1] * (maxK + 1)
    pow5 = [1] * (maxK + 1)
    for i in range(1, maxK + 1):
        pow3[i] = pow3[i - 1] * 3
        pow5[i] = pow5[i - 1] * 5

    total = 0
    for k in range(1, maxK + 1):
        total += compute_F_power(k, pow2, pow3, pow5)

    return str(total)

if __name__ == "__main__":
    print(solve())
