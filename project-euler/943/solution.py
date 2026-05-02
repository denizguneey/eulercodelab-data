import sys
sys.setrecursionlimit(2000)

def solve():
    kN = 22332223332233; kMod = 2233222333; kMin = 2; kMax = 223

    class Counter:
        def __init__(self, a, b):
            self.a = a; self.b = b; self.memo = {}

        def evaluate_prefix(self, n):
            for depth in range(62):
                s = self._block(0, depth, n)
                if s[0]+s[1] >= n: return s
            return (0, 0, 0)

        def _block(self, state, depth, budget):
            lm = 2 << depth; bit = state & lm
            rl = self.b if bit else self.a; take = min(rl, budget)
            if depth == 0:
                ca = take if (state & 1) == 0 else 0
                cb = take - ca
                return (ca, cb, state ^ 1)
            pa = pb = 0; cs = state ^ bit
            for i in range(take):
                key = (cs, depth - 1)
                if key in self.memo:
                    cached = self.memo[key]
                    if pa + pb + cached[0] + cached[1] <= budget:
                        child = cached
                    else:
                        child = self._block(cs, depth - 1, budget - (pa + pb))
                else:
                    child = self._block(cs, depth - 1, budget - (pa + pb))
                pa += child[0]; pb += child[1]; cs = child[2]
            result = (pa, pb, cs ^ bit ^ (1 << depth))
            self.memo[(state, depth)] = result
            return result

    def compute_t(a, b, n):
        c = Counter(a, b); s = c.evaluate_prefix(n)
        return s[0]*a + s[1]*b

    total = 0
    for a in range(kMin, kMax+1):
        for b in range(kMin, kMax+1):
            if a == b: continue
            total = (total + compute_t(a, b, kN) % kMod) % kMod
    return str(total)

if __name__ == '__main__':
    print(solve())
