import math

def solve():
    N = 100000000000000

    def isqrt(x):
        r = int(math.isqrt(x))
        while (r+1) <= x // (r+1): r += 1
        while r > x // r: r -= 1
        return r

    limit = isqrt(N)
    is_prime = bytearray(b'\x01'*(limit+1)); is_prime[0] = is_prime[1] = 0
    for i in range(2, int(limit**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, limit+1, i): is_prime[j] = 0
    primes = [i for i in range(2, limit+1) if is_prime[i]]

    cache = {}
    def alpha(n):
        if n <= 1: return n
        if n in cache: return cache[n]
        r = isqrt(n); s = 0; i = 1
        while i <= r:
            q = n // i; j = min(r, n // q)
            s += q * (j - i + 1); i = j + 1
        ans = 2 * s - r * r
        cache[n] = ans; return ans

    def dfs(a, i):
        if a > N: return 0
        res = alpha(N // a)
        for j in range(i + 1, len(primes)):
            p = primes[j]
            if a > N // (p * p): break
            pp = p * p; w = 1
            while a <= N // pp:
                res += w * dfs(a * pp, j)
                if pp > N // p: break
                pp *= p; w <<= 1
        return res

    return str(dfs(1, -1))

if __name__ == '__main__':
    print(solve())
