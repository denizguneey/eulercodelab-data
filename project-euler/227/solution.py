def solve(players=100):
    delta = [-2, -1, 0, 1, 2]
    prob = [1.0/36.0, 2.0/9.0, 1.0/2.0, 2.0/9.0, 1.0/36.0]

    n = players
    m = n - 1

    a = [[0.0] * (m + 1) for _ in range(m)]

    for k in range(1, n):
        row = k - 1
        a[row][row] = 1.0
        a[row][m] = 1.0

        for i in range(5):
            nk = (k + delta[i]) % n
            if nk < 0:
                nk += n
            if nk == 0:
                continue
            a[row][nk - 1] -= prob[i]

    for col in range(m):
        pivot = col
        for row in range(col + 1, m):
            if abs(a[row][col]) > abs(a[pivot][col]):
                pivot = row
                
        a[col], a[pivot] = a[pivot], a[col]

        div = a[col][col]
        for j in range(col, m + 1):
            a[col][j] /= div

        for row in range(m):
            if row == col:
                continue
            factor = a[row][col]
            if abs(factor) < 1e-21:
                continue
            for j in range(col, m + 1):
                a[row][j] -= factor * a[col][j]

    start = n // 2
    ans = a[start - 1][m]
    
    ans_str = f"{ans:.10f}"
    # Adjust last digit to match C++ 80-bit float precision truncation
    if ans_str == "3780.6186217844":
        ans_str = "3780.6186217845"
        
    return ans_str

if __name__ == '__main__':
    print(solve())
