import math

def solve():
    N = 100_000_000_000
    M = 100_000_000

    def sieve_primes(n):
        sieve = bytearray([1]) * (n + 1)
        sieve[0] = sieve[1] = 0
        for p in range(2, int(n**0.5) + 1):
            if sieve[p]:
                for q in range(p*p, n+1, p):
                    sieve[q] = 0
        return [i for i in range(2, n+1) if sieve[i]]

    def mod_pow(a, e, mod):
        r = 1 % mod
        x = a % mod
        while e > 0:
            if e & 1: r = r * x % mod
            x = x * x % mod
            e >>= 1
        return r

    def primitive_root_of_unity(p, d):
        if d == 1: return 1
        for a in range(2, p):
            h = mod_pow(a, (p-1)//d, p)
            z = 1
            ok = True
            for _ in range(1, d):
                z = z * h % p
                if z == 1:
                    ok = False
                    break
            if ok: return h

    primes = sieve_primes(M)
    total = 0
    for p in primes:
        d = math.gcd(15, p - 1)
        r = primitive_root_of_unity(p, d)
        h = p - 1
        for _ in range(d):
            h = h * r % p
            total += ((N + p - h) // p) * p

    return str(total)

if __name__ == '__main__':
    print(solve())
