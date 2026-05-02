MOD = 1000004321
COLORS = 4

class State:
    def __init__(self, rt, ct, rb, cb, prev_vert):
        self.rt = rt
        self.ct = ct
        self.rb = rb
        self.cb = cb
        self.prev_vert = prev_vert

    def __hash__(self):
        return hash((self.rt, self.ct, self.rb, self.cb, self.prev_vert))

    def __eq__(self, other):
        return (self.rt == other.rt and self.ct == other.ct and 
                self.rb == other.rb and self.cb == other.cb and 
                self.prev_vert == other.prev_vert)

    def __lt__(self, other):
        return (self.rt, self.ct, self.rb, self.cb, self.prev_vert) < (other.rt, other.ct, other.rb, other.cb, other.prev_vert)

def initial_states():
    init = []
    for v in range(COLORS):
        init.append(State(0, v, 0, v, 1))

    for lt in range(1, 4):
        for lb in range(1, 4):
            for a in range(COLORS):
                for b in range(COLORS):
                    if a == b:
                        continue
                    init.append(State(lt - 1, a, lb - 1, b, 0))
    return init

def next_states(s):
    out = []
    top_change = (s.rt == 0)
    bottom_change = (s.rb == 0)

    if s.rt == 0 and s.rb == 0:
        for v in range(COLORS):
            if v == s.ct or v == s.cb:
                continue
            out.append(State(0, v, 0, v, 1))

    top_options = []
    bottom_options = []

    if s.rt > 0:
        top_options.append((s.rt - 1, s.ct))
    else:
        for length in range(1, 4):
            for color in range(COLORS):
                if color == s.ct:
                    continue
                top_options.append((length - 1, color))

    if s.rb > 0:
        bottom_options.append((s.rb - 1, s.cb))
    else:
        for length in range(1, 4):
            for color in range(COLORS):
                if color == s.cb:
                    continue
                bottom_options.append((length - 1, color))

    for top in top_options:
        for bottom in bottom_options:
            nt_rt, nt_ct = top
            nt_rb, nt_cb = bottom

            if nt_ct == nt_cb:
                continue

            if top_change and bottom_change and s.prev_vert == 0:
                continue

            out.append(State(nt_rt, nt_ct, nt_rb, nt_cb, 0))

    return out

def multiply(x, y):
    n = len(x)
    z = [[0] * n for _ in range(n)]
    for i in range(n):
        x_row = x[i]
        z_row = z[i]
        non_zero_x = [(k, v) for k, v in enumerate(x_row) if v]
        for k, xik in non_zero_x:
            y_row = y[k]
            for j in range(n):
                if y_row[j]:
                    z_row[j] += xik * y_row[j]
        for j in range(n):
            z_row[j] %= MOD
    return z

def multiply_vec(v, m):
    n = len(m)
    out = [0] * n
    non_zero_v = [(i, val) for i, val in enumerate(v) if val]
    for i, vi in non_zero_v:
        for j in range(n):
            if m[i][j]:
                out[j] += vi * m[i][j]
    for j in range(n):
        out[j] %= MOD
    return out

class Solver:
    def __init__(self):
        self.init_states = initial_states()
        self.build_reachable()
        self.build_transition()
        self.build_initial_vector()

    def build_reachable(self):
        seen = set()
        q = []

        for s in self.init_states:
            if s not in seen:
                seen.add(s)
                q.append(s)

        while q:
            s = q.pop(0)
            for t in next_states(s):
                if t not in seen:
                    seen.add(t)
                    q.append(t)

        self.states = sorted(list(seen))
        self.index = {s: i for i, s in enumerate(self.states)}

    def build_transition(self):
        n = len(self.states)
        self.transition = [[0] * n for _ in range(n)]

        for i in range(n):
            ns = next_states(self.states[i])
            for t in ns:
                j = self.index[t]
                self.transition[i][j] = (self.transition[i][j] + 1) % MOD

    def build_initial_vector(self):
        self.init_vector = [0] * len(self.states)
        for s in self.init_states:
            i = self.index[s]
            self.init_vector[i] = (self.init_vector[i] + 1) % MOD

    def count(self, n):
        vec = list(self.init_vector)
        p = [list(row) for row in self.transition]
        exp = n - 1

        while exp > 0:
            if exp % 2 != 0:
                vec = multiply_vec(vec, p)
            exp //= 2
            if exp > 0:
                p = multiply(p, p)

        ans = 0
        for i in range(len(self.states)):
            s = self.states[i]
            if s.rt == 0 and s.rb == 0:
                ans = (ans + vec[i]) % MOD

        return ans

def solve():
    solver = Solver()
    ans = solver.count(10000000000000000)
    return str(ans)

if __name__ == '__main__':
    print(solve())
