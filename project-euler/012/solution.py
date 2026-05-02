def divisor_count(n):
    if n == 1:
        return 1
    count = 1
    exp = 0
    while n % 2 == 0:
        n //= 2
        exp += 1
    if exp > 0:
        count *= (exp + 1)
    p = 3
    while p * p <= n:
        exp = 0
        while n % p == 0:
            n //= p
            exp += 1
        if exp > 0:
            count *= (exp + 1)
        p += 2
    if n > 1:
        count *= 2
    return count

def solve(min_divisors=500):
    n = 1
    while True:
        a, b = n, n + 1
        if a % 2 == 0:
            a //= 2
        else:
            b //= 2
        if divisor_count(a) * divisor_count(b) > min_divisors:
            return n * (n + 1) // 2
        n += 1

if __name__ == "__main__":
    assert solve(5) == 28, "Checkpoint failed for divisors>5"
    print(solve())
