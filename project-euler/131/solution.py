# Problem 131: Prime cube partnership
# Primes p < 10^6 where there exists n such that n^3 + n^2*p is a perfect cube.
# This simplifies to p = 3a^2 + 3a + 1 (difference of consecutive cubes).

def solve():
    limit = 1000000
    count = 0
    a = 1
    while True:
        p = 3*a*a + 3*a + 1
        if p >= limit: break
        # check primality
        if p > 1:
            is_p = True
            d = 2
            while d*d <= p:
                if p % d == 0: is_p = False; break
                d += 1
            if is_p: count += 1
        a += 1
    print(count)

solve()
