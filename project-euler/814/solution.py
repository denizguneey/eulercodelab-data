def solve():
    MOD = 998244353
    n = 1000; cols = 2*n; target = n
    L, R, V = 0, 1, 2

    def swap_low2(mask): return ((mask&1)<<1)|((mask>>1)&1)

    def build_trans(last_col):
        grouped = [[] for _ in range(4)]
        for inp in range(4):
            cnt = [[0]*3 for _ in range(4)]
            it, ib = inp&1, (inp>>1)&1
            for top in range(3):
                for bot in range(3):
                    d = 0
                    if top == L and it: d += 1
                    if bot == L and ib: d += 1
                    if top == V and bot == V: d += 1
                    out = 0
                    if top == R: out |= 1
                    if bot == R: out |= 2
                    if last_col: out = swap_low2(out)
                    cnt[out][d] += 1
            for out in range(4):
                for d in range(3):
                    if cnt[out][d] > 0:
                        grouped[inp].append((out, d, cnt[out][d]))
        return grouped

    tm = build_trans(False); tl = build_trans(True)
    total = 0

    for init in range(4):
        dp = [[0]*(target+1) for _ in range(4)]
        dp[init][0] = 1
        for col in range(cols - 1):
            nxt = [[0]*(target+1) for _ in range(4)]
            for inp in range(4):
                cur = dp[inp]
                for out, delta, ways in tm[inp]:
                    for k in range(target - delta + 1):
                        if cur[k] == 0: continue
                        nxt[out][k+delta] = (nxt[out][k+delta] + cur[k]*ways) % MOD
            dp = nxt
        # last column
        nxt = [[0]*(target+1) for _ in range(4)]
        for inp in range(4):
            cur = dp[inp]
            for out, delta, ways in tl[inp]:
                for k in range(target - delta + 1):
                    if cur[k] == 0: continue
                    nxt[out][k+delta] = (nxt[out][k+delta] + cur[k]*ways) % MOD
        total = (total + nxt[init][target]) % MOD

    return str(total)

if __name__ == '__main__':
    print(solve())
