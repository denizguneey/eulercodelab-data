def solve():
    LIMIT = 10_000_000

    # Build SPF via linear sieve
    spf = [0] * (LIMIT + 1)
    primes = []
    for i in range(2, LIMIT + 1):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
        for p in primes:
            if i * p > LIMIT: break
            spf[i * p] = p
            if p == spf[i]: break

    def inv_mod(a, m):
        b, u, v = m, 1, 0
        while b:
            t = a // b
            a, b = b, a - t * b
            u, v = v, u - t * v
        return u % m

    ans = 0
    for n in range(2, LIMIT + 1):
        x = n
        k = 0
        pp = []
        while x > 1:
            p = spf[x]
            pe = 1
            while x % p == 0:
                x //= p
                pe *= p
            pp.append(pe)
            k += 1

        if k == 1:
            ans += 1
            continue

        full = 1 << k
        subset_prod = [0] * full
        subset_prod[0] = 1
        for mask in range(1, full):
            lsb = mask & -mask
            bit = lsb.bit_length() - 1
            subset_prod[mask] = subset_prod[mask ^ lsb] * pp[bit]

        best = 1
        for mask in range(1, full - 1):
            u = subset_prod[mask]
            v = n // u
            inv = inv_mod(u % v, v)
            a = (u * inv) % n
            if a > best:
                best = a

        ans += best

    return str(ans)

if __name__ == '__main__':
    print(solve())
