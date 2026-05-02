def solve():
    MOD = 989898989
    n = 9898
    span = 4*n + 4; size = 2*span+1; shift = span
    cur = [0]*size; cur[shift] = 1

    for step in range(1, n+1):
        nxt = [0]*size
        lo = shift - 4*step; hi = shift + 4*step
        for i in range(lo, hi+1):
            v = cur[i-4] + cur[i+4]
            if v >= MOD: v -= MOD
            v += cur[i-1]
            if v >= MOD: v -= MOD
            v += cur[i+1]
            if v >= MOD: v -= MOD
            nxt[i] = v
        cur = nxt

    return str(cur[shift])

if __name__ == '__main__':
    print(solve())
