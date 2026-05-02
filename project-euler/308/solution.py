import math

def solve():
    target_index = 10001

    def estimate_upper(n):
        if n < 6:
            return 15
        nd = float(n)
        return int(math.ceil(nd * (math.log(nd) + math.log(math.log(nd))) + 32))

    def build_sieve(limit):
        spf = list(range(limit + 1))
        primes = []
        spf[0] = 0
        if limit >= 1:
            spf[1] = 1
        for i in range(2, limit + 1):
            if spf[i] == i:
                primes.append(i)
            for p in primes:
                if p * i > limit or p > spf[i]:
                    break
                spf[p * i] = p
        return primes, spf

    limit = estimate_upper(target_index)
    primes, spf = build_sieve(limit)
    while len(primes) < target_index:
        limit *= 2
        primes, spf = build_sieve(limit)

    prime_target = primes[target_index - 1]

    def floor_sum_upto(n, r):
        if r == 0:
            return 0
        r = min(r, n)
        s = 0
        left = 1
        while left <= r:
            q = n // left
            right = min(n // q, r)
            s += q * (right - left + 1)
            left = right + 1
        return s

    def floor_sum_range(n, l, r):
        if l > r or r == 0:
            return 0
        return floor_sum_upto(n, r) - floor_sum_upto(n, l - 1)

    def candidate_delta(n, spf_n):
        max_pd = n // spf_n
        ndc = (n - max_pd - 1) if n > max_pd + 1 else 0
        ndfs = floor_sum_range(n, max_pd + 1, n - 1)
        setup = 2 * n - 1
        ndt = (6 * n + 2) * ndc + 2 * ndfs
        terminal = 5 * n + max_pd + 2 * (n // max_pd) + 2
        return setup + ndt + terminal

    def prime_hit_offset(pc):
        ndfs = floor_sum_range(pc, 2, pc - 1)
        setup = 2 * pc - 1
        ndt = (6 * pc + 2) * (pc - 2) + 2 * ndfs
        pb = 6 * pc + 2
        return setup + ndt + pb

    start_step = 2
    found = 0
    for n in range(2, prime_target + 1):
        spf_n = spf[n]
        is_p = (spf_n == n)
        if is_p:
            hit_step = start_step + prime_hit_offset(n)
            found += 1
            if found == target_index:
                return str(hit_step)
        start_step += candidate_delta(n, spf_n)

    return str(start_step)

if __name__ == '__main__':
    print(solve())
