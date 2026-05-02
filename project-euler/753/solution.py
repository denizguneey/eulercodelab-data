import math

def solve():
    LIMIT = 6000000
    is_prime = bytearray(b'\x01' * LIMIT)
    is_prime[0] = is_prime[1] = 0
    for i in range(2, int(LIMIT**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, LIMIT, i): is_prime[j] = 0

    def isqrt(n):
        r = int(math.isqrt(n))
        while (r+1)*(r+1) <= n: r += 1
        while r*r > n: r -= 1
        return r

    twu = []
    u = 1
    while 27*u*u <= 4*LIMIT:
        twu.append(27*u*u); u += 1

    total = 0
    for p in range(2, LIMIT):
        if not is_prime[p]: continue
        if p == 3: total += 2; continue
        if p < 5 or p % 3 == 0: continue
        if p % 3 == 2:
            total += (p-1)*(p-2); continue
        target = 4*p; t_sel = 0
        for v in twu:
            if v > target: break
            rem = target - v
            t = isqrt(rem)
            if t*t == rem:
                t_sel = t if t%3 == 1 else -t; break
        total += (p-1)*(p - 8 + t_sel)

    return str(total)

if __name__ == '__main__':
    print(solve())
