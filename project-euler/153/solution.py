import math

def sigma_prefix(n, memo):
    if n in memo:
        return memo[n]
    s = 0
    l = 1
    while l <= n:
        q = n // l
        r = n // q
        interval_sum = (l + r) * (r - l + 1) // 2
        s += q * interval_sum
        l = r + 1
    memo[n] = s
    return s

def solve():
    limit = 100000000
    memo = {}
    answer = sigma_prefix(limit, memo)
    a = 1
    while a * a <= limit:
        aa = a * a
        bmax = math.isqrt(limit - aa)
        for b in range(1, bmax + 1):
            if math.gcd(a, b) != 1:
                continue
            norm = aa + b * b
            answer += 2 * a * sigma_prefix(limit // norm, memo)
        a += 1
    return str(answer)

if __name__ == '__main__':
    print(solve())
