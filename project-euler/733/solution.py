import bisect

def solve():
    MOD = 1000000007; SEQ_MOD = 10000019; n = 1000000
    # Generate sequence
    a = [0]*n; cur = 1
    for i in range(n): cur = cur * 153 % SEQ_MOD; a[i] = cur
    # Coordinate compression
    s = sorted(set(a)); m = len(s)
    rank = [bisect.bisect_left(s, x)+1 for x in a]
    # Fenwick pair trees (count, sum)
    def make_fw(): return [[0]*(m+1), [0]*(m+1)]
    def fw_query(fw, idx):
        c = sm = 0
        while idx > 0:
            c = (c + fw[0][idx]) % MOD; sm = (sm + fw[1][idx]) % MOD
            idx -= idx & (-idx)
        return c, sm
    def fw_update(fw, idx, ac, asum):
        while idx <= m:
            fw[0][idx] = (fw[0][idx] + ac) % MOD; fw[1][idx] = (fw[1][idx] + asum) % MOD
            idx += idx & (-idx)

    fw = [make_fw() for _ in range(3)]; ans = 0
    for i in range(n):
        r = rank[i]; x = a[i]
        c1 = 1; s1 = x
        c1p, s1p = fw_query(fw[0], r-1)
        c2 = c1p; s2 = (s1p + x*c2) % MOD
        c2p, s2p = fw_query(fw[1], r-1)
        c3 = c2p; s3 = (s2p + x*c3) % MOD
        c3p, s3p = fw_query(fw[2], r-1)
        s4 = (s3p + x*c3p) % MOD
        ans = (ans + s4) % MOD
        fw_update(fw[0], r, c1, s1)
        fw_update(fw[1], r, c2, s2)
        fw_update(fw[2], r, c3, s3)
    return str(ans)

if __name__ == '__main__':
    print(solve())
