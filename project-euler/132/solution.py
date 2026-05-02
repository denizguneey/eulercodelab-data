# Problem 132: Large repunit factors
# Sum of first 40 primes that are factors of R(10^9).

def solve():
    exp = 10**9
    found = 0
    total = 0
    p = 2
    while found < 40:
        if p not in (2, 5):
            # Check if R(exp) % p == 0, i.e. pow(10, exp, 9*p) == 1
            if pow(10, exp, 9 * p) == 1:
                found += 1
                total += p
        # next prime
        p += 1
        while True:
            is_p = p >= 2
            d = 2
            while d * d <= p:
                if p % d == 0: is_p = False; break
                d += 1
            if is_p: break
            p += 1
    print(total)

solve()
