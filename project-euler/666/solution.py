def extinction_probability(k, m):
    n = k * m
    r = [0] * n
    r[0] = 306
    for i in range(1, n):
        x = r[i - 1]
        r[i] = (x * x) % 10007

    cnt = [[0] * 5 for _ in range(k)]
    for i in range(k):
        for j in range(m):
            q = r[i * m + j] % 5
            cnt[i][q] += 1

    p = [0.0] * k
    nxt = [0.0] * k

    max_iter = 1000000
    eps = 1e-15

    for iteration in range(max_iter):
        max_delta = 0.0

        for i in range(k):
            c = cnt[i]
            a = (2 * i) % k
            b = (i * i + 1) % k
            d = (i + 1) % k

            pi = p[i]
            pa = p[a]
            pb = p[b]
            pd = p[d]

            val = (c[0] +
                   c[1] * pi * pi +
                   c[2] * pa +
                   c[3] * pb * pb * pb +
                   c[4] * pi * pd) / m

            nxt[i] = val
            delta = abs(val - pi)
            if delta > max_delta:
                max_delta = delta

        # Swap references
        p, nxt = nxt, p
        
        if max_delta < eps:
            break

    return p[0]

def solve():
    ans = extinction_probability(500, 10)
    return "{:.8f}".format(ans)

if __name__ == '__main__':
    print(solve())
