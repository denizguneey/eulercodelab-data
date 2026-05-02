import math

def solve():
    # 10^10 = 2^10 * 5^10, so we compute for radius = 5^10 then shift by 2^10
    exp2 = 10
    exp5 = 10
    r = 5 ** exp5
    limit = 2 * r

    # Build SPF sieve
    spf = list(range(limit + 1))
    i = 2
    while i * i <= limit:
        if spf[i] == i:
            for j in range(i*i, limit+1, i):
                if spf[j] == j:
                    spf[j] = i
        i += 1

    bad = [0] * (limit + 1)
    e5 = [0] * (limit + 1)
    f1 = [1] * (limit + 1)

    for n in range(1, limit + 1):
        x = n
        is_bad = False
        exp_5 = 0
        mult = 1
        while x > 1:
            p = spf[x]
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            if p == 5:
                exp_5 = e
            elif p % 4 == 3:
                if e % 2 != 0:
                    is_bad = True
            elif p % 4 == 1:
                mult *= (e + 1)
        bad[n] = 1 if is_bad else 0
        e5[n] = exp_5
        f1[n] = mult

    total = 0
    for x in range(1, r):
        a = r - x
        b = r + x
        if bad[a] or bad[b]:
            continue
        ways = 4 * f1[a] * f1[b] * (e5[a] + e5[b] + 1)
        total += 6 * x * ways

    # x = r: contributes r_2(0)=1 => 6*r
    total += 6 * r
    total <<= exp2

    return str(total)

if __name__ == '__main__':
    print(solve())
