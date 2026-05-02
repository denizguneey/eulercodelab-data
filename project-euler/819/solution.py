def expected_steps(n):
    p = [[0.0] * (n + 1) for _ in range(n + 1)]
    p[0][0] = 1.0
    
    N = float(n)
    
    for k in range(n):
        for j in range(k + 1):
            cur = p[k][j]
            if cur == 0.0:
                continue
            p[k + 1][j] += cur * (float(j) / N)
            p[k + 1][j + 1] += cur * (float(n - j) / N)
            
    e = [0.0] * (n + 1)
    e[1] = 0.0
    
    for k in range(2, n + 1):
        num = 1.0
        for j in range(1, k):
            num += p[k][j] * e[j]
        den = 1.0 - p[k][k]
        e[k] = num / den
        
    return e[n]

def solve():
    ans = expected_steps(1000)
    return "{:.6f}".format(ans)

if __name__ == "__main__":
    print(solve())
