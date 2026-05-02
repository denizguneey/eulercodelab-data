import math

def solve():
    MOD = 1000000007
    N = K = 10000000000

    def int_root(n, k):
        r = max(1, int(n ** (1.0/k)))
        while True:
            try:
                if (r+1)**k <= n: r += 1
                else: break
            except: break
        while r**k > n: r -= 1
        return r

    max_parts = 0
    p = 1
    while p <= N: max_parts += 1; p <<= 1
    max_parts -= 1

    memo = {}
    def count_nd(limit, min_f, parts):
        if parts == 0: return 1
        if parts == 1:
            return max(0, limit - min_f + 1) if limit >= min_f else 0
        key = (limit, min_f, parts)
        if key in memo: return memo[key]
        r = int_root(limit, parts)
        if r < min_f: memo[key] = 0; return 0
        total = 0
        for x in range(min_f, r + 1):
            total += count_nd(limit // x, x, parts - 1)
        memo[key] = total; return total

    counts = [0] * (max_parts + 1); counts[0] = 1
    for m in range(1, max_parts + 1):
        counts[m] = count_nd(N, 2, m)

    answer = K % MOD
    for m in range(1, max_parts + 1):
        if m > K: break
        ways = counts[m] % MOD
        mult = (K - m + 1) % MOD
        answer = (answer + ways * mult) % MOD

    return str(answer)

if __name__ == '__main__':
    print(solve())
