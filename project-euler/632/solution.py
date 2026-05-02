import math

def solve():
    MOD = 1000000007
    LIM = 100000000
    N = 10000000000000000

    # Sieve primes
    half = LIM // 2 + 1
    comp = bytearray(half)
    primes = [2]
    for i in range(3, int(LIM**0.5)+1, 2):
        if not comp[i//2]:
            for j in range(i*i, LIM+1, 2*i): comp[j//2] = 1
    for i in range(3, LIM+1, 2):
        if not comp[i//2]: primes.append(i)

    omega = bytearray(LIM+1)
    sqfree = bytearray(b'\x01'*(LIM+1)); sqfree[0] = 0
    for p in primes:
        for m in range(p, LIM+1, p):
            if omega[m] < 255: omega[m] += 1
        p2 = p*p
        if p2 <= LIM:
            for m in range(p2, LIM+1, p2): sqfree[m] = 0

    def isqrt(x):
        r = int(math.isqrt(x))
        while (r+1)*(r+1) <= x: r += 1
        while r*r > x: r -= 1
        return r

    def compute_A():
        limit = isqrt(N)
        A = [0]*10; i = 1
        while i <= limit:
            q = N // (i*i)
            r = isqrt(N // q)
            if r > limit: r = limit
            while r+1 <= limit and N // ((r+1)*(r+1)) == q: r += 1
            while r > limit or N // (r*r) != q: r -= 1
            for d in range(i, r+1):
                if not sqfree[d]: continue
                w = omega[d]
                if w < 10: A[w] += q
            i = r + 1
        return A

    binom = [[0]*10 for _ in range(10)]
    for n in range(10):
        binom[n][0] = binom[n][n] = 1
        for k in range(1, n): binom[n][k] = binom[n-1][k-1] + binom[n-1][k]

    A = compute_A()
    C = [0]*10
    for k in range(10):
        s = 0
        for r in range(k, 10):
            s += A[r] * binom[r][k] * (1 if (r-k) % 2 == 0 else -1)
        C[k] = s

    ans = 1
    for x in C:
        if x == 0: continue
        ans = ans * (x % MOD) % MOD
    return str(ans)

if __name__ == '__main__':
    print(solve())
