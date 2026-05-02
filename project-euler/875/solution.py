def solve():
    LIMIT = 12345678; MOD = 1001961001

    def q_prime_power(p, e):
        if e == 0: return 1
        if p == 2:
            q = 128 % MOD; add = 2048 % MOD
            for _ in range(2, e+1):
                q = (q * 128 + add) % MOD; add = add * 16 % MOD
            return q
        pm = p % MOD; p2 = pm*pm%MOD; p3 = p2*pm%MOD; p4 = p2*p2%MOD; p7 = p4*p3%MOD
        coeff = (pm + MOD - 1) % MOD
        q = 1; term = p3
        for _ in range(1, e+1):
            q = (q * p7 + coeff * term) % MOD; term = term * p4 % MOD
        return q

    spf = list(range(LIMIT+1))
    primes = []
    for i in range(2, LIMIT+1):
        if spf[i] == i: primes.append(i)
        for p in primes:
            if i*p > LIMIT: break
            spf[i*p] = p
            if p == spf[i]: break

    s = 1
    for i in range(2, LIMIT+1):
        x = i; qn = 1
        while x > 1:
            p = spf[x]; e = 0
            while x > 1 and spf[x] == p: x //= p; e += 1
            qn = qn * q_prime_power(p, e) % MOD
        s = (s + qn) % MOD

    return str(s)

if __name__ == '__main__':
    print(solve())
