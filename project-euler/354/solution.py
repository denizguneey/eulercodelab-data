import math

def solve():
    TARGET_L = 500_000_000_000

    def isqrt(n):
        return math.isqrt(n)

    def sieve_primes_mod1(limit):
        is_comp = bytearray(limit + 1)
        primes = []
        for i in range(2, limit + 1):
            if not is_comp[i]:
                primes.append(i)
                if i <= limit // i:
                    for j in range(i*i, limit+1, i):
                        is_comp[j] = 1
        return [p for p in primes if p % 3 == 1]

    n_limit = TARGET_L * TARGET_L // 3
    MIN_CORE = 2401 * 28561 * 361  # 7^4 * 13^4 * 19^2
    CORE_BOUND = 2401 * 28561      # 7^4 * 13^4

    if n_limit < MIN_CORE:
        return '0'

    prime_limit = isqrt(n_limit // CORE_BOUND)
    primes_m1 = sieve_primes_mod1(prime_limit)
    ps = len(primes_m1)

    def pp(base, exp):
        r = 1
        for _ in range(exp):
            if r > n_limit // base:
                return n_limit + 1
            r *= base
        return r

    pow2 = [pp(p, 2) for p in primes_m1]
    pow4 = [pp(p, 4) for p in primes_m1]
    pow14 = [(i, pp(p, 14)) for i, p in enumerate(primes_m1) if pp(p, 14) <= n_limit]
    pow24 = [(i, pp(p, 24)) for i, p in enumerate(primes_m1) if pp(p, 24) <= n_limit]
    pow74 = [(i, pp(p, 74)) for i, p in enumerate(primes_m1) if pp(p, 74) <= n_limit]

    max_s = isqrt(n_limit // MIN_CORE)

    # Build neutral multiplier prefix sums
    spf = list(range(max_s + 1))
    for i in range(2, max_s + 1):
        if spf[i] == i:
            if i <= max_s // i:
                for j in range(i*i, max_s+1, i):
                    if spf[j] == j:
                        spf[j] = i

    good = [0] * (max_s + 1)
    good[1] = 1
    for n in range(2, max_s + 1):
        p = spf[n]
        m = n // p
        good[n] = 1 if (p % 3 == 2 and good[m] == 1) else 0

    prefix = [0] * (max_s + 1)
    for n in range(1, max_s + 1):
        prefix[n] = prefix[n-1] + good[n]

    def count_mult(x):
        total = 0
        p3 = 1
        while p3 <= x:
            y = isqrt(x // p3)
            if y <= max_s:
                total += prefix[y]
            if p3 > x // 3:
                break
            p3 *= 3
        return total

    import bisect
    answer = 0

    # Pattern [74]
    for i, v in pow74:
        answer += count_mult(n_limit // v)

    # Pattern [24, 2]
    for i, v24 in pow24:
        b0 = n_limit // v24
        for j in range(i+1, ps):
            if pow2[j] > b0: break
            answer += count_mult(b0 // pow2[j])

    # Pattern [2, 24]
    for j, v24 in pow24:
        if j == 0: continue
        b0 = n_limit // v24
        for i in range(j):
            if pow2[i] > b0: break
            answer += count_mult(b0 // pow2[i])

    # Pattern [14, 4]
    for i, v14 in pow14:
        b0 = n_limit // v14
        for j in range(i+1, ps):
            if pow4[j] > b0: break
            answer += count_mult(b0 // pow4[j])

    # Pattern [4, 14]
    for j, v14 in pow14:
        if j == 0: continue
        b0 = n_limit // v14
        for i in range(j):
            if pow4[i] > b0: break
            answer += count_mult(b0 // pow4[i])

    # Pattern [4, 4, 2]
    i_end4 = 0
    for i in range(ps):
        if pow4[i] <= n_limit:
            i_end4 = i + 1
        else:
            break
    for i in range(i_end4):
        b0 = n_limit // pow4[i]
        for j in range(i+1, ps):
            if pow4[j] > b0: break
            b1 = b0 // pow4[j]
            for k in range(j+1, ps):
                if pow2[k] > b1: break
                answer += count_mult(b1 // pow2[k])

    # Pattern [4, 2, 4]
    for i in range(i_end4):
        b0 = n_limit // pow4[i]
        for j in range(i+1, ps):
            if pow2[j] > b0: break
            b1 = b0 // pow2[j]
            for k in range(j+1, ps):
                if pow4[k] > b1: break
                answer += count_mult(b1 // pow4[k])

    # Pattern [2, 4, 4]
    for i in range(i_end4 - 1 if i_end4 > 0 else 0):
        b0 = n_limit // pow2[i]
        for j in range(i+1, ps):
            if pow4[j] > b0: break
            b1 = b0 // pow4[j]
            for k in range(j+1, ps):
                if pow4[k] > b1: break
                answer += count_mult(b1 // pow4[k])

    return str(answer)

if __name__ == '__main__':
    print(solve())
