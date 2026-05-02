def solve():
    MOD = 1234567891
    N = 5000
    W = N + 1

    part = [0]*(W*W)
    part[0] = 1
    for u in range(1, N+1):
        part[u*W] = 1
        for v in range(1, N+1):
            val = part[(u-1)*W + v]
            if v >= u: val = (val + part[u*W + v - u]) % MOD
            part[u*W + v] = val

    g = [0]*(W*W)
    for t in range(N+1):
        for v in range(t+1):
            g[t*W + v] = part[(t-v)*W + v]
    del part

    agg = [0]*W; contrib_ge2 = 0
    for vA in range(N+1):
        av = vA - 2
        if av >= 0:
            for t in range(av, N+1):
                agg[t] = (agg[t] + g[t*W + av]) % MOD
        pref = [0]*W; run = 0
        for t in range(N+1):
            run = (run + agg[t]) % MOD; pref[t] = run
        for tA in range(vA, N+1):
            ga = g[tA*W + vA]
            if ga == 0: continue
            contrib_ge2 = (contrib_ge2 + ga * pref[N - tA]) % MOD

    contrib_eq1 = 0
    for vA in range(1, N+1):
        vB = vA - 1
        esum = osum = 0
        pe = [0]*W; po = [0]*W
        for t in range(N+1):
            gb = g[t*W + vB]
            if t & 1: osum = (osum + gb) % MOD
            else: esum = (esum + gb) % MOD
            pe[t] = esum; po[t] = osum
        for tA in range(vA, N+1):
            ga = g[tA*W + vA]
            if ga == 0: continue
            lim = N - tA
            wb = po[lim] if tA & 1 else pe[lim]
            contrib_eq1 = (contrib_eq1 + ga * wb) % MOD

    return str((contrib_ge2 + contrib_eq1) % MOD)

if __name__ == '__main__':
    print(solve())
