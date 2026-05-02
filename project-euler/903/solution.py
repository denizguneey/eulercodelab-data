def solve():
    MOD = 1000000007; n = 1000000

    def am(a, b):
        s = a+b; return s-MOD if s>=MOD else s
    def sm(a, b): return a-b if a>=b else a+MOD-b
    def mm(a, b): return a*b%MOD
    def mp(a, e):
        r = 1; a %= MOD
        while e > 0:
            if e&1: r=r*a%MOD
            a=a*a%MOD; e >>= 1
        return r
    def mi(a): return mp(a, MOD-2)

    # Inverses
    inv = [0]*(n+1)
    if n >= 1: inv[1] = 1
    for i in range(2, n+1): inv[i] = (MOD - MOD//i * inv[MOD%i] % MOD) % MOD

    # Harmonics
    H = [0]*(n+1); H2 = [0]*(n+1)
    for i in range(1, n+1):
        H[i] = am(H[i-1], inv[i]); H2[i] = am(H2[i-1], mm(inv[i], inv[i]))

    # Phi via linear sieve
    phi = [0]*(n+1); isComp = [False]*(n+1); primes = []; phi[1] = 1
    for i in range(2, n+1):
        if not isComp[i]: primes.append(i); phi[i] = i-1
        for p in primes:
            if p*i > n: break
            isComp[p*i] = True
            if i%p == 0: phi[p*i] = phi[i]*p; break
            else: phi[p*i] = phi[i]*(p-1)

    # Prefix sums of phi(i)/i^2
    pref = [0]*(n+1)
    for i in range(1, n+1):
        inv_i2 = mm(inv[i], inv[i])
        pref[i] = am(pref[i-1], mm(phi[i], inv_i2))

    def Tval(m):
        h = H[m]; t = mm(h, h); return sm(t, H2[m])

    # S(n) = sum_{d} phi(d)/d^2 * T(n/d) via block decomposition
    S = 0; l = 1
    while l <= n:
        q = n//l; r = n//q
        sumF = sm(pref[r], pref[l-1])
        S = (S + mm(sumF, Tval(q))) % MOD
        l = r+1

    Hn = H[n]; inv2 = inv[2]; inv_n = inv[n]; inv_nm1 = inv[n-1]; inv_d = inv[n-2]

    pF = mm(Hn, inv_n)
    pO = mm(sm(1, pF), inv_nm1)
    pSW = mm(mm(mm(H[n//2], inv2), inv_n), inv_nm1)
    pFF = mm(mm(am(sm(n%MOD, Hn), S), inv_n), inv_nm1)

    K1 = mm(am(sm(sm(pF, pFF), pO), pSW), inv_d)
    K0 = pFF
    K0 = am(K0, mm(sm(pF, pFF), mm((n-3)%MOD, inv_d)))
    K0 = am(K0, mm(sm(pO, pSW), mm((n-1)%MOD, inv_d)))
    K0 = am(K0, inv2); K0 = sm(K0, pF); K0 = sm(K0, pO)
    K0 = am(K0, mm(am(pFF, pSW), inv2))

    fact = [1]*(n+1)
    for i in range(1, n+1): fact[i] = mm(fact[i-1], i)

    term1_const = mm(sm(n%MOD, Hn), inv2)
    A_const = mm(sm(Hn, 1), inv_nm1)
    C1 = sm(A_const, K0)

    total = 0
    for j in range(1, n+1):
        m = j-1; mM = m%MOD
        tri = mM*(mM+1)%MOD*inv2%MOD
        Ea = (term1_const + mM*C1 - K1*tri) % MOD
        if Ea < 0: Ea += MOD
        total += Ea*fact[n-j]%MOD
        if total >= MOD*1000: total %= MOD

    total %= MOD
    E_rank = am(1, total)
    ans = fact[n]*fact[n]%MOD*E_rank%MOD
    return str(ans)

if __name__ == '__main__':
    print(solve())
