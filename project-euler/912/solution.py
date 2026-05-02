MOD = 1000000007

def add_mod(a, b):
    v = a + b
    if v >= MOD:
        v -= MOD
    return v

def mul_mod(a, b):
    return (a * b) % MOD

class Stats:
    def __init__(self):
        self.total = 0
        self.odd = 0
        self.odd_mod = 0
        self.s1_mod = 0
        self.s2_mod = 0

class Solver:
    def __init__(self):
        self.memo = [[], [], []]
        self.seen = [[], [], []]
        for c in range(3):
            self.memo[c].append(Stats())
            self.seen[c].append(False)

    def empty(self):
        return Stats()

    def merge(self, left, right):
        if left.total == 0:
            return right
        if right.total == 0:
            return left
            
        out = Stats()
        out.total = left.total + right.total
        out.odd = left.odd + right.odd
        out.odd_mod = add_mod(left.odd_mod, right.odd_mod)
        
        shift = left.total % MOD
        shift2 = mul_mod(shift, shift)
        
        out.s1_mod = left.s1_mod
        out.s1_mod = add_mod(out.s1_mod, right.s1_mod)
        out.s1_mod = add_mod(out.s1_mod, mul_mod(shift, right.odd_mod))
        
        out.s2_mod = left.s2_mod
        out.s2_mod = add_mod(out.s2_mod, right.s2_mod)
        out.s2_mod = add_mod(out.s2_mod, mul_mod((2 * shift) % MOD, right.s1_mod))
        out.s2_mod = add_mod(out.s2_mod, mul_mod(shift2, right.odd_mod))
        
        return out

    def base(self, c):
        s = Stats()
        s.total = 1
        s.odd = 1 if c > 0 else 0
        s.odd_mod = s.odd
        s.s1_mod = s.odd
        s.s2_mod = s.odd
        return s

    def full(self, c, r):
        if r >= len(self.memo[c]):
            # Append up to r
            while len(self.memo[c]) <= r:
                self.memo[c].append(Stats())
                self.seen[c].append(False)
                
        if self.seen[c][r]:
            return self.memo[c][r]
            
        if r == 0:
            out = self.base(c)
        else:
            left = self.full(0, r - 1)
            right = self.full(c + 1, r - 1) if c < 2 else self.empty()
            out = self.merge(left, right)
            
        self.seen[c][r] = True
        self.memo[c][r] = out
        return out

    def prefix_stats(self, c, r, k):
        if k == 0:
            return self.empty()
            
        f = self.full(c, r)
        if k >= f.total:
            return f
            
        if r == 0:
            return self.base(c)
            
        left = self.full(0, r - 1)
        if k <= left.total:
            return self.prefix_stats(0, r - 1, k)
            
        assert c < 2
        right_part = self.prefix_stats(c + 1, r - 1, k - left.total)
        return self.merge(left, right_part)

    def F(self, n):
        remaining = n
        prefix = 0
        ans = 0
        length = 1
        
        while remaining > 0:
            block = self.full(1, length - 1)
            take = remaining if remaining < block.total else block.total
            chosen = block if take == block.total else self.prefix_stats(1, length - 1, take)
            
            p = prefix % MOD
            p2 = mul_mod(p, p)
            
            contrib = 0
            contrib = add_mod(contrib, mul_mod(chosen.odd_mod, p2))
            contrib = add_mod(contrib, mul_mod((2 * p) % MOD, chosen.s1_mod))
            contrib = add_mod(contrib, chosen.s2_mod)
            
            ans = add_mod(ans, contrib)
            prefix += take
            remaining -= take
            length += 1
            
        return ans

def solve():
    solver = Solver()
    return str(solver.F(10000000000000000))

if __name__ == "__main__":
    print(solve())
