import math
import bisect

def solve():
    pi = math.pi
    sinv = [math.sin(pi * d / 180.0) for d in range(181)]

    g = [[0.0] * 181 for _ in range(181)]
    for n in range(2, 179):
        for k in range(1, n):
            g[n][k] = sinv[n - k] / sinv[k]

    ratio_list = [[] for _ in range(181)]
    for U in range(2, 179):
        V = 180 - U
        vec = []
        for c in range(1, U):
            gU = g[U][c]
            for a in range(1, V):
                ratio = gU / g[V][a]
                vec.append((ratio, a, c))
        vec.sort()
        ratio_list[U] = vec

    unique = set()
    search_eps = 1e-10
    verify_eps = 1e-12

    def canonical(seq):
        pairs = [(seq[0], seq[1]), (seq[2], seq[3]), (seq[4], seq[5]), (seq[6], seq[7])]
        best = None
        def consider(ps, rot):
            nonlocal best
            s = []
            for i in range(4):
                p = ps[(rot + i) & 3]
                s.extend(p)
            s = tuple(s)
            if best is None or s < best:
                best = s
        for r in range(4):
            consider(pairs, r)
        ref = [(pairs[0][1], pairs[0][0]), (pairs[3][1], pairs[3][0]),
               (pairs[2][1], pairs[2][0]), (pairs[1][1], pairs[1][0])]
        for r in range(4):
            consider(ref, r)
        return best

    for p_val in range(1, 179):
        for q_val in range(1, 179 - p_val):
            U = p_val + q_val
            V = 180 - U
            vec = ratio_list[U]
            if not vec:
                continue
            vals = [v[0] for v in vec]
            sinp = sinv[p_val]
            sinq = sinv[q_val]
            for r in range(1, V):
                s = V - r
                K = (sinp * sinv[r]) / (sinq * sinv[s])
                lo = K - search_eps
                hi = K + search_eps
                i1 = bisect.bisect_left(vals, lo)
                i2 = bisect.bisect_right(vals, hi)
                for idx in range(i1, i2):
                    ratio, a, c_val = vec[idx]
                    left = sinq * sinv[s] * sinv[U - c_val] * sinv[a]
                    right = sinp * sinv[r] * sinv[c_val] * sinv[V - a]
                    diff = abs(left - right)
                    scale = max(1.0, abs(left))
                    if diff > verify_eps * scale:
                        continue
                    seq = (a, p_val, q_val, r, s, c_val, U - c_val, V - a)
                    unique.add(canonical(seq))

    return str(len(unique))

if __name__ == '__main__':
    print(solve())
