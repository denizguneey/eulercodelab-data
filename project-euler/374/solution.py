import math

def solve():
    MOD = 982451653
    LIMIT = 100_000_000_000_000

    def isqrt(n):
        return math.isqrt(n)

    def max_m_for_n(n):
        m = (isqrt(8*n + 9) - 3) // 2
        while (m+1)*(m+4)//2 <= n:
            m += 1
        while m > 0 and m*(m+3)//2 > n:
            m -= 1
        return m

    m_max = max_m_for_n(LIMIT)
    inv_limit = m_max + 3

    inv = [0] * (inv_limit + 1)
    inv[1] = 1
    for i in range(2, inv_limit + 1):
        inv[i] = (MOD - MOD // i * inv[MOD % i] % MOD) % MOD

    inv2 = (MOD + 1) // 2
    answer = 1  # n=1
    fact = 1
    harmonic = 0
    upto = 1

    for m in range(1, m_max + 1):
        target = m + 2
        while upto < target:
            upto += 1
            fact = fact * upto % MOD
            if upto >= 2:
                harmonic = (harmonic + inv[upto]) % MOD

        start = m * (m + 3) // 2
        end_full = (m + 1) * (m + 4) // 2 - 1
        ln = min(LIMIT, end_full) - start + 1

        mm = m % MOD
        base = mm * fact % MOD

        if ln <= m:
            d1 = m + 3 - ln
            d2 = m + 2
            partial_h = 0
            for d in range(d1, d2 + 1):
                partial_h = (partial_h + inv[d]) % MOD
            add = base * partial_h % MOD
        elif ln == m + 1:
            add = base * harmonic % MOD
        else:  # ln == m + 2
            add = base * harmonic % MOD
            fact_m3 = fact * (m + 3) % MOD
            extra = mm * fact_m3 % MOD * inv2 % MOD * inv[m + 2] % MOD
            add = (add + extra) % MOD

        answer = (answer + add) % MOD

    return str(answer)

if __name__ == '__main__':
    print(solve())
