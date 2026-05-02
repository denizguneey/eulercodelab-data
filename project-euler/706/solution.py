def solve():
    MOD = 1000000007
    d = 100000; STATES = 243

    def encode(pref, n0, n1, n2, fmod):
        return ((((pref*3+n0)*3+n1)*3+n2)*3+fmod)

    # Build transitions
    nxt = [[0]*3 for _ in range(STATES)]
    for sid in range(STATES):
        x = sid; fmod = x%3; x //= 3; n2 = x%3; x //= 3; n1 = x%3; x //= 3; n0 = x%3; x //= 3; pref = x%3
        for cls in range(3):
            np = (pref+cls)%3
            ncnt = [n0, n1, n2]; add = ncnt[np]
            nf = (fmod+add)%3; ncnt[np] = (ncnt[np]+1)%3
            nxt[sid][cls] = encode(np, ncnt[0], ncnt[1], ncnt[2], nf)

    dp = [0]*STATES
    dp[encode(0, 1, 0, 0, 0)] = 1

    for pos in range(1, d+1):
        ndp = [0]*STATES
        mult = [3,3,3] if pos == 1 else [4,3,3]
        for sid in range(STATES):
            w = dp[sid]
            if w == 0: continue
            for cls in range(3):
                to = nxt[sid][cls]
                ndp[to] = (ndp[to] + w * mult[cls]) % MOD
        dp = ndp

    ans = 0
    for sid in range(STATES):
        if sid % 3 == 0: ans = (ans + dp[sid]) % MOD
    return str(ans)

if __name__ == '__main__':
    print(solve())
