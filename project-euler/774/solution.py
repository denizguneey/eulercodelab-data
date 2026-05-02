import sys

# Increase recursion depth just in case
sys.setrecursionlimit(20000)

MOD = 998244353

def add_mod(a, b):
    s = a + b
    if s >= MOD: s -= MOD
    return s

def mul_mod(a, b):
    return (a * b) % MOD

# EdgeTypes: 0=G, 1=O, 2=C
def is_g(e): return e[0] == 0
def is_o(e): return e[0] == 1
def is_c(e): return e[0] == 2

def G(): return (0, 0)
def O(): return (1, 0)
def C(n): return (2, n)

def insert_edge(n, e):
    if is_g(e): return C(n)
    if is_o(e): return C(n) if (n & 1) else C(0)
    return C(n)

def up0(e):
    if is_c(e): return C(e[1] // 2)
    if is_o(e): return C(0)
    return G()

def up1(e):
    if is_c(e):
        if (e[1] & 1) == 0: return C(e[1] // 2)
        return G()
    return G()

def edge_code(e):
    if is_g(e): return -1
    if is_o(e): return -2
    return e[1]

class Solver774:
    def __init__(self, max_l, a, b):
        self.a_ = a
        self.b_ = b
        self.fib_pos_ = [0] * (max_l + 2)
        self.fib_pos_[0] = 0
        self.fib_pos_[1] = 1
        for i in range(2, max_l + 2):
            self.fib_pos_[i] = add_mod(self.fib_pos_[i - 1], self.fib_pos_[i - 2])
        self.memo_ = {}

    def fib(self, x):
        if x >= 0: return self.fib_pos_[x]
        n = -x
        v = self.fib_pos_[n]
        if (n & 1) == 0 and v != 0: v = MOD - v
        return v

    def f(self, l, n, left, right):
        if (is_c(left) and left[1] == 0) or (is_c(right) and right[1] == 0):
            return 0

        key = (l, n, edge_code(left), edge_code(right))
        if key in self.memo_:
            return self.memo_[key]

        ret = 0

        if n == 0:
            ret = 1 if (l <= 1 and is_g(left) and is_g(right)) else 0
            self.memo_[key] = ret
            return ret

        if n == 1:
            if is_g(left) and is_g(right):
                ret = 1 if (l > 1) else 2
            elif (is_o(left) and is_o(right)) or (is_o(left) and is_g(right)) or (is_g(left) and is_o(right)):
                ret = 1
            elif is_c(left) and is_c(right):
                ret = 1 if ((left[1] & 1) and (right[1] & 1)) else 0
            elif is_c(left):
                ret = 1 if (left[1] & 1) else 0
            elif is_c(right):
                ret = 1 if (right[1] & 1) else 0
            else:
                ret = 0
            self.memo_[key] = ret
            return ret

        m = (n - 1) // 2

        if l == 1:
            if is_g(left) and is_g(right):
                ret = (n + 1) % MOD
            else:
                ret = add_mod(self.f(1, n // 2, up0(left), up0(right)),
                              self.f(1, m, up1(left), up1(right)))
            self.memo_[key] = ret
            return ret

        s = 0
        s = add_mod(s, mul_mod(self.f(l, m, up0(left), up0(right)), self.fib(l)))
        s = add_mod(s, mul_mod(self.f(l, m, up0(left), up1(right)), self.fib(l - 1)))
        s = add_mod(s, mul_mod(self.f(l, m, up1(left), up0(right)), self.fib(l - 1)))
        s = add_mod(s, mul_mod(self.f(l, m, up1(left), up1(right)), self.fib(l - 2)))

        up1o = up1(O())
        for x in range(1, l):
            right_part = self.f(l - x, n, O(), right)
            if x > 1:
                left_part = self.f(x, m, up0(left), up1o)
                s = add_mod(s, mul_mod(mul_mod(left_part, right_part), self.fib(x - 1)))
            left_part2 = self.f(x, m, up1(left), up1o)
            s = add_mod(s, mul_mod(mul_mod(left_part2, right_part), self.fib(x - 2)))

        if (n & 1) == 0:
            cn = C(n)
            up0cn = up0(cn)

            for x in range(2, l):
                right_part = self.f(l - x, n, cn, right)

                a = self.f(x - 1, m, up0(left), up0cn)
                s = add_mod(s, mul_mod(mul_mod(a, right_part), self.fib(x)))

                b = self.f(x - 1, m, up1(left), up0cn)
                s = add_mod(s, mul_mod(mul_mod(b, right_part), self.fib(x - 1)))

            s = add_mod(s, self.f(l - 1, n, insert_edge(n, left), right))

            ins_right = insert_edge(n, right)
            s = add_mod(s, mul_mod(self.f(l - 1, m, up0(left), up0(ins_right)), self.fib(l)))
            s = add_mod(s, mul_mod(self.f(l - 1, m, up1(left), up0(ins_right)), self.fib(l - 1)))

        ret = s
        self.memo_[key] = ret
        return ret

    def solve(self):
        return self.f(self.a_, self.b_, G(), G())

def compute_c(n, b):
    solver = Solver774(n, n, b)
    return solver.solve()

def solve():
    return str(compute_c(123, 123456789))

if __name__ == "__main__":
    print(solve())
