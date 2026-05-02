import math

def solve():
    LIMIT = 100_000_000_000

    def build_spf(limit):
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
        return spf

    def special_factor_count(n, spf):
        count = 0
        while n > 1:
            p = spf[n]
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            if p == 3:
                if e >= 2:
                    count += 1
            elif p % 3 == 1:
                count += 1
        return count

    # Sieve special (p ≡ 1 mod 3) primes
    PRIME_BOUND_DENOM = 15561  # 9*7*13*19
    upper = LIMIT // PRIME_BOUND_DENOM
    sp_sieve = bytearray(b'\x01' * (upper + 1))
    sp_sieve[0] = 0
    sp_sieve[1] = 0
    for p in range(2, math.isqrt(upper) + 1):
        if sp_sieve[p]:
            sp_sieve[p*p::p] = bytearray(len(sp_sieve[p*p::p]))
    special_primes = [p for p in range(7, upper + 1) if sp_sieve[p] and p % 3 == 1]

    INF = float('inf')
    n_sp = len(special_primes)
    min_prod = [[INF]*(n_sp + 1) for _ in range(5)]
    for i in range(n_sp + 1):
        min_prod[0][i] = 1
    for i in range(n_sp - 1, -1, -1):
        for r in range(1, 5):
            tail = min_prod[r-1][i+1]
            if tail == INF or special_primes[i] > LIMIT:
                min_prod[r][i] = INF
            else:
                min_prod[r][i] = special_primes[i] * tail

    # Build cofactor prefix sums
    MIN_PROD5 = 7 * 13 * 19 * 31 * 37
    MIN_PROD4 = 7 * 13 * 19 * 31
    max_cf1 = LIMIT // MIN_PROD5 if MIN_PROD5 <= LIMIT else 0
    max_cf2 = LIMIT // (9 * MIN_PROD4) if 9 * MIN_PROD4 <= LIMIT else 0
    max_cofactor = max(max_cf1, max_cf2)

    spf = build_spf(max_cofactor)
    valid = bytearray(max_cofactor + 1)
    valid[1] = 1
    for nn in range(2, max_cofactor + 1):
        p = spf[nn]
        valid[nn] = 1 if (valid[nn // p] and p % 3 == 2) else 0

    prefix = [0] * (max_cofactor + 2)
    for nn in range(1, max_cofactor + 1):
        prefix[nn] = prefix[nn - 1] + (nn if valid[nn] else 0)

    def sum_allowed(m):
        if m > max_cofactor:
            m = max_cofactor
        return prefix[m]

    def sum_allowed_opt3(m):
        if m > max_cofactor:
            m = max_cofactor
        return sum_allowed(m) + 3 * sum_allowed(m // 3)

    def dfs_without_9(start, remaining, product):
        if remaining == 0:
            cf_limit = LIMIT // product
            return product * sum_allowed_opt3(cf_limit)
        total = 0
        for i in range(start, n_sp):
            mr = min_prod[remaining - 1][i + 1]
            if mr == INF:
                break
            if product > LIMIT // mr:
                break
            mp = (LIMIT // product) // mr
            p = special_primes[i]
            if p > mp:
                break
            power = p
            while power <= mp:
                total += dfs_without_9(i + 1, remaining - 1, product * power)
                if power > mp // p:
                    break
                power *= p
        return total

    def dfs_with_9(start, remaining, product, sl):
        if remaining == 0:
            total = 0
            mtp = LIMIT // product
            tp = 9
            while tp <= mtp:
                cf_limit = LIMIT // (product * tp)
                total += product * tp * sum_allowed(cf_limit)
                if tp > mtp // 3:
                    break
                tp *= 3
            return total
        total = 0
        for i in range(start, n_sp):
            mr = min_prod[remaining - 1][i + 1]
            if mr == INF:
                break
            if product > sl // mr:
                break
            mp = (sl // product) // mr
            p = special_primes[i]
            if p > mp:
                break
            power = p
            while power <= mp:
                total += dfs_with_9(i + 1, remaining - 1, product * power, sl)
                if power > mp // p:
                    break
                power *= p
        return total

    case1 = 0
    for i in range(n_sp):
        mr = min_prod[4][i + 1]
        if mr == INF:
            break
        if special_primes[i] > LIMIT // mr:
            break
        p = special_primes[i]
        mp = LIMIT // mr
        power = p
        while power <= mp:
            case1 += dfs_without_9(i + 1, 4, power)
            if power > mp // p:
                break
            power *= p

    sl = LIMIT // 9
    case2 = 0
    for i in range(n_sp):
        mr = min_prod[3][i + 1]
        if mr == INF:
            break
        if special_primes[i] > sl // mr:
            break
        p = special_primes[i]
        mp = sl // mr
        power = p
        while power <= mp:
            case2 += dfs_with_9(i + 1, 3, power, sl)
            if power > mp // p:
                break
            power *= p

    return str(case1 + case2)

if __name__ == '__main__':
    print(solve())
