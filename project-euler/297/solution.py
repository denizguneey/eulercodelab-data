import sys

sys.setrecursionlimit(2000)

class Solver:
    def __init__(self):
        self.fib = [1, 2]
        while self.fib[-1] < 1000000000000000000:
            self.fib.append(self.fib[-1] + self.fib[-2])
        self.memo = {}

    def S(self, n):
        if n <= 4:
            return n - 1
        if n in self.memo:
            return self.memo[n]

        # Find largest Fibonacci number less than n
        lb = 0
        for i, val in enumerate(self.fib):
            if val >= n:
                lb = i
                break

        p = self.fib[lb - 1]
        value = self.S(p) + (n - p) + self.S(n - p)
        self.memo[n] = value
        return value

    def solve(self, n):
        self.memo.clear()
        return self.S(n)

def solve(limit=100000000000000000):
    solver = Solver()
    return str(solver.solve(limit))

if __name__ == '__main__':
    print(solve())
