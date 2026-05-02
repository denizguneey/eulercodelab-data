def mod_pow(base, exp, mod):
    return pow(base, exp, mod)

def is_prime(n):
    if n < 2:
        return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if n == p:
            return True
        if n % p == 0:
            return False

    d = n - 1
    s = 0
    while (d & 1) == 0:
        d >>= 1
        s += 1

    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        if a % n == 0:
            continue
        x = mod_pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        witness = True
        for _ in range(1, s):
            x = (x * x) % n
            if x == n - 1:
                witness = False
                break
        if witness:
            return False
    return True

def prime_prefix():
    return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

def generate_admissible(primes, idx, current, limit, out):
    if idx >= len(primes):
        return
    p = primes[idx]
    value = current
    while value <= (limit - 1) // p:
        value *= p
        out.add(value)
        generate_admissible(primes, idx + 1, value, limit, out)

def pseudo_fortunate(n):
    m = 3
    while True:
        if is_prime(n + m):
            return m
        m += 2

def solve(limit=1000000000):
    admissible = set()
    primes = prime_prefix()
    generate_admissible(primes, 0, 1, limit, admissible)

    pseudo_values = set()
    for n in admissible:
        pseudo_values.add(pseudo_fortunate(n))

    return str(sum(pseudo_values))

if __name__ == '__main__':
    print(solve())
