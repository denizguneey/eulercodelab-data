import sys
sys.setrecursionlimit(2000)

def width_from_exponents(exps):
    poly = [1]
    for e in exps:
        next_poly = [0] * (len(poly) + e)
        for i, v in enumerate(poly):
            for t in range(e + 1):
                next_poly[i + t] += v
        poly = next_poly
    return max(poly)

class Solver:
    def __init__(self):
        self.TARGET = 10000
        self.primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
        self.best = 1
        for i in range(16):
            self.best *= self.primes[i]

    def dfs(self, pos, max_exp, n, exps):
        w = width_from_exponents(exps)
        if w >= self.TARGET:
            if n < self.best:
                self.best = n
            return
        
        if pos >= len(self.primes):
            return

        mult = 1
        p = self.primes[pos]
        for e in range(1, max_exp + 1):
            mult *= p
            n2 = n * mult
            if n2 >= self.best:
                break
            exps.append(e)
            self.dfs(pos + 1, e, n2, exps)
            exps.pop()

    def solve(self):
        exps = []
        self.dfs(0, 64, 1, exps)
        return str(self.best)

def solve():
    s = Solver()
    return s.solve()

if __name__ == "__main__":
    print(solve())
