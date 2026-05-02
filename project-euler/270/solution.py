def build_boundary(n):
    pts = []
    for x in range(n + 1):
        pts.append((x, 0))
    for y in range(1, n + 1):
        pts.append((n, y))
    for x in range(n - 1, -1, -1):
        pts.append((x, n))
    for y in range(n - 1, 0, -1):
        pts.append((0, y))
    return pts

def same_side(a, b, n):
    if a[1] == 0 and b[1] == 0: return True
    if a[1] == n and b[1] == n: return True
    if a[0] == 0 and b[0] == 0: return True
    if a[0] == n and b[0] == n: return True
    return False

def count_triangulations(n):
    if n <= 0: return 0
    kMod = 100000000
    pts = build_boundary(n)
    m = len(pts)
    
    allowed = [[False] * m for _ in range(m)]
    for i in range(m):
        for j in range(i + 1, m):
            ok = False
            if j == i + 1 or (i == 0 and j == m - 1):
                ok = True
            elif not same_side(pts[i], pts[j], n):
                ok = True
            allowed[i][j] = ok
            allowed[j][i] = ok
            
    dp = [[0] * m for _ in range(m)]
    for i in range(m - 1):
        dp[i][i + 1] = 1
        
    for length in range(2, m):
        for i in range(m - length):
            j = i + length
            if not allowed[i][j]:
                dp[i][j] = 0
                continue
                
            s = 0
            for k in range(i + 1, j):
                left = dp[i][k]
                if left == 0: continue
                right = dp[k][j]
                if right == 0: continue
                s = (s + left * right) % kMod
            dp[i][j] = s
            
    return dp[0][m - 1]

def solve():
    return str(count_triangulations(30))

if __name__ == '__main__':
    print(solve())
