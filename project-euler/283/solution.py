import math

def solve():
    k_limit = 1000
    n_max = 4 * (2 * k_limit) ** 2

    # Build smallest prime factor
    spf = list(range(n_max + 1))
    spf[0] = 0
    if n_max >= 1:
        spf[1] = 1
    for i in range(2, math.isqrt(n_max) + 1):
        if spf[i] == i:
            for j in range(i*i, n_max + 1, i):
                if spf[j] == j:
                    spf[j] = i

    def factorize(n):
        factors = []
        while n > 1:
            p = spf[n]
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            factors.append((p, e))
        return factors

    def merge_factors(a, b):
        result = []
        i = j = 0
        while i < len(a) or j < len(b):
            if j == len(b) or (i < len(a) and a[i][0] < b[j][0]):
                result.append(a[i]); i += 1
            elif i == len(a) or b[j][0] < a[i][0]:
                result.append(b[j]); j += 1
            else:
                result.append((a[i][0], a[i][1] + b[j][1])); i += 1; j += 1
        return result

    def gen_divisors(factors):
        divs = [1]
        for p, e in factors:
            base = len(divs)
            mul = 1
            for _ in range(e):
                mul *= p
                for j in range(base):
                    divs.append(divs[j] * mul)
        return divs

    total = 0
    for k in range(1, k_limit + 1):
        r = 2 * k
        n = r * r
        factors_n = factorize(n)

        x_max = int(math.sqrt(3 * n))
        for x in range(1, x_max + 1):
            m = x * x + n
            factors_m = factorize(m)
            factors_all = merge_factors(factors_n, factors_m)
            divs = gen_divisors(factors_all)

            M = n * m
            for u in divs:
                if u * u > M:
                    continue
                v = M // u
                if (u + n) % x != 0 or (v + n) % x != 0:
                    continue
                y = (u + n) // x
                if y < x:
                    continue
                z = (v + n) // x
                total += 2 * (x + y + z)

    return str(total)

if __name__ == '__main__':
    print(solve())
