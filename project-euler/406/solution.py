import math

def capacity_with_budget(c, a, b, cap):
    imax = int(c / a)
    jmax = int(c / b)
    cols = jmax + 2

    dp = [0] * ((imax + 2) * cols)
    def at(i, j):
        return i * cols + j

    eps = 1e-16 * (1.0 + c)
    for i in range(imax, -1, -1):
        ai = i * a
        for j in range(jmax, -1, -1):
            if ai + j * b <= c + eps:
                v = 1 + dp[at(i + 1, j)] + dp[at(i, j + 1)]
                if v > cap:
                    v = cap
                dp[at(i, j)] = v

    return dp[at(0, 0)]

def C_value(n, a, b):
    lo = 0.0
    hi = 1.0
    while capacity_with_budget(hi, a, b, n) < n:
        hi *= 2.0

    for _ in range(90):
        mid = (lo + hi) / 2.0
        if capacity_with_budget(mid, a, b, n) >= n:
            hi = mid
        else:
            lo = mid

    return hi

def solve():
    n = 1000000000000
    fib = [0] * 31
    fib[1] = 1
    fib[2] = 1
    for k in range(3, 31):
        fib[k] = fib[k - 1] + fib[k - 2]

    ans = 0.0
    for k in range(1, 31):
        a = math.sqrt(k)
        b = math.sqrt(fib[k])
        ans += C_value(n, a, b)
        
    return "{:.8f}".format(ans)

if __name__ == '__main__':
    print(solve())
