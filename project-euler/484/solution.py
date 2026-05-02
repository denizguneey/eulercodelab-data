import math

def solve():
    N = 5_000_000_000_000_000

    def isqrt(x): return math.isqrt(x)

    limit = isqrt(N)
    # Sieve primes up to sqrt(N)
    is_comp = bytearray(limit + 1)
    primes = []
    for i in range(2, limit + 1):
        if not is_comp[i]:
            primes.append(i)
            if i <= limit // i:
                for j in range(i*i, limit+1, i):
                    is_comp[j] = 1
    p2 = [p * p for p in primes]

    def dfs_alt(i0, L0):
        res = 0
        for i in range(i0, len(primes)):
            q = p2[i]
            L = L0 // q
            if L == 0: break
            p = primes[i]
            e = 1
            g = 1
            while L > 0:
                gp = g
                e += 1
                if e != 1:
                    if e == p:
                        g *= q
                        e = 0
                    else:
                        g *= p
                    c = g - gp
                    res += c * L
                    if L > q:
                        res += c * dfs_alt(i + 1, L)
                L //= p
        return res

    total = N + dfs_alt(0, N)
    total -= 1  # exclude n=1
    return str(total)

if __name__ == '__main__':
    print(solve())
