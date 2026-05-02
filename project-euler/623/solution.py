def solve():
    MOD = 1000000007
    N = 2000
    maxD = (N - 1) // 5

    nxt = [0] * (N + 1)
    cur = [0] * (N + 1)

    for d in range(maxD, -1, -1):
        S = N - 5 * d
        cur = [0] * (N + 1)
        maxK = S - 2
        conv = [0] * (maxK + 1) if maxK >= 0 else []
        for s in range(1, S + 1):
            val = 0
            if s == 1: val += d
            if s >= 6: val += nxt[s-5]
            if s >= 4 and s - 2 < len(conv): val += conv[s-2] % MOD
            cur[s] = val % MOD
            if maxK < s + 1: continue
            u_max = min(s, maxK - s)
            for u in range(1, u_max + 1):
                add = cur[s] * cur[u]
                if u != s: add *= 2
                conv[s + u] += add
        nxt = cur[:]

    pref = [0] * (N + 1)
    for s in range(1, N + 1):
        pref[s] = (pref[s-1] + nxt[s]) % MOD

    return str(pref[N])

if __name__ == '__main__':
    print(solve())
