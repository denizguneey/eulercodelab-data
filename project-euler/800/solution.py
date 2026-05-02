import math

def solve():
    base = 800800
    exponent = 800800
    limit = float(exponent) * math.log(float(base))

    q_max = int(limit / math.log(2.0)) + 16
    sieve = bytearray([1]) * (q_max + 1)
    sieve[0] = sieve[1] = 0
    for p in range(2, int(q_max**0.5) + 1):
        if sieve[p]:
            for x in range(p*p, q_max+1, p):
                sieve[x] = 0
    primes = [i for i in range(2, q_max+1) if sieve[i]]
    logs = [math.log(float(p)) for p in primes]
    m = len(primes)

    ans = 0
    j = m - 1
    for i in range(m):
        if i >= j: break
        lp = logs[i]
        p = primes[i]
        while i < j:
            q = primes[j]
            lhs = float(q) * lp + float(p) * logs[j]
            if lhs <= limit + 1e-9:
                break
            j -= 1
        if j <= i: break
        ans += j - i

    return str(ans)

if __name__ == '__main__':
    print(solve())
