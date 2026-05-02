import math

def solve():
    MOD = 100_000_000
    N = 10**12

    def iroot3(n):
        x = round(n ** (1/3))
        while (x+1)**3 <= n: x += 1
        while x**3 > n: x -= 1
        return x

    def divisor_summatory(n, cache):
        if n <= 0: return 0
        if n in cache: return cache[n]
        res = 0
        k = 1
        while k <= n:
            q = n // k
            r = n // q
            res += q * (r - k + 1)
            k = r + 1
        cache[n] = res
        return res

    def sum_floor_products(n):
        if n < 2: return 0
        s = 0
        i = 2
        while i <= n:
            a = n // i
            b = n // (i - 1)
            next_a = n // a + 1
            next_b = n // b + 2
            nxt = min(next_a, next_b, n + 1)
            cnt = nxt - i
            s += cnt * a * b
            i = nxt
        return s

    def sum_double_floor(n, limit):
        total = 0
        for a in range(1, limit + 1):
            for b in range(1, limit + 1):
                total += n // (a * b)
        return total

    def triple_count(n):
        L = iroot3(n)
        cache = {}
        sum_a = 0
        a = 1
        while a <= L:
            q = n // a
            r = n // q
            if r > L: r = L
            cnt = r - a + 1
            sum_a += cnt * divisor_summatory(q, cache)
            a = r + 1
        sum_ab = sum_double_floor(n, L)
        return 3 * sum_a - 3 * sum_ab + L**3

    def compute_G(n):
        if n < 2: return 0
        cache = {}
        s_prod = sum_floor_products(n)
        d_n = divisor_summatory(n, cache)
        t_n = triple_count(n)
        return s_prod - t_n + d_n

    answer = compute_G(N) % MOD
    return str(answer)

if __name__ == '__main__':
    print(solve())
