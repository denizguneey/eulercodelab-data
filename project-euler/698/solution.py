import sys

sys.setrecursionlimit(20000)

def build_is123(limit):
    is123 = [False] * (limit + 1)
    is123[1] = True
    for x in range(2, limit + 1):
        s = str(x)
        c1 = c2 = c3 = 0
        valid = True
        for ch in s:
            if ch == '1': c1 += 1
            elif ch == '2': c2 += 1
            elif ch == '3': c3 += 1
            else:
                valid = False
                break
        if not valid: continue
        if (c1 == 0 or is123[c1]) and (c2 == 0 or is123[c2]) and (c3 == 0 or is123[c3]):
            is123[x] = True
    return is123

class Nth123Solver:
    def __init__(self, cap, is123):
        self.cap = cap
        self.is123 = is123
        self.choose = [[1]]
        self.memo = {}
        self.length = 0
        
    def ensure_choose(self, n):
        while len(self.choose) <= n:
            m = len(self.choose)
            row = [0] * (m + 1)
            row[0] = 1
            row[m] = 1
            for k in range(1, m):
                val = self.choose[m - 1][k - 1] + self.choose[m - 1][k]
                row[k] = min(val, self.cap + 1)
            self.choose.append(row)
            
    def multinomial(self, n, a, b):
        self.ensure_choose(n)
        first = self.choose[n][a]
        second = self.choose[n - a][b]
        return min(first * second, self.cap + 1)

    def count_length(self, length):
        total = 0
        for a in range(length + 1):
            if a > 0 and not self.is123[a]: continue
            for b in range(length - a + 1):
                c = length - a - b
                if b > 0 and not self.is123[b]: continue
                if c > 0 and not self.is123[c]: continue
                if a == 0 and b == 0 and c == 0: continue
                
                total += self.multinomial(length, a, b)
                if total > self.cap:
                    return self.cap + 1
        return total

    def count_with_prefix(self, pos, u1, u2, u3):
        key = (pos, u1, u2, u3)
        if key in self.memo: return self.memo[key]
        
        rem = self.length - pos
        total = 0
        
        for A in range(u1, self.length + 1):
            if A > 0 and not self.is123[A]: continue
            max_b = self.length - A
            if u2 > max_b: continue
            for B in range(u2, max_b + 1):
                C = self.length - A - B
                if C < u3: continue
                if B > 0 and not self.is123[B]: continue
                if C > 0 and not self.is123[C]: continue
                
                a = A - u1
                b = B - u2
                c = C - u3
                if a + b + c != rem: continue
                
                total += self.multinomial(rem, a, b)
                if total > self.cap:
                    self.memo[key] = self.cap + 1
                    return self.cap + 1
                    
        self.memo[key] = total
        return total

    def solve(self, n):
        cumulative = 0
        self.length = 0
        
        while True:
            self.length += 1
            count = self.count_length(self.length)
            if cumulative + count >= n:
                break
            cumulative += count
            
        rank = n - cumulative
        self.memo.clear()
        
        u1 = u2 = u3 = 0
        out = []
        
        for pos in range(self.length):
            for d in range(1, 4):
                n1 = u1 + (1 if d == 1 else 0)
                n2 = u2 + (1 if d == 2 else 0)
                n3 = u3 + (1 if d == 3 else 0)
                
                cnt = self.count_with_prefix(pos + 1, n1, n2, n3)
                if rank > cnt:
                    rank -= cnt
                else:
                    out.append(str(d))
                    u1, u2, u3 = n1, n2, n3
                    break
                    
        return "".join(out)

def solve():
    kTargetN = 111111111111222333
    kMod = 123123123
    kIs123Limit = 5000
    
    is123 = build_is123(kIs123Limit)
    solver = Nth123Solver(kTargetN, is123)
    val_str = solver.solve(kTargetN)
    
    value = 0
    for ch in val_str:
        value = (value * 10 + int(ch)) % kMod
        
    return str(value)

if __name__ == '__main__':
    print(solve())
