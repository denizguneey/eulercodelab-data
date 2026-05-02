import math
from itertools import combinations

DIRS = 4
DR = [-1, 1, 0, 0]
DC = [0, 0, -1, 1]

def build_binom():
    c = [[0]*8 for _ in range(31)]
    for n in range(31):
        c[n][0] = 1
        for k in range(1, 8):
            c[n][k] = 0 if k > n else c[n-1][k-1] + c[n-1][k]
    return c

kBinom = build_binom()

def rank_combination(a):
    rank = 0
    for i, val in enumerate(a):
        rank += kBinom[val][i + 1]
    return rank

class Shape:
    def __init__(self, h, w, cells):
        self.h = h
        self.w = w
        max_r = max(r for r, c in cells)
        max_c = max(c for r, c in cells)
        self.rows = h - max_r
        self.cols = w - max_c
        total = self.rows * self.cols
        self.masks = [0] * total
        self.next = [[-1]*DIRS for _ in range(total)]

        for ar in range(self.rows):
            for ac in range(self.cols):
                idx = self.idx_of(ar, ac)
                mask = 0
                for dr, dc in cells:
                    rr = ar + dr
                    cc = ac + dc
                    mask |= (1 << (rr * w + cc))
                self.masks[idx] = mask

                for d in range(DIRS):
                    nr = ar + DR[d]
                    nc = ac + DC[d]
                    if 0 <= nr < self.rows and 0 <= nc < self.cols:
                        self.next[idx][d] = self.idx_of(nr, nc)

    def idx_of(self, r, c):
        return r * self.cols + c

def encode_target(red, green, yellow, pink, blue, cyan):
    kR = 190
    kG = 190
    kY = 276
    kP = 593775
    kB = 20
    kC = 25

    rr = rank_combination(red)
    gg = rank_combination(green)
    yy = rank_combination(yellow)
    pp = rank_combination(pink)

    key = rr
    key = key * kG + gg
    key = key * kY + yy
    key = key * kP + pp
    key = key * kB + blue
    key = key * kC + cyan
    return key

