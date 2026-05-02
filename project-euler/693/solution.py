def solve():
    N = 3000000

    def g_value(x):
        if x < 2: return 0
        if x == 2: return 1
        # Initial active set after first step
        mod = x; seen = bytearray(mod); active = []
        limit = mod // 2
        for y in range(2, limit+1):
            sq = y*y % mod
            if sq > 1 and not seen[sq]:
                seen[sq] = 1; active.append(sq)
        length = 2; mod = x + 1
        while len(active) > 1:
            if len(active) >= 120000:
                nseen = bytearray(mod); nxt = []
                for a in active:
                    v = a*a % mod
                    if v > 1 and not nseen[v]: nseen[v] = 1; nxt.append(v)
            else:
                ns = set()
                for a in active:
                    v = a*a % mod
                    if v > 1: ns.add(v)
                nxt = list(ns)
            active = nxt; length += 1; mod += 1
            if not active: return length
        if not active: return length
        v = active[0]
        while v > 1: v = v*v % mod; length += 1; mod += 1
        return length

    import math
    def f_value(n):
        if n < 2: return 0
        pts = list(range(2, n+1, max(1, (n-2)//15)))
        if pts[-1] != n: pts.append(n)
        gpts = [g_value(x) for x in pts]
        cache = dict(zip(pts, gpts))
        best = max(gpts)
        import heapq
        pq = []
        for i in range(1, len(pts)):
            ub = gpts[i] + (pts[i]-pts[i-1])
            heapq.heappush(pq, (-ub, pts[i-1], pts[i], gpts[i]))
        while pq:
            neg_ub, left, right, gr = heapq.heappop(pq)
            if -neg_ub <= best: break
            if right - left <= 1: continue
            mid = (left+right)//2
            gm = cache.get(mid)
            if gm is None: gm = g_value(mid); cache[mid] = gm
            if gm > best: best = gm
            if mid-left > 1:
                ub_l = gm + (mid-left)
                if ub_l > best: heapq.heappush(pq, (-ub_l, left, mid, gm))
            if right-mid > 1:
                ub_r = gr + (right-mid)
                if ub_r > best: heapq.heappush(pq, (-ub_r, mid, right, gr))
        return best

    return str(f_value(N))

if __name__ == '__main__':
    print(solve())
