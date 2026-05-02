import math
from functools import lru_cache

def interval_less(a, b):
    if a[0] != b[0]:
        return a[0] < b[0]
    return a[1] < b[1]

def lcm_upto(n):
    d = 1
    for i in range(1, n + 1):
        d = math.lcm(d, i)
    return d

class Solver:
    def __init__(self, target):
        self.target = target
        self.d = lcm_upto(target)
        self.memo_min = {}
        self.memo_feasible = {}

    def pack(self, intervals):
        return tuple((in_l, in_u) for in_l, in_u in intervals)

    def solve_min_state(self, intervals):
        key = self.pack(intervals)
        if key in self.memo_min:
            return self.memo_min[key]

        n = len(intervals)
        if n == self.target:
            s = sum(in_l for in_l, _ in intervals)
            self.memo_min[key] = s
            return s

        m = n + 1
        bins = [(k * self.d // m, (k + 1) * self.d // m) for k in range(m)]
        options = [[] for _ in range(n)]

        for i in range(n):
            for k in range(m):
                nl = max(intervals[i][0], bins[k][0])
                nu = min(intervals[i][1], bins[k][1])
                if nl < nu:
                    options[i].append((k, nl, nu))
            if not options[i]:
                inf = 1 << 60
                self.memo_min[key] = inf
                return inf

        order = list(range(n))
        order.sort(key=lambda i: len(options[i]))

        used = [False] * m
        assigned = [(0, 0)] * n
        best = [1 << 60]

        def dfs(pos):
            if pos == n:
                hole = -1
                for k in range(m):
                    if not used[k]:
                        hole = k
                        break
                if hole < 0:
                    return
                child = list(assigned)
                child.append((bins[hole][0], bins[hole][1]))
                child.sort(key=lambda x: (x[0], x[1]))

                cand = self.solve_min_state(child)
                if cand < best[0]:
                    best[0] = cand
                return

            i = order[pos]
            for op_bin, op_l, op_u in options[i]:
                if used[op_bin]:
                    continue
                used[op_bin] = True
                assigned[i] = (op_l, op_u)
                dfs(pos + 1)
                used[op_bin] = False

        dfs(0)
        self.memo_min[key] = best[0]
        return best[0]

    def solve_min(self):
        init = [(0, self.d)]
        return self.solve_min_state(init)

    def feasible_state(self, intervals):
        key = self.pack(intervals)
        if key in self.memo_feasible:
            return self.memo_feasible[key]

        n = len(intervals)
        if n == self.target:
            self.memo_feasible[key] = True
            return True

        m = n + 1
        bins = [(k * self.d // m, (k + 1) * self.d // m) for k in range(m)]
        options = [[] for _ in range(n)]

        for i in range(n):
            for k in range(m):
                nl = max(intervals[i][0], bins[k][0])
                nu = min(intervals[i][1], bins[k][1])
                if nl < nu:
                    options[i].append((k, nl, nu))
            if not options[i]:
                self.memo_feasible[key] = False
                return False

        order = list(range(n))
        order.sort(key=lambda i: len(options[i]))

        used = [False] * m
        assigned = [(0, 0)] * n
        ok = [False]

        def dfs(pos):
            if ok[0]:
                return
            if pos == n:
                hole = -1
                for k in range(m):
                    if not used[k]:
                        hole = k
                        break
                if hole < 0:
                    return
                child = list(assigned)
                child.append((bins[hole][0], bins[hole][1]))
                child.sort(key=lambda x: (x[0], x[1]))
                if self.feasible_state(child):
                    ok[0] = True
                return

            i = order[pos]
            for op_bin, op_l, op_u in options[i]:
                if used[op_bin]:
                    continue
                used[op_bin] = True
                assigned[i] = (op_l, op_u)
                dfs(pos + 1)
                used[op_bin] = False
                if ok[0]:
                    return

        dfs(0)
        self.memo_feasible[key] = ok[0]
        return ok[0]

    def can_choose_all(self):
        init = [(0, self.d)]
        return self.feasible_state(init)

def format_rounded_12(num, den):
    scale = 1000000000000
    rounded = (num * scale * 2 + den) // (den * 2)
    integer_part = rounded // scale
    frac_part = rounded % scale
    frac_str = str(frac_part).zfill(12)
    return f"{integer_part}.{frac_str}"

def solve():
    solver = Solver(17)
    num = solver.solve_min()
    return format_rounded_12(num, solver.d)

if __name__ == "__main__":
    print(solve())
