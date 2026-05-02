def solve():
    N = 100_000_000

    def primes_up_to(n):
        if n < 2: return []
        half = n // 2
        is_comp = bytearray(half + 1)
        r = int(n**0.5)
        for i in range(1, half + 1):
            p = 2 * i + 1
            if p > r: break
            if is_comp[i]: continue
            start = (p * p - 1) // 2
            for j in range(start, half + 1, p):
                is_comp[j] = 1
        primes = [2]
        for i in range(1, half + 1):
            if not is_comp[i]: primes.append(2 * i + 1)
        return primes

    def vp_fact(n, p):
        s = 0
        while n:
            n //= p
            s += n
        return s

    def min_m(p, exp):
        lo, hi = 1, p * exp
        while lo < hi:
            mid = (lo + hi) // 2
            if vp_fact(mid, p) >= exp: hi = mid
            else: lo = mid + 1
        return lo

    s = [0] * (N + 1)
    primes = primes_up_to(N)

    for p in primes:
        for k in range(p, N + 1, p):
            if s[k] < p: s[k] = p
        q = p * p
        exp = 2
        while q <= N:
            m = min_m(p, exp)
            for k in range(q, N + 1, q):
                if s[k] < m: s[k] = m
            if q > N // p: break
            q *= p
            exp += 1

    return str(sum(s[i] for i in range(2, N + 1)))

if __name__ == '__main__':
    print(solve())
