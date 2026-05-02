def solve():
    N = 200000
    INF = 1 << 62

    def depth_int(m):
        if m <= 0:
            return -1
        return m.bit_length() - 1

    # Compute A(m)
    A = [0] * (N + 1)
    B = [0] * (N + 1)

    suf_min_val = {}
    suf_arg_val = {}
    built = set([0])

    def build_suf(d):
        lo = 1 << (d - 1)
        hi = (1 << d) - 1
        length = hi - lo + 1
        smv = [0] * length
        sav = [0] * length

        best = A[hi] - hi * d
        arg = hi
        smv[length - 1] = best
        sav[length - 1] = arg
        for i in range(length - 2, -1, -1):
            q = lo + i
            v = A[q] - q * d
            if v < best:
                best = v
                arg = q
            smv[i] = best
            sav[i] = arg

        suf_min_val[d] = smv
        suf_arg_val[d] = sav
        built.add(d)

    for m in range(2, N + 1):
        d = depth_int(m)
        if d >= 1 and d not in built:
            build_suf(d)
        if d == 0:
            A[m] = 0
            continue
        base = 1 << (d - 1)
        qLo = max(base, m - (1 << d))
        right_cost = m * d + suf_min_val[d][qLo - base]
        left_cost = INF
        p = m - base + 1
        if p <= (1 << d):
            left_cost = p + A[p - 1]
        A[m] = min(left_cost, right_cost)

    max_d = depth_int(N)
    for d in range(1, max_d + 1):
        if d not in built:
            build_suf(d)

    # Compute B(m)
    def B_cand(m, q):
        d = depth_int(m)
        p = m - q
        L = p - 1
        best = p * (d - 1) + B[q]
        Dl = depth_int(L)
        if Dl == d - 1:
            best = max(best, p + B[L])
        elif Dl == d - 2:
            best = max(best, p + A[L])
        return best

    for m in range(2, N + 1):
        d = depth_int(m)
        if d == 0:
            B[m] = 0
            continue
        base = 1 << (d - 1)
        p0 = m - base + 1
        leftA = INF
        if p0 <= (1 << d):
            leftA = p0 + A[p0 - 1]

        qLo = max(base, m - (1 << d))
        rightBestA = m * d + suf_min_val[d][qLo - base]

        if leftA == A[m]:
            L = p0 - 1
            R = m - p0
            bestB = max(p0 + B[L], p0 * (d - 1) + A[R])
            if rightBestA == A[m]:
                q = suf_arg_val[d][qLo - base]
                bestB = min(bestB, B_cand(m, q))
            B[m] = bestB
        else:
            q = suf_arg_val[d][qLo - base]
            B[m] = B_cand(m, q)

    # Build sparse table RMQ per band
    class BandRMQ:
        def __init__(self, d, start, end):
            self.d = d
            self.start = start
            self.end = end
            self.length = end - start + 1
            self.s1 = [A[start + i] - (start + i) * (d + 1) for i in range(self.length)]
            self.s2 = [B[start + i] - (start + i) * d for i in range(self.length)]
            lg = [0] * (self.length + 1)
            for i in range(2, self.length + 1):
                lg[i] = lg[i // 2] + 1
            K = lg[self.length] + 1
            st1 = [list(range(self.length))]
            st2 = [list(range(self.length))]
            for k in range(1, K):
                sp = 1 << (k - 1)
                lim = self.length - (1 << k) + 1
                row1 = [0] * lim
                row2 = [0] * lim
                for i in range(lim):
                    i1, i2 = st1[k-1][i], st1[k-1][i + sp]
                    row1[i] = i1 if self.s1[i1] <= self.s1[i2] else i2
                    j1, j2 = st2[k-1][i], st2[k-1][i + sp]
                    row2[i] = j1 if self.s2[j1] <= self.s2[j2] else j2
                st1.append(row1)
                st2.append(row2)
            self.st1, self.st2, self.lg = st1, st2, lg

        def rmq1(self, lA, rA):
            l, r = lA - self.start, rA - self.start
            L = r - l + 1; k = self.lg[L]
            i1, i2 = self.st1[k][l], self.st1[k][r - (1 << k) + 1]
            return self.start + (i1 if self.s1[i1] <= self.s1[i2] else i2)

        def rmq2(self, lA, rA):
            l, r = lA - self.start, rA - self.start
            L = r - l + 1; k = self.lg[L]
            i1, i2 = self.st2[k][l], self.st2[k][r - (1 << k) + 1]
            return self.start + (i1 if self.s2[i1] <= self.s2[i2] else i2)

    bands = {}
    for d in range(1, max_d + 1):
        s = 1 << d
        e = min((1 << (d + 1)) - 1, N)
        if s <= e:
            bands[d] = BandRMQ(d, s, e)

    # Compute C(n)
    C = [0] * (N + 1)
    total_sum = 0

    def obj(n, d, m):
        k = n - m
        L = k + C[k - 1]
        g1 = k * (d + 1) + A[m]
        g2 = k * d + B[m]
        return max(L, max(g1, g2))

    for n in range(2, N + 1):
        best = INF
        # d=0 band: m=1
        k = n - 1
        best = min(best, k + C[k - 1])

        maxDn = depth_int(n - 1)
        for d in range(1, maxDn + 1):
            mLo = 1 << d
            mHi = min((1 << (d + 1)) - 1, n - 1)
            if mLo > mHi:
                continue

            def rightCost(m):
                kk = n - m
                return max(kk * d + A[m], kk * (d - 1) + B[m])

            def P(m):
                kk = n - m
                return C[kk - 1] <= rightCost(m)

            def h(m):
                kk = n - m
                return kk + A[m] - B[m]

            if not P(mHi):
                for m in [mHi, mHi - 1]:
                    if mLo <= m <= mHi:
                        best = min(best, obj(n, d, m))
                continue

            if P(mLo):
                mP = mLo
            else:
                lo2, hi2 = mLo, mHi
                while lo2 < hi2:
                    mid = (lo2 + hi2) >> 1
                    if P(mid):
                        hi2 = mid
                    else:
                        lo2 = mid + 1
                mP = lo2
                for m in [mP - 1, mP]:
                    if mLo <= m <= mHi:
                        best = min(best, obj(n, d, m))

            subLo, subHi = mP, mHi
            for m in [subLo, subHi, subHi - 1, subHi - 2]:
                if subLo <= m <= subHi:
                    best = min(best, obj(n, d, m))

            if d in bands:
                hLo = h(subLo)
                hHi = h(subHi)
                band = bands[d]
                if hLo >= 0 and hHi >= 0:
                    mMin = band.rmq1(subLo, subHi)
                    for m in range(max(subLo, mMin - 2), min(subHi, mMin + 2) + 1):
                        best = min(best, obj(n, d, m))
                elif hLo <= 0 and hHi <= 0:
                    mMin = band.rmq2(subLo, subHi)
                    for m in range(max(subLo, mMin - 2), min(subHi, mMin + 2) + 1):
                        best = min(best, obj(n, d, m))
                else:
                    lo2, hi2 = subLo, subHi
                    while lo2 < hi2:
                        mid = (lo2 + hi2) >> 1
                        if h(mid) >= 0:
                            hi2 = mid
                        else:
                            lo2 = mid + 1
                    mQ = lo2
                    for m in range(max(subLo, mQ - 4), min(subHi, mQ + 4) + 1):
                        best = min(best, obj(n, d, m))
                    mMin1 = band.rmq1(subLo, subHi)
                    mMin2 = band.rmq2(subLo, subHi)
                    for mm in [mMin1, mMin2]:
                        for m in range(max(subLo, mm - 2), min(subHi, mm + 2) + 1):
                            best = min(best, obj(n, d, m))

        C[n] = best
        total_sum += best

    return str(total_sum)

if __name__ == '__main__':
    print(solve())
