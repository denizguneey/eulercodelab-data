MOD18 = 1000000000000000000

def tonelli_shanks(n, p):
    if n == 0: return 0
    if p == 2: return n
    if pow(n, (p - 1) // 2, p) != 1: return 0
    if p % 4 == 3: return pow(n, (p + 1) // 4, p)

    q = p - 1
    s = 0
    while (q & 1) == 0:
        q >>= 1
        s += 1

    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1

    m = s
    c = pow(z, q, p)
    t = pow(n, q, p)
    r = pow(n, (q + 1) // 2, p)

    while t != 1:
        tt = t
        i = 0
        while tt != 1:
            tt = (tt * tt) % p
            i += 1
        
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i

    return r

def sieve_primes(n):
    composite = bytearray(n + 1)
    primes = []
    for i in range(2, n + 1):
        if not composite[i]:
            primes.append(i)
        for p in primes:
            v = p * i
            if v > n: break
            composite[v] = 1
            if i % p == 0: break
    return primes

def solve_case(kmax):
    limit = 2 * kmax
    primes = sieve_primes(limit)

    rem = [0] * (kmax + 1)
    last_small = [1] * (kmax + 1)
    for k in range(1, kmax + 1):
        rem[k] = 4 * k * k + 1

    for p in primes:
        if p == 2 or (p & 3) != 1: continue

        root = tonelli_shanks(p - 1, p)
        if root == 0: continue

        inv2 = (p + 1) // 2
        k1 = (root * inv2) % p
        k2 = 0 if k1 == 0 else p - k1

        def process_residue(residue):
            start = residue
            if start <= 0: start += p
            for k in range(start, kmax + 1, p):
                v = rem[k]
                if v % p != 0: continue
                while v % p == 0:
                    v //= p
                rem[k] = v
                last_small[k] = p

        process_residue(k1)
        if k2 != k1: process_residue(k2)

    ans = 0
    for k in range(1, kmax + 1):
        tail = rem[k]
        lpf = last_small[k]
        if tail > lpf: lpf = tail
        ans = (ans + lpf) % MOD18

    return "{:018d}".format(ans)

def solve():
    ans_str = solve_case(10000000)
    return ans_str.lstrip('0') or '0'

if __name__ == '__main__':
    print(solve())
