import math

def solve():
    N = 10**16; KMOD = 10**9

    def isqrt(n):
        x = int(n**0.5)
        while (x+1)*(x+1) <= n: x += 1
        while x*x > n: x -= 1
        return x

    def max_r(nl):
        rhs = 2*nl*nl; lo = 0; hi = int(nl**0.5)+10
        while 13*hi**4 <= rhs: hi *= 2
        while lo+1 < hi:
            mid = (lo+hi)//2
            if 13*mid**4 <= rhs: lo = mid
            else: hi = mid
        return lo

    rl = max_r(N); ml = isqrt(rl)
    total = 0
    for m in range(1, ml+1):
        for n in range(0, m):
            if (m-n)%2 == 0: continue
            if math.gcd(m, n) != 1: continue
            r = m*m + n*n
            if r > rl: continue
            u = m*m - n*n; v = 2*m*n
            cands = [
                (abs(3*u-2*v), abs(2*u+3*v)),
                (abs(3*u+2*v), abs(2*u-3*v)),
            ]
            seen = set()
            for p, q in cands:
                if p == 0 or q == 0: continue
                if p < q: p, q = q, p
                if (p, q) in seen: continue
                seen.add((p, q))
                if math.gcd(p, q) != 1: continue
                x = q*r; y = p*r; z = p*q
                if x > N or y > N or z > N: continue
                total += x + y + z

    return str(total % KMOD).zfill(9)

if __name__ == '__main__':
    print(solve())
