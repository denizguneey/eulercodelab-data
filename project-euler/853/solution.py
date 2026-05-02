def fib_pair(n, mod):
    if n == 0:
        return (0, 1 % mod)
    a, b = fib_pair(n >> 1, mod)
    c = (a * ((2 * b - a) % mod)) % mod
    d = (a * a + b * b) % mod
    if (n & 1) == 0:
        return (c, d)
    return (d, (c + d) % mod)

def divisors_of(n):
    divs = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            divs.append(d)
            if d * d != n:
                divs.append(n // d)
        d += 1
    divs.sort()
    return divs

def has_period(mod, period, proper_divs):
    a, b = fib_pair(period, mod)
    if a != 0 or b != 1 % mod:
        return False
    for d in proper_divs:
        qa, qb = fib_pair(d, mod)
        if qa == 0 and qb == 1 % mod:
            return False
    return True

def solve():
    limit = 1000000000
    period = 120
    proper_divs = [d for d in divisors_of(period) if d < period]

    fac = [
        (2, 5), (3, 2), (5, 1), (7, 1), (11, 1), (23, 1), (31, 1),
        (41, 1), (61, 1), (241, 1), (2161, 1), (2521, 1), (20641, 1)
    ]

    divisors = [1]
    for p, e in fac:
        next_divs = []
        pe = 1
        for i in range(e + 1):
            for d in divisors:
                v = d * pe
                if v < limit:
                    next_divs.append(v)
            pe *= p
        divisors = next_divs

    ans = 0
    for n in divisors:
        if n < 2:
            continue
        if has_period(n, period, proper_divs):
            ans += n

    return str(ans)

if __name__ == "__main__":
    print(solve())
