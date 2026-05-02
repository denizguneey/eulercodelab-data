def solve():
    limit = 300000

    def primes_up_to(n):
        is_comp = bytearray(n + 1)
        primes = []
        for i in range(2, n+1):
            if not is_comp[i]:
                primes.append(i)
                if i <= n // i:
                    for j in range(i*i, n+1, i): is_comp[j] = 1
        return primes

    def ext_gcd(a, b):
        if b == 0: return a, 1, 0
        g, x1, y1 = ext_gcd(b, a % b)
        return g, y1, x1 - (a // b) * y1

    def mod_inv(a, p):
        g, x, _ = ext_gcd(a, p)
        return x % p

    primes = primes_up_to(limit)
    m = len(primes)
    xmod = [1] * m  # A_1 = 1
    mmod = [0] * m
    for j in range(m):
        mmod[j] = 2 % primes[j]  # M_1 = 2

    hit = [False] * m
    for i in range(1, m + 1):
        for j in range(i, m):
            if not hit[j] and xmod[j] == 0: hit[j] = True
        if i == m: break
        p = primes[i]
        rhs = (i + 1) % p
        xp, mp = xmod[i], mmod[i]
        inv_mp = mod_inv(mp, p)
        diff = (rhs - xp) % p
        t = diff * inv_mp % p
        for j in range(i, m):
            q = primes[j]
            add = mmod[j] * t % q
            xmod[j] = (xmod[j] + add) % q
            mmod[j] = mmod[j] * p % q

    return str(sum(primes[j] for j in range(m) if hit[j]))

if __name__ == '__main__':
    print(solve())
