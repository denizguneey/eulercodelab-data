import sys

sys.setrecursionlimit(2000)

class Solver:
    def __init__(self, ranks, copies):
        self.ranks = ranks
        self.copies = copies
        self.base = ranks + 1
        self.memo = {}

    def expected_draws(self):
        if self.ranks <= 0 or self.copies <= 0:
            return 0.0
        a = [0] * (self.copies + 1)
        if self.ranks >= 1:
            a[self.copies] = self.ranks - 1
        m = self.copies - 1
        self.memo.clear()
        return 1.0 + self.dfs(m, tuple(a))

    def dfs(self, m, a):
        remaining = m
        for i in range(1, self.copies + 1):
            remaining += i * a[i]
        if remaining == 0:
            return 0.0

        key = (m, a)
        if key in self.memo:
            return self.memo[key]

        ans = 1.0
        for i in range(1, self.copies + 1):
            if a[i] == 0:
                continue
            p = float(i * a[i]) / float(remaining)
            b = list(a)
            b[i] -= 1
            b[m] += 1
            ans += p * self.dfs(i - 1, tuple(b))

        self.memo[key] = ans
        return ans

def solve():
    ans = Solver(13, 4).expected_draws()
    return f"{ans:.8f}"

if __name__ == "__main__":
    print(solve())
