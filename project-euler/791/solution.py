import math

def solve():
    MOD = 433494437
    n = 100000000
    R = 8 * n

    def isqrt(x):
        if x <= 0: return 0
        r = int(math.isqrt(x))
        while (r+1)*(r+1) <= x: r += 1
        while r*r > x: r -= 1
        return r

    def ceil_sqrt(x):
        if x <= 0: return 0
        r = isqrt(x)
        return r if r*r >= x else r+1

    def sum_interval(L, H, N0):
        if L % 2 == 0: L += 1
        if H % 2 == 0: H -= 1
        if L > H: return 0
        cnt = (H - L) // 2 + 1
        t = cnt - 1
        si = cnt * t // 2
        si2 = t * cnt * (2*t+1) // 6
        sC = cnt * L + 2 * si
        sC2 = cnt * L * L + 4 * L * si + 4 * si2
        sn = cnt * N0 + sC2 + 2 * sC
        ss = sn // 2
        return ss % MOD

    A_max = isqrt(R + 3) - 2
    if A_max < 1: return '0'
    if A_max % 2 == 0: A_max -= 1

    ans = 0
    for A in range(1, A_max + 1, 2):
        A2 = A * A
        D = R - A2 - 4*A - 1
        if D < 0: continue
        B_max = isqrt(D) - 2
        if B_max < -1: continue
        if B_max > A: B_max = A

        for B in range(-1, B_max + 1, 2):
            B2 = B * B
            L = R - A2 - B2 - 4*A - 4*B - 5
            if L < 0: continue
            C_max = isqrt(L)
            C_low = max(-C_max, -B - 2)
            C_high = min(C_max, B)
            if C_low > C_high: continue

            Lmin = 11 - A2 - B2
            N0 = A2 + B2 + 2*A + 2*B + 3

            if Lmin <= 0:
                ans = (ans + sum_interval(C_low, C_high, N0)) % MOD
            else:
                cmin = ceil_sqrt(Lmin)
                if cmin % 2 == 0: cmin += 1
                nh = min(C_high, -cmin)
                if C_low <= nh:
                    ans = (ans + sum_interval(C_low, nh, N0)) % MOD
                pl = max(C_low, cmin)
                if pl <= C_high:
                    ans = (ans + sum_interval(pl, C_high, N0)) % MOD

    return str(ans)

if __name__ == '__main__':
    print(solve())
