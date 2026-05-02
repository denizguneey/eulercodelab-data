import math

def solve():
    MOD = 1000000000
    N = 10000000000000000

    def iroot4(n):
        if n == 0: return 0
        x = int(n ** 0.25)
        while (x+1)**4 <= n: x += 1
        while x**4 > n: x -= 1
        return x

    total = 0

    # Case 1: p,q odd coprime, p<q
    qmax = iroot4(2*N)
    for q in range(1, qmax+1, 2):
        q4 = q**4
        if q4 > 2*N: continue
        lim = 2*N - q4
        pmax = iroot4(lim)
        if pmax >= q: pmax = q - 1
        if pmax % 2 == 0:
            if pmax == 0: continue
            pmax -= 1
        for p in range(1, pmax+1, 2):
            if math.gcd(p, q) != 1: continue
            p4 = p**4
            z = (p4 + q4) // 2
            if z > N: continue
            x = (q4 - p4) // 8
            y = p * q
            if y > N: continue
            total = (total + (x + y + z) % MOD) % MOD

    # Case 2: r, s coprime, s odd
    smax = iroot4(N // 4)
    for s in range(1, smax+1, 2):
        s4 = s**4
        if s4 > N // 4: break
        rem = N // 4 - s4
        rmax = iroot4(rem // 4)
        for r in range(1, rmax+1):
            if math.gcd(r, s) != 1: continue
            r4 = r**4
            z = 4*(s4 + 4*r4)
            if z > N: continue
            a = 4*r4
            x = abs(s4 - a)
            y = 4*r*s
            if y > N: continue
            total = (total + (x + y + z) % MOD) % MOD

    return str(total % MOD)

if __name__ == '__main__':
    print(solve())
