def solve():
    LIMIT = 20_000_000

    # Build SPF sieve
    spf = list(range(LIMIT + 1))
    for i in range(2, int(LIMIT**0.5) + 1):
        if spf[i] == i:
            for j in range(i*i, LIMIT+1, i):
                if spf[j] == j:
                    spf[j] = i

    def mod_inv(a, m):
        b, x0, x1 = m, 1, 0
        while b:
            q = a // b
            a, b = b, a - q * b
            x0, x1 = x1, x0 - q * x1
        return x0 % m

    def compute_I(n):
        target = n - 1
        sums = [target]
        best = 1

        nn = n
        while nn != 1:
            p = spf[nn]
            q = 1
            while nn % p == 0:
                nn //= p
                q *= p
            if q == 2:
                continue

            m = n // q
            inv = mod_inv(m % q, q)
            b = (m * inv) % n
            delta2 = (2 * b) % n

            delta_half = 0
            delta_half_plus_two = 0
            if q % 2 == 0 and q >= 8:
                half = q // 2
                delta_half = (half * b) % n
                delta_half_plus_two = ((half + 2) * b) % n

            current = list(sums)
            for base in current:
                s = (base + delta2) % n
                sums.append(s)
                if s > best and s < target: best = s

                if q % 2 == 0 and q >= 8:
                    s1 = (base + delta_half) % n
                    sums.append(s1)
                    if s1 > best and s1 < target: best = s1
                    s2 = (base + delta_half_plus_two) % n
                    sums.append(s2)
                    if s2 > best and s2 < target: best = s2

        return best

    total = sum(compute_I(n) for n in range(3, LIMIT + 1))
    return str(total)

if __name__ == '__main__':
    print(solve())
