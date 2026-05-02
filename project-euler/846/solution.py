def extended_gcd(a, b):
    x, y = a, b
    ax, ay = 1, 0
    bx, by = 0, 1
    while x != 0:
        k = y // x
        y %= x
        ay -= k * ax
        by -= k * bx
        x, y = y, x
        ax, ay = ay, ax
        bx, by = by, bx
    return y, ay, by

class GaussianInt:
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __mul__(self, other):
        return GaussianInt(self.x * other.x - self.y * other.y,
                           self.x * other.y + self.y * other.x)
                           
    def norm(self):
        return self.x * self.x + self.y * self.y

def solve_F(N):
    primes = []
    spf = [0] * (N + 1)
    for i in range(2, N + 1):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
        for p in primes:
            if p * i > N: break
            spf[p * i] = p
            if p == spf[i]: break
            
    exact_sqrt = [0] * (N + 1)
    i = 1
    while i * i <= N:
        exact_sqrt[i * i] = i
        i += 1
        
    vals = [None] * (N + 1)
    
    def normalize(a):
        ax = abs(a.x)
        ay = abs(a.y)
        if ax < ay:
            ax, ay = ay, ax
        return GaussianInt(ax, ay)
        
    vals[1] = GaussianInt(1, 0)
    if N >= 2:
        vals[2] = GaussianInt(1, 1)
        
    for p in primes:
        if p == 2 or (p & 3) == 3: continue
        
        a = 0
        b = 0
        i = 1
        while True:
            rem = p - i * i
            if rem >= 0 and exact_sqrt[rem] != 0:
                a = i
                b = exact_sqrt[rem]
                break
            i += 1
            
        cur = GaussianInt(1, 0)
        q = 1
        while q * p <= N:
            q *= p
            cur = cur * GaussianInt(a, b)
            vals[q] = normalize(cur)
            if 2 * q <= N:
                vals[2 * q] = normalize(cur * GaussianInt(1, 1))
                
    parents = [[] for _ in range(N + 1)]
    dp = [[] for _ in range(N + 1)]
    
    for i in range(1, N + 1):
        if vals[i] is None: continue
        if i == 1: continue
        
        v = vals[i]
        g, cx, cy = extended_gcd(v.x, v.y)
        if g < 0:
            g = -g
            cx = -cx
            cy = -cy
            
        p1 = GaussianInt(abs(cy), abs(cx))
        p2 = GaussianInt(v.x - p1.x, v.y - p1.y)
        if p1.norm() > p2.norm():
            p1, p2 = p2, p1
            
        n1 = p1.norm()
        if n1 <= N and vals[n1] is not None:
            parents[i].append(n1)
            
        n2 = p2.norm()
        if i > 2 and n2 <= N and vals[n2] is not None:
            parents[i].append(n2)
            
        dp[i] = [[0, 0] for _ in range(len(parents[i]))]
        
    answer = 0
    ways = 0
    
    for i in range(N, 0, -1):
        pi = parents[i]
        dpi = dp[i]
        
        for z in range(len(pi)):
            cur_ways, cur_sum = dpi[z]
            ways += cur_ways
            answer += cur_ways * (i + pi[z]) + cur_sum
            dpi[z][0] += 1
            
        if len(pi) == 2:
            j = pi[1]
            pj = parents[j]
            z = pj.index(pi[0])
            
            w0, s0 = dpi[0]
            w1, s1 = dpi[1]
            
            dp[j][z][0] += w0 * w1
            dp[j][z][1] += w0 * w1 * i + w0 * s1 + w1 * s0
            
    return answer

def solve():
    return str(solve_F(1000000))

if __name__ == "__main__":
    print(solve())
