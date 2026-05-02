def solve():
    N = 24680
    MOD = 1020202009

    prev = [0] * (N + 1)
    curr = [0] * (N + 1)
    prev[0] = 1

    for row in range(1, N + 1):
        curr[0] = 0
        for k in range(1, row + 1):
            v = curr[k-1] + prev[row-k]
            if v >= MOD: v -= MOD
            curr[k] = v
        prev, curr = curr, prev

    return str(prev[N])

if __name__ == '__main__':
    print(solve())
