def solve():
    MOD = 998244353
    n = 10000

    def addmod(a, b):
        s = a + b
        return s - MOD if s >= MOD else s
    def submod(a, b):
        s = a - b
        return s + MOD if s < 0 else s

    M = max(100, 40*n)
    phi = list(range(M+1))
    for i in range(2, M+1):
        if phi[i] == i:
            for j in range(i, M+1, i): phi[j] -= phi[j]//i

    deg = [0]*(M+1)
    if M >= 1: deg[1] = 1
    if M >= 2: deg[2] = 1
    for m in range(3, M+1): deg[m] = phi[m]//2

    # build chain1
    tail_weights = []
    prefix = 0; m = 4
    while m < len(deg):
        d = deg[m]
        if d > n: break
        prefix += d
        t = prefix + 1
        if t > n: break
        tail_weights.append(t)
        m *= 2

    G = [0]*(n+1); G[0] = 1
    H = [0]*(n+1); H[0] = 1
    for t in tail_weights:
        for k in range(t, n+1): G[k] = addmod(G[k], G[k-t])
    for t in tail_weights:
        for k in range(t, n+1): H[k] = submod(H[k], H[k-t])

    inv2 = (MOD+1)//2
    S = [0]*(n+1)
    for k in range(n+1):
        val = G[k] + H[k]
        if k > 0: val += G[k-1] - H[k-1]
        val %= MOD
        S[k] = val * inv2 % MOD
    for k in range(1, n+1): S[k] = addmod(S[k], S[k-1])
    for k in range(2, n+1): S[k] = addmod(S[k], S[k-2])

    dp = S
    for b in range(3, M+1, 2):
        if deg[b] > n: continue
        prefix = 0; m = b
        while m <= M:
            d = deg[m]
            if d > n: break
            prefix += d
            if prefix > n: break
            w = prefix
            for k in range(w, n+1): dp[k] = addmod(dp[k], dp[k-w])
            m *= 2

    return str(dp[n])

if __name__ == '__main__':
    print(solve())
