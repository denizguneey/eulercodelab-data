import math

def solve():
    N = 10**14
    MOD = 1_000_000_007

    root = math.isqrt(N)

    j2 = [i * i for i in range(root + 1)]

    is_comp = bytearray(root + 1)
    for p in range(2, root + 1):
        if is_comp[p]: continue
        p2 = p * p
        for m in range(p, root + 1, p):
            is_comp[m] = 1
            v = j2[m]
            j2[m] = (v // p2) * (p2 - 1)

    answer = 0
    for m in range(1, root + 1):
        m2 = m * m
        count = N // m2
        answer = (answer + j2[m] % MOD * (count % MOD)) % MOD

    return str(answer)

if __name__ == '__main__':
    print(solve())
