import math

def solve():
    threshold = 100

    def isqrt(n):
        r = int(math.isqrt(n))
        while (r+1)*(r+1) <= n: r += 1
        while r*r > n: r -= 1
        return r

    def prime_list(limit):
        comp = bytearray(limit+1); ps = []
        for i in range(2, limit+1):
            if not comp[i]:
                ps.append(i)
                if i*i <= limit:
                    for j in range(i*i, limit+1, i): comp[j] = 1
        return ps

    def sum2sq(p):
        for x in range(1, int(p**0.5)+1):
            y2 = p - x*x; y = isqrt(y2)
            if y*y == y2: return (x, y)
        return (0, 0)

    def gm(a, b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])
    def gconj(a): return (a[0], -a[1])

    primes = prime_list(400)
    gp = {2: (1,1)}
    for p in primes:
        if p == 2 or p % 4 == 3: continue
        gp[p] = sum2sq(p)

    def count_from_fac(factors):
        reps = [(1, 0)]
        for pr, exp in factors:
            base = gp[pr]
            pows = [(1, 0)]
            for i in range(exp): pows.append(gm(pows[-1], base))
            terms = [gm(pows[i], gconj(pows[exp-i])) for i in range(exp+1)]
            reps = [gm(r, t) for r in reps for t in terms]
        uniq = set()
        for x, y in reps:
            x, y = abs(x), abs(y)
            if x == 0 or y == 0: continue
            if x < y: x, y = y, x
            if x % 6 == 5 and y % 6 == 5: uniq.add((x, y))
        return len(uniq)

    for n in range(1, 10**9):
        k = 6*n - 1; value = k*k + 1
        factors = []
        v = value; ok = True
        for p in primes:
            if p > 400: break
            if v % p == 0:
                e = 0
                while v % p == 0: v //= p; e += 1
                factors.append((p, e))
                if p != 2 and p % 4 == 3: ok = False; break
                if p not in gp: gp[p] = sum2sq(p)
        if not ok: continue
        if v > 1: continue  # Only smooth numbers

        bound = 1
        for _, e in factors: bound *= (e+1)
        if bound // 2 <= threshold: continue

        ways = count_from_fac(factors)
        if ways > threshold:
            return str(n * (3*n - 1) // 2)

if __name__ == '__main__':
    print(solve())
