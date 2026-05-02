import math

def solve():
    def mod_pow(base, exp, mod):
        r = 1 % mod; a = base % mod
        while exp > 0:
            if exp & 1: r = r * a % mod
            a = a * a % mod
            exp >>= 1
        return r

    def is_prime(n):
        if n < 2: return False
        for p in [2,3,5,7,11,13,17,19,23,29,31,37]:
            if n == p: return True
            if n % p == 0: return False
        d = n - 1; s = 0
        while d % 2 == 0: d >>= 1; s += 1
        for a in [2,325,9375,28178,450775,9780504,1795265022]:
            if a % n == 0: continue
            x = mod_pow(a, d, n)
            if x == 1 or x == n - 1: continue
            comp = True
            for _ in range(1, s):
                x = x * x % n
                if x == n - 1: comp = False; break
            if comp: return False
        return True

    def rev_digits(x):
        r = 0
        while x > 0:
            r = r * 10 + x % 10
            x //= 10
        return r

    def is_palindrome(x): return x == rev_digits(x)

    need = 50
    limit = 1 << 16
    while True:
        sieve = bytearray([1]) * (limit + 1)
        sieve[0] = sieve[1] = 0
        for p in range(2, int(limit**0.5) + 1):
            if sieve[p]:
                for q in range(p*p, limit+1, p):
                    sieve[q] = 0
        primes = [i for i in range(2, limit+1) if sieve[i]]
        vals = []
        for p in primes:
            sq = p * p
            if is_palindrome(sq): continue
            rev = rev_digits(sq)
            r = math.isqrt(rev)
            if r * r == rev and is_prime(r):
                vals.append(sq)
                if len(vals) >= need: break
        if len(vals) >= need:
            return str(sum(vals[:need]))
        limit <<= 1

if __name__ == '__main__':
    print(solve())
