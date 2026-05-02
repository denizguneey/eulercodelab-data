import sys
sys.setrecursionlimit(100000)

def solve():
    LIMIT = 100_000_000_000_000

    def pow_mod(base, exp, mod):
        result = 1
        base %= mod
        while exp > 0:
            if exp & 1:
                result = result * base % mod
            base = base * base % mod
            exp >>= 1
        return result

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
        while d % 2 == 0:
            d //= 2
            s += 1
        for a in [2, 3, 5, 7, 11, 13, 17]:
            if a >= n:
                continue
            x = pow_mod(a, d, n)
            if x == 1 or x == n - 1:
                continue
            witness = True
            for _ in range(1, s):
                x = x * x % n
                if x == n - 1:
                    witness = False
                    break
            if witness:
                return False
        return True

    harshad_limit = (LIMIT - 1) // 10
    total = 0

    def dfs(n, digit_sum):
        nonlocal total
        if n >= 10 and n % digit_sum == 0:
            q = n // digit_sum
            if is_prime(q):
                for d in [1, 3, 7, 9]:
                    cand = n * 10 + d
                    if cand < LIMIT and is_prime(cand):
                        total += cand
        if n > harshad_limit // 10:
            return
        for d in range(10):
            nxt = n * 10 + d
            ns = digit_sum + d
            if ns != 0 and nxt % ns == 0:
                dfs(nxt, ns)

    for d in range(1, 10):
        dfs(d, d)

    return str(total)

if __name__ == '__main__':
    print(solve())
