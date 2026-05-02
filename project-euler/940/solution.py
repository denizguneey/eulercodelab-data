kMod = 1123581313

def mat_mul(a, b):
    c = [[0, 0], [0, 0]]
    for i in range(2):
        for k in range(2):
            if a[i][k] == 0:
                continue
            for j in range(2):
                c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % kMod
    return c

def mat_pow(base, exp):
    res = [[1, 0], [0, 1]]
    while exp > 0:
        if exp & 1:
            res = mat_mul(res, base)
        base = mat_mul(base, base)
        exp >>= 1
    return res

def mat_vec_mul(a, v):
    r = [0, 0]
    for i in range(2):
        r[i] = (a[i][0] * v[0] + a[i][1] * v[1]) % kMod
    return r

def solve(k):
    fib = [0] * (k + 1)
    fib[0] = 0
    if k >= 1:
        fib[1] = 1
    for i in range(2, k + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
        
    C = [[0, 1], [3, 1]]
    M = [[1, 1], [3, 2]]
    v0 = [0, 1]
    
    col = [[0, 0] for _ in range(k + 1)]
    row = [[[0, 0], [0, 0]] for _ in range(k + 1)]
    
    for i in range(2, k + 1):
        row[i] = mat_pow(M, fib[i])
        col[i] = mat_vec_mul(mat_pow(C, fib[i]), v0)
        
    ans = 0
    for i in range(2, k + 1):
        for j in range(2, k + 1):
            val = (row[i][0][0] * col[j][0] + row[i][0][1] * col[j][1]) % kMod
            ans = (ans + val) % kMod
            
    return str(ans)

if __name__ == "__main__":
    print(solve(50))
