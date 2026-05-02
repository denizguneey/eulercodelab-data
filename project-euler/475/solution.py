def solve():
    MOD = 1000000007
    musicians = 600

    def mod_pow(base, exp):
        r = 1; base %= MOD
        while exp > 0:
            if exp & 1: r = r * base % MOD
            base = base * base % MOD; exp >>= 1
        return r

    n = musicians // 12
    m = 3 * n  # quartets
    t = 4 * n  # trios

    comb = [[0]*4 for _ in range(m+1)]
    for i in range(m+1):
        comb[i][0] = 1
        if i >= 1: comb[i][1] = i
        if i >= 2: comb[i][2] = i*(i-1)//2
        if i >= 3: comb[i][3] = i*(i-1)*(i-2)//6

    picks = []
    for x0 in range(4):
        for x1 in range(4-x0):
            for x2 in range(4-x0-x1):
                x3 = 3-x0-x1-x2
                picks.append((x0, x1, x2, x3))

    def pack(c0,c1,c2,c3): return (c0<<24)|(c1<<16)|(c2<<8)|c3

    cur = {pack(m,0,0,0): 1}
    for step in range(t):
        nxt = {}
        for key, ways in cur.items():
            c0=(key>>24)&0xFF; c1=(key>>16)&0xFF; c2=(key>>8)&0xFF; c3=key&0xFF
            for x0,x1,x2,x3 in picks:
                if x0>c0 or x1>c1 or x2>c2 or x3>c3: continue
                nc0=c0-x0; nc1=c1-x1+x0; nc2=c2-x2+x1; nc3=c3-x3+x2
                wp = comb[c0][x0]*comb[c1][x1]%MOD*comb[c2][x2]%MOD*comb[c3][x3]%MOD
                add = ways * wp % MOD
                nk = pack(nc0,nc1,nc2,nc3)
                nxt[nk] = (nxt.get(nk, 0) + add) % MOD
        cur = nxt

    mc = cur.get(pack(0,0,0,0), 0)
    aqm = mod_pow(24, m)
    ft = 1
    for i in range(2, t+1): ft = ft * i % MOD
    ift = mod_pow(ft, MOD-2)
    return str(mc * aqm % MOD * ift % MOD)

if __name__ == '__main__':
    print(solve())