def solve_target():
    H = 5
    W = 6

    red_l = Shape(H, W, [(0, 0), (0, 1), (1, 0)])
    green_l = Shape(H, W, [(0, 1), (1, 0), (1, 1)])
    v_domino = Shape(H, W, [(0, 0), (1, 0)])
    single = Shape(H, W, [(0, 0)])
    blue_sq = Shape(H, W, [(0, 0), (0, 1), (1, 0), (1, 1)])
    h_domino = Shape(H, W, [(0, 0), (0, 1)])

    start_red = tuple(sorted([red_l.idx_of(0, 1), red_l.idx_of(0, 4)]))
    start_green = tuple(sorted([green_l.idx_of(0, 2), green_l.idx_of(3, 4)]))
    start_yellow = tuple(sorted([v_domino.idx_of(1, 5), v_domino.idx_of(2, 4)]))
    start_pink = tuple(sorted([
        single.idx_of(2, 0), single.idx_of(2, 1),
        single.idx_of(3, 0), single.idx_of(3, 1),
        single.idx_of(4, 0), single.idx_of(4, 1)
    ]))
    start_blue = blue_sq.idx_of(2, 2)
    start_cyan = h_domino.idx_of(4, 2)

    seen = set()
    start_state = (start_red, start_green, start_yellow, start_pink, start_blue, start_cyan)
    start_key = encode_target(*start_state)
    seen.add(start_key)

    q = [start_state]
    head = 0

    def push_state(ns):
        key = encode_target(*ns)
        if key not in seen:
            seen.add(key)
            q.append(ns)

    while head < len(q):
        cur_red, cur_green, cur_yellow, cur_pink, cur_blue, cur_cyan = q[head]
        head += 1

        m_r0 = red_l.masks[cur_red[0]]
        m_r1 = red_l.masks[cur_red[1]]
        m_g0 = green_l.masks[cur_green[0]]
        m_g1 = green_l.masks[cur_green[1]]
        m_y0 = v_domino.masks[cur_yellow[0]]
        m_y1 = v_domino.masks[cur_yellow[1]]
        m_p = [single.masks[p] for p in cur_pink]
        m_b = blue_sq.masks[cur_blue]
        m_c = h_domino.masks[cur_cyan]

        occ = m_r0 | m_r1 | m_g0 | m_g1 | m_y0 | m_y1 | m_b | m_c
        for m in m_p:
            occ |= m

        # Red
        for i in range(2):
            base = cur_red[i]
            own = m_r0 if i == 0 else m_r1
            occ_wo = occ ^ own
            for d in range(DIRS):
                cur_idx = base
                while True:
                    next_idx = red_l.next[cur_idx][d]
                    if next_idx < 0: break
                    nm = red_l.masks[next_idx]
                    if (nm & occ_wo) != 0: break
                    ns_red = list(cur_red)
                    ns_red[i] = next_idx
                    if ns_red[0] > ns_red[1]: ns_red[0], ns_red[1] = ns_red[1], ns_red[0]
                    push_state((tuple(ns_red), cur_green, cur_yellow, cur_pink, cur_blue, cur_cyan))
                    cur_idx = next_idx

        # Green
        for i in range(2):
            base = cur_green[i]
            own = m_g0 if i == 0 else m_g1
            occ_wo = occ ^ own
            for d in range(DIRS):
                cur_idx = base
                while True:
                    next_idx = green_l.next[cur_idx][d]
                    if next_idx < 0: break
                    nm = green_l.masks[next_idx]
                    if (nm & occ_wo) != 0: break
                    ns_green = list(cur_green)
                    ns_green[i] = next_idx
                    if ns_green[0] > ns_green[1]: ns_green[0], ns_green[1] = ns_green[1], ns_green[0]
                    push_state((cur_red, tuple(ns_green), cur_yellow, cur_pink, cur_blue, cur_cyan))
                    cur_idx = next_idx

        # Yellow
        for i in range(2):
            base = cur_yellow[i]
            own = m_y0 if i == 0 else m_y1
            occ_wo = occ ^ own
            for d in range(DIRS):
                cur_idx = base
                while True:
                    next_idx = v_domino.next[cur_idx][d]
                    if next_idx < 0: break
                    nm = v_domino.masks[next_idx]
                    if (nm & occ_wo) != 0: break
                    ns_yellow = list(cur_yellow)
                    ns_yellow[i] = next_idx
                    if ns_yellow[0] > ns_yellow[1]: ns_yellow[0], ns_yellow[1] = ns_yellow[1], ns_yellow[0]
                    push_state((cur_red, cur_green, tuple(ns_yellow), cur_pink, cur_blue, cur_cyan))
                    cur_idx = next_idx

        # Pink
        for i in range(6):
            base = cur_pink[i]
            own = m_p[i]
            occ_wo = occ ^ own
            for d in range(DIRS):
                cur_idx = base
                while True:
                    next_idx = single.next[cur_idx][d]
                    if next_idx < 0: break
                    nm = single.masks[next_idx]
                    if (nm & occ_wo) != 0: break
                    ns_pink = list(cur_pink)
                    ns_pink[i] = next_idx
                    ns_pink.sort()
                    push_state((cur_red, cur_green, cur_yellow, tuple(ns_pink), cur_blue, cur_cyan))
                    cur_idx = next_idx

        # Blue
        occ_wo_b = occ ^ m_b
        for d in range(DIRS):
            cur_idx = cur_blue
            while True:
                next_idx = blue_sq.next[cur_idx][d]
                if next_idx < 0: break
                nm = blue_sq.masks[next_idx]
                if (nm & occ_wo_b) != 0: break
                push_state((cur_red, cur_green, cur_yellow, cur_pink, next_idx, cur_cyan))
                cur_idx = next_idx

        # Cyan
        occ_wo_c = occ ^ m_c
        for d in range(DIRS):
            cur_idx = cur_cyan
            while True:
                next_idx = h_domino.next[cur_idx][d]
                if next_idx < 0: break
                nm = h_domino.masks[next_idx]
                if (nm & occ_wo_c) != 0: break
                push_state((cur_red, cur_green, cur_yellow, cur_pink, cur_blue, next_idx))
                cur_idx = next_idx

    return len(seen)

def solve():
    return str(solve_target())

if __name__ == "__main__":
    print(solve())
