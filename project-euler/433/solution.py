import math

def solve():
    n = 5000000
    limit = n // 5

    def isqrt(x):
        r = int(math.isqrt(x))
        while (r+1)*(r+1) <= x: r += 1
        while r*r > x: r -= 1
        return r

    # Build Mobius
    mu = [0]*(limit+1); mu[1] = 1
    lp = [0]*(limit+1); primes = []
    for i in range(2, limit+1):
        if lp[i] == 0:
            lp[i] = i; primes.append(i); mu[i] = -1
        for p in primes:
            if i*p > limit: break
            lp[i*p] = p
            if p == lp[i]: mu[i*p] = 0; break
            mu[i*p] = -mu[i]
    prefix_mu = [0]*(limit+1)
    for i in range(1, limit+1): prefix_mu[i] = prefix_mu[i-1] + mu[i]

    def floor_div(a, b):
        return a // b if a >= 0 else -((-a + b - 1) // b)

    def floor_sum_pair(p, q, m, s1, s2):
        r1 = r2 = 0; sign = 1
        while True:
            t = floor_div(m, q); m -= t*q
            r1 += sign*t*s1; r2 += sign*t*s2
            t = floor_div(p, q); p -= t*q
            r1 += sign*t*s1*(s1+1)//2; r2 += sign*t*s2*(s2+1)//2
            if p == 0: return r1, r2
            t = (p*s1 + m) // q; r1 += sign*s1*t; s1 = t
            t = (p*s2 + m) // q; r2 += sign*s2*t; s2 = t
            p, q = q, p; m = -m - 1; sign = -sign

    def calc_smart(val):
        mxy = isqrt(val); r1 = r2 = 0
        for x in range(2, mxy+1):
            for y in range(1, x):
                sp = val // (x + y)
                r1 += sp*(sp-1)//2
                s1 = val//x - sp
                s2 = max(0, mxy - sp) if sp <= mxy else 0
                b1, b2 = floor_sum_pair(-x, y, val - sp*x, s1, s2)
                r1 += b1
                if sp <= mxy:
                    r2 += sp*(sp-1)//2; r2 += b2
                else:
                    r2 += mxy*(mxy-1)//2
        return 2*r1 - r2

    def base_term(nn):
        m = nn // 2
        return (3*m - 2)*m if nn % 2 == 0 else 3*m*m + m

    # Build tasks
    tasks = []; l = 1
    while l <= limit:
        q = n // l; r = min(limit, n // q)
        ms = prefix_mu[r] - prefix_mu[l-1]
        if ms != 0 and q > 1: tasks.append((q, ms))
        l = r + 1

    result = base_term(n)
    for q, ms in tasks: result += 2 * ms * calc_smart(q)
    total = 2 * result + n * (n + 1) // 2
    return str(total)

if __name__ == '__main__':
    print(solve())
