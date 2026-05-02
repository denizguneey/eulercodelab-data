def solve():
    N = 3000000

    def popcount(x):
        c = 0
        while x: c += 1; x &= x - 1
        return c

    pow2 = [1 << i for i in range(25)]
    pow3 = [1]; 
    for _ in range(23): pow3.append(pow3[-1] * 3)

    U = []
    for n in range(1, N+1):
        b3 = popcount(3*n); b2 = popcount(2*n); b1 = popcount(n+1)
        U.append(pow2[b3] + pow3[b2] + b1)

    # Coordinate compress
    vals = sorted(set(U))
    val_idx = {v: i for i, v in enumerate(vals)}
    M = len(vals)

    # Fenwick tree
    bit = [0] * (M + 1)
    def bit_add(i, d):
        i += 1
        while i <= M: bit[i] += d; i += i & -i
    def bit_sum(i):
        s = 0
        while i > 0: s += bit[i]; i -= i & -i
        return s
    def bit_kth(k):
        idx = 0; bm = 1
        while bm * 2 <= M: bm <<= 1
        step = bm
        while step:
            nxt = idx + step
            if nxt <= M and bit[nxt] <= k:
                k -= bit[nxt]; idx = nxt
            step >>= 1
        return idx

    cnt = [0] * M
    best_score = 0; best_per = 0; ans = 0

    for n_idx in range(N):
        v = U[n_idx]; idx = val_idx[v]
        pos = bit_sum(idx) + cnt[idx]
        cnt[idx] += 1; bit_add(idx, 1)
        nn = n_idx + 1
        if nn >= 4:
            lo = max(0, pos - 3)
            hi = min(nn - 1, pos + 3)
            win = [vals[bit_kth(p)] for p in range(lo, hi + 1)]
            s_min = max(0, pos - 3)
            s_max = min(pos, nn - 4)
            for s in range(s_min, s_max + 1):
                off = s - lo
                if off + 3 >= len(win): continue
                a, b, c, d = win[off], win[off+1], win[off+2], win[off+3]
                if d >= a + b + c: continue
                ss = a+b+c+d
                sc = (ss-2*a)*(ss-2*b)*(ss-2*c)*(ss-2*d)
                per = ss
                if sc > best_score or (sc == best_score and per > best_per):
                    best_score = sc; best_per = per
            ans += best_per

    return str(ans)

if __name__ == '__main__':
    print(solve())
