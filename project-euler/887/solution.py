import sys
sys.setrecursionlimit(20000)

class BoundedSearch:
    def __init__(self, limit):
        self.limit = limit
        self.memo = [{} for _ in range(128)]

    def F(self, m, d):
        if d < -1:
            return 0
        if d > self.limit:
            d = self.limit
            
        if m == 0:
            return 1
        if d == -1:
            return 1
            
        if d >= m - 1:
            if m >= 63:
                return self.limit
            full = 1 << m
            return min(full, self.limit)

        key = d + 1
        
        if key in self.memo[m]:
            return self.memo[m][key]

        y = self.F(m - 1, d - 1)
        d2 = y + d - 1
        z = self.F(m - 1, d2)

        ans = y + z
        if ans > self.limit:
            ans = self.limit
            
        self.memo[m][key] = ans
        return ans

    def Q(self, N, d):
        if d == 0:
            return N - 1
        m = 0
        while self.F(m, d) < N:
            m += 1
        return m

def solve():
    L = 7**10
    bs = BoundedSearch(L)

    ans = L * (L - 1) // 2
    for d in range(1, 8):
        prev = 0
        m = 0
        while prev < L:
            cur = bs.F(m, d)
            upto = min(cur, L)
            ans += m * (upto - prev)
            prev = upto
            m += 1

    return str(ans)

if __name__ == "__main__":
    print(solve())
