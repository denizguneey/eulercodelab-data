def solve():
    N = 10**15
    DMAX = 12
    CMAX = 9 * DMAX
    P = 1_000_000
    DS6_MAX = 54
    RMAX = DS6_MAX + CMAX

    def digit_sum(x):
        s = 0
        while x:
            s += x % 10
            x //= 10
        return s

    # Build ds6: digit sum for 0..P-1
    ds6 = [0] * P
    for i in range(1, P):
        ds6[i] = ds6[i // 10] + i % 10

    # Build tables: for each carry c, steps/rem to next overflow
    steps_tab = [[0]*(RMAX+1) for _ in range(CMAX+1)]
    rem_tab = [[0]*(RMAX+1) for _ in range(CMAX+1)]

    for c in range(CMAX + 1):
        st = [0] * P
        rm = [0] * P
        for i in range(P - 1, -1, -1):
            y = i + ds6[i] + c
            if y >= P:
                st[i] = 1
                rm[i] = y - P
            else:
                st[i] = st[y] + 1
                rm[i] = rm[y]
        for x in range(RMAX + 1):
            steps_tab[c][x] = st[x]
            rem_tab[c][x] = rm[x]

    # Transpose compose logic
    def make_single(c):
        nxt = list(rem_tab[c][:RMAX+1])
        cost = list(steps_tab[c][:RMAX+1])
        return (nxt, cost)

    def compose(a, b):
        nxt_a, cost_a = a
        nxt_b, cost_b = b
        nxt = [0]*(RMAX+1)
        cost = [0]*(RMAX+1)
        for r in range(RMAX+1):
            mid = nxt_a[r]
            nxt[r] = nxt_b[mid]
            cost[r] = cost_a[r] + cost_b[mid]
        return (nxt, cost)

    def identity():
        return (list(range(RMAX+1)), [0]*(RMAX+1))

    pow10 = [1]
    for d in range(1, DMAX+1):
        pow10.append(pow10[-1] * 10)

    block = [[None]*(CMAX+1) for _ in range(DMAX+1)]
    for ps in range(CMAX+1):
        block[0][ps] = make_single(ps)

    for d in range(1, DMAX+1):
        for ps in range(CMAX - 9*d + 1):
            tr = block[d-1][ps]
            for dig in range(1, 10):
                tr = compose(tr, block[d-1][ps+dig])
            block[d][ps] = tr

    def range_trans(l, r):
        res = identity()
        cur = l
        while cur < r:
            best_d = 0
            for d in range(DMAX, -1, -1):
                p = pow10[d]
                if cur % p == 0 and cur + p <= r:
                    best_d = d
                    break
            p = pow10[best_d]
            hi = cur // p
            ps = digit_sum(hi)
            res = compose(res, block[best_d][ps])
            cur += p
        return res

    if N <= 1: return str(1)

    remaining = N - 1
    H = 0
    low = 1

    lo_c, hi_c = 0, 1
    while True:
        tr = range_trans(H, H + hi_c)
        cost = tr[1][low]
        if cost > remaining: break
        lo_c = hi_c
        hi_c <<= 1

    while lo_c + 1 < hi_c:
        mid = lo_c + (hi_c - lo_c) // 2
        tr = range_trans(H, H + mid)
        cost = tr[1][low]
        if cost <= remaining: lo_c = mid
        else: hi_c = mid

    tr = range_trans(H, H + lo_c)
    used = tr[1][low]
    low_after = tr[0][low]
    H += lo_c
    remaining -= used
    low = low_after

    c = digit_sum(H)
    for _ in range(remaining):
        low += ds6[low] + c

    return str(H * P + low)

if __name__ == '__main__':
    print(solve())
