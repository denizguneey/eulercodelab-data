MOD = 1000000007

def mod_pow(a, e):
    return pow(a, e, MOD)

class Solver867:
    def __init__(self, n):
        self.n = n
        self.max_len = 2 * n - 1
        self.indep = [[] for _ in range(self.max_len + 1)]
        self.build_independent_masks()
        self.count_cache = {}
        self.h_cache = {}
        self.f_cache = {}
        self.r_cache = {}

    def pair_key(self, a, b):
        return (a << 32) | b

    def build_independent_masks(self):
        for L in range(self.max_len + 1):
            lim = 1 << L
            for m in range(lim):
                if (m & (m << 1)) == 0:
                    self.indep[L].append(m)

    def zeta_subset_sum(self, v, L):
        out = list(v)
        size = 1 << L
        for bit in range(L):
            step = 1 << bit
            block = step << 1
            for start in range(0, size, block):
                mid = start + step
                end = start + block
                for m in range(mid, end):
                    x = out[m] + out[m - step]
                    if x >= MOD:
                        x -= MOD
                    out[m] = x
        return out

    def encode_lengths(self, lens):
        return "|".join(map(str, lens))

    def count_independent_sets(self, row_lengths):
        key = self.encode_lengths(row_lengths)
        if key in self.count_cache:
            return self.count_cache[key]

        if not row_lengths:
            self.count_cache[key] = 1
            return 1

        L0 = row_lengths[0]
        dp = [0] * (1 << L0)
        for m in self.indep[L0]:
            dp[m] = 1

        for i in range(1, len(row_lengths)):
            Lc = row_lengths[i - 1]
            Ln = row_lengths[i]

            subs = self.zeta_subset_sum(dp, Lc)
            ndp = [0] * (1 << Ln)
            full = (1 << Lc) - 1

            if Ln == Lc + 1:
                for b in self.indep[Ln]:
                    forb = (b | (b >> 1)) & full
                    allowed = full ^ forb
                    ndp[b] = subs[allowed]
            else:
                for b in self.indep[Ln]:
                    forb = (b | (b << 1)) & full
                    allowed = full ^ forb
                    ndp[b] = subs[allowed]

            dp = ndp

        lastL = row_lengths[-1]
        total = 0
        for m in self.indep[lastL]:
            total += dp[m]
            if total >= MOD:
                total -= MOD

        self.count_cache[key] = total
        return total

    def H(self, n):
        if n in self.h_cache:
            return self.h_cache[n]

        lens = []
        for x in range(n, 2 * n):
            lens.append(x)
        for x in range(2 * n - 2, n - 1, -1):
            lens.append(x)

        val = self.count_independent_sets(lens)
        self.h_cache[n] = val
        return val

    def F(self, n, h):
        key = self.pair_key(n, h)
        if key in self.f_cache:
            return self.f_cache[key]

        rows = h - 1
        lens = []
        for i in range(max(0, rows)):
            lens.append(max(0, (n - 2) - i))

        val = self.count_independent_sets(lens)
        self.f_cache[key] = val
        return val

    def R(self, u, v):
        key = self.pair_key(u, v)
        if key in self.r_cache:
            return self.r_cache[key]

        if v == 0:
            res = self.H(u)
        else:
            res = 1 if (u == 1 and v == 1) else 0
            for w in range(u):
                corner = self.F(u, u - w)
                add = (self.R(v, w) * mod_pow(corner, 6)) % MOD
                res += add
                if res >= MOD:
                    res -= MOD

        self.r_cache[key] = res
        return res

    def T(self, n):
        ans = (2 * self.R(n, n)) % MOD
        if n == 1:
            ans = (ans + MOD - 1) % MOD
        return ans

def solve():
    solver = Solver867(10)
    return str(solver.T(10))

if __name__ == "__main__":
    print(solve())
