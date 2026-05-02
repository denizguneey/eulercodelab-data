import math

def solve():
    MOD = 83456729

    def mul_mod(a, b): return a*b%MOD
    def add_mod(a, b):
        s = a+b; return s-MOD if s>=MOD else s
    def sub_mod(a, b):
        s = a-b; return s+MOD if s<0 else s
    def mod_pow(a, e):
        r = 1; a %= MOD
        while e > 0:
            if e&1: r=r*a%MOD
            a=a*a%MOD; e >>= 1
        return r
    def mod_inv(a): return mod_pow(a, MOD-2)

    def det_mod(A):
        n = len(A)
        if n == 0: return 1
        if n == 1: return A[0][0]%MOD
        A = [row[:] for row in A]; ri = 1
        for i in range(n-2):
            piv = -1
            for r in range(i, n):
                if A[r][i]%MOD: piv=r; break
            if piv<0: return 0
            if piv!=i: A[piv],A[i]=A[i],A[piv]; ri=MOD-ri if ri else 0
            Aii = A[i][i]%MOD; ri = mul_mod(ri, mod_pow(Aii, n-i-2))
            for r in range(i+1,n):
                x = A[r][i]%MOD; A[r][i]=0
                for c in range(i+1,n): A[r][c]=sub_mod(mul_mod(Aii,A[r][c]),mul_mod(x,A[i][c]))
        last = sub_mod(mul_mod(A[n-2][n-2],A[n-1][n-1]),mul_mod(A[n-2][n-1],A[n-1][n-2]))
        return mul_mod(last, mod_inv(ri))

    def perm_mod(A, binom):
        n = len(A)
        if n == 0: return 1
        cc = {}
        for col in range(n):
            mask = 0
            for r in range(n):
                if A[r][col]: mask |= 1<<r
            cc.setdefault(mask, []).append(col)
        classes = []
        for inds in cc.values():
            if len(inds) >= 3: classes.append(inds)
            else:
                for idx in inds: classes.append([idx])
        classes.sort(key=len)
        order = [c for cl in classes for c in cl]
        B = [[A[r][order[c]] for c in range(n)] for r in range(n)]
        csz = [len(cl) for cl in classes]
        be = 0; sc = 0
        while sc < len(csz) and be+csz[sc] < 10: be += csz[sc]; sc += 1
        bs = 1<<be
        hcs = csz[sc:]; hco = []; off = be
        for s in hcs: hco.append(off); off += s
        result = [0]
        hmask = [0]*n
        pc = [0]*bs
        for s in range(1,bs): pc[s] = pc[s>>1]+(s&1)
        def rec(ci, tw, ho):
            if ci == len(hcs):
                for state in range(bs):
                    term = tw
                    for r in range(n):
                        sm = 0
                        for c in range(be):
                            if (state>>c)&1: sm += B[r][c]
                        for c in range(be, n):
                            if hmask[c]: sm += B[r][c]
                        term = mul_mod(term, sm)
                        if term == 0: break
                    if (pc[state]+ho)&1 and term: term = MOD-term
                    result[0] = add_mod(result[0], term)
                return
            sz = hcs[ci]; base = hco[ci]
            for ones in range(sz+1):
                for j in range(sz): hmask[base+j] = 1 if j>=sz-ones else 0
                w2 = mul_mod(tw, binom[sz][ones])
                rec(ci+1, w2, ho+ones)
        rec(0, 1, 0)
        r = result[0]
        if n&1: r = MOD-r if r else 0
        return r

    nn = 34; half = nn//2
    even_idx = list(range(1, nn, 2)); odd_idx = list(range(2, nn+1, 2))
    Bm = [[1 if math.gcd(even_idx[r], odd_idx[c])==1 else 0 for r in range(half)] for c in range(half)]
    binom = [[0]*(half+1) for _ in range(half+1)]
    for i in range(half+1):
        binom[i][0] = 1
        for j in range(1, i+1): binom[i][j] = binom[i-1][j-1]+binom[i-1][j]

    def row_classes(M):
        groups = {}
        for i in range(len(M)):
            mask = sum(1<<j for j in range(len(M[i])) if M[i][j])
            groups.setdefault(mask, []).append(i)
        return [(idxs[0], len(idxs)) for idxs in groups.values()]

    rw = row_classes(Bm)
    # Remove one row
    rm = -1
    for i in range(len(rw)):
        if rw[i][1] == 1: rm=i; break
    if rm >= 0: rw = rw[:rm]+rw[rm+1:]
    else: rw = [(rw[0][0],rw[0][1]-1)]+rw[1:]

    BT = [[Bm[c][r] for c in range(half)] for r in range(half)]
    cw = row_classes(BT)

    from itertools import combinations
    result = 0
    for inc in range(half):
        for rp in combinations(range(len(rw)), inc):
            rways = 1; irows = []
            for idx in rp: rways *= rw[idx][1]; irows.append(rw[idx][0])
            inr = set(irows)
            nrows = [r for r in range(half) if r not in inr]
            for cp in combinations(range(len(cw)), inc):
                ways = rways; icols = []
                for idx in cp: ways *= cw[idx][1]; icols.append(cw[idx][0])
                dm = [[Bm[irows[i]][icols[j]] for j in range(inc)] for i in range(inc)]
                dv = det_mod(dm)
                if dv == 0: continue
                dv = mul_mod(dv, dv)
                if inc&1: dv = MOD-dv if dv else 0
                inc2 = set(icols); ncols = [c for c in range(half) if c not in inc2]
                rest = half-inc
                pm = [[Bm[nrows[i]][ncols[j]] for j in range(rest)] for i in range(rest)]
                pv = perm_mod(pm, binom); pv = mul_mod(pv, pv)
                result = add_mod(result, mul_mod(ways%MOD, mul_mod(dv, pv)))
    return str(result)

if __name__ == '__main__':
    print(solve())
