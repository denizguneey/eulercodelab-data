def solve():
    TARGET = 47547

    def divisor_count_square(n):
        result = 1
        e = 0
        while n % 2 == 0:
            n //= 2
            e += 1
        if e > 0:
            result *= (2*e + 1)
        p = 3
        while p * p <= n:
            if n % p == 0:
                e = 0
                while n % p == 0:
                    n //= p
                    e += 1
                result *= (2*e + 1)
            p += 2
        if n > 1:
            result *= 3
        return result

    def collect_factorizations(remaining, min_factor):
        if remaining == 1:
            return [[]]
        result = []
        f = min_factor
        while f <= remaining:
            if remaining % f == 0:
                for sub in collect_factorizations(remaining // f, f):
                    result.append([f] + sub)
            f += 2
        return result

    ODD_PRIMES = [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73]

    def build_number(two_exp, exponents):
        exponents = sorted(exponents, reverse=True)
        val = 1 << two_exp if two_exp > 0 else 1
        for i, e in enumerate(exponents):
            val *= ODD_PRIMES[i] ** e
        return val

    product_target = 2 * TARGET + 1
    best = float('inf')

    # Odd catheti
    for factors in collect_factorizations(product_target, 3):
        exps = [(f - 1) // 2 for f in factors]
        cand = build_number(0, exps)
        if cand < best:
            best = cand

    # Even catheti
    for factor in range(1, product_target + 1, 2):
        if product_target % factor != 0:
            continue
        remaining = product_target // factor
        two_exp = (factor + 1) // 2
        facs = collect_factorizations(remaining, 3)
        if remaining == 1:
            facs = [[]]
        for odd_factors in facs:
            exps = [(f - 1) // 2 for f in odd_factors]
            cand = build_number(two_exp, exps)
            if cand < best:
                best = cand

    return str(best)

if __name__ == '__main__':
    print(solve())
