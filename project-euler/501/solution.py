import math

def solve():
    N = 10**12

    def isqrt(x): return math.isqrt(x)
    def icbrt(x):
        r = round(x ** (1/3))
        while (r+1)**3 <= x: r += 1
        while r**3 > x: r -= 1
        return r

    def iroot7(n):
        r = round(n ** (1/7))
        while (r+1)**7 <= n: r += 1
        while r**7 > n: r -= 1
        return r

    v = isqrt(N)
    # Sieve primes up to v
    sieve = bytearray([1]) * (v + 1)
    sieve[0] = sieve[1] = 0
    for p in range(2, isqrt(v) + 1):
        if sieve[p]:
            for q in range(p*p, v+1, p):
                sieve[q] = 0
    primes = [i for i in range(2, v+1) if sieve[i]]

    # Lucy pi tables
    smalls = list(range(v + 1))  # smalls[i] = i - 1 for i >= 1
    for i in range(v + 1):
        smalls[i] = i - 1
    larges = [0] * (v + 1)
    for i in range(1, v + 1):
        larges[i] = N // i - 1

    for p in primes:
        if p * p > N: break
        p_cnt = smalls[p - 1]
        q = p * p
        end = min(v, N // q)
        for i in range(1, end + 1):
            d = i * p
            if d <= v:
                larges[i] -= larges[d] - p_cnt
            else:
                larges[i] -= smalls[N // d] - p_cnt
        i = v
        while i >= q:
            smalls[i] -= smalls[i // p] - p_cnt
            if i == q: break
            i -= 1

    # Count numbers with exactly 8 divisors
    ans = 0
    cbrt_n = icbrt(N)
    pi_cbrt = smalls[cbrt_n]

    # Case 1: p*q*r (three distinct primes)
    for pi_idx in range(pi_cbrt):
        p = primes[pi_idx]
        if p**3 >= N: break
        m = N // p
        q_lim = smalls[isqrt(m)]
        for pj_idx in range(pi_idx + 1, q_lim):
            q = primes[pj_idx]
            r = m // q
            pi_r = smalls[r] if r <= v else larges[p * q]
            ans += pi_r - smalls[q]

    # Case 2: p^3 * q
    for pi_idx in range(pi_cbrt):
        p = primes[pi_idx]
        p3 = p**3
        r = N // p3
        if r <= 1: break
        ans += smalls[r] if r <= v else larges[p3]

    # Case 3: p^7 (subtract overcounting)
    root4 = isqrt(isqrt(N))
    ans -= smalls[root4]

    # Case 4: p^7 (add back)
    ans += smalls[iroot7(N)]

    return str(ans)

if __name__ == '__main__':
    print(solve())
