from collections import deque

def solve():
    u, k = 100000000, 100000

    # Divisor count sieve via SPF
    d = [0] * (u + 1)
    lp = [0] * (u + 1)
    exp = [0] * (u + 1)
    primes = []
    d[1] = 1
    for i in range(2, u + 1):
        minp = lp[i]
        if minp == 0:
            primes.append(i); d[i] = 2; exp[i] = 1; minp = i
        for p in primes:
            if p > minp: break
            x = i * p
            if x > u: break
            lp[x] = p
            if p == minp:
                e = exp[i] + 1; exp[x] = e
                d[x] = d[i] // (exp[i] + 1) * (e + 1)
                break
            exp[x] = 1; d[x] = d[i] * 2

    dq = deque(); total = 0
    for i in range(1, u + 1):
        while dq and d[dq[-1]] <= d[i]: dq.pop()
        dq.append(i)
        while dq and dq[0] <= i - k: dq.popleft()
        if i >= k: total += d[dq[0]]

    return str(total)

if __name__ == '__main__':
    print(solve())
