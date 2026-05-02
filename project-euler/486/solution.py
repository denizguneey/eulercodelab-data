def solve():
    MOD = 87654321; LIMIT = 10**18
    C = [182,216,252,286,318,350]; PPF = [9,1997,4877]

    def mm(a,b,m): return a*b%m
    def pm(b,e,m):
        r=1; b%=m
        while e>0:
            if e&1: r=r*b%m
            b=b*b%m; e>>=1
        return r
    def gcd(a,b):
        while b: a,b=b,a%b
        return a
    def lcm(a,b): return a//gcd(a,b)*b

    def euler_phi(n):
        r=n; x=n
        p=2
        while p*p<=x:
            if x%p==0:
                while x%p==0: x//=p
                r-=r//p
            p+=1
        if x>1: r-=r//x
        return r

    def mult_order(a, m):
        if gcd(a,m)!=1: return 0
        o=euler_phi(m); x=o
        p=2
        while p*p<=x:
            if x%p==0:
                while o%p==0 and pm(a,o//p,m)==1: o//=p
            p+=1
            while x%p==0: x//=p
        if x>1:
            while o%x==0 and pm(a,o//x,m)==1: o//=x
        return o

    def mod_inv(a,m):
        t,nt,r,nr=0,1,m,a%m
        while nr:
            q=r//nr; t,nt=nt,t-q*nt; r,nr=nr,r-q*nr
        if r!=1: return 0
        return t%m

    def crt_merge(a,m1,b,m2):
        g=gcd(m1,m2); m1g=m1//g; m2g=m2//g; lc=m1g*m2
        inv=mod_inv(m1g%m2g,m2g)
        diff=b-a; dg=diff//g
        k=dg%m2g; t=k*inv%m2g
        x=(a+m1*t)%lc
        return x,lc

    # Compute mod data
    mod_data = []
    for pp in PPF:
        o = mult_order(64%pp, pp); period = lcm(pp, o)
        residues = [[] for _ in range(6)]
        for u in range(6):
            lhs_mul = pm(2, 10+u, pp)
            p64 = 1%pp; rhs = C[u]%pp
            res = []
            for t in range(period):
                if mm(lhs_mul, p64, pp) == rhs: res.append(t)
                p64 = mm(p64, 64%pp, pp); rhs = (rhs+200)%pp
            residues[u] = res
        mod_data.append((pp, period, residues))

    # Combine residues for each u
    global_period = 1
    global_res = [None]*6
    for u in range(6):
        r1997 = mod_data[1][2][u]; p1997 = mod_data[1][1]
        r4877 = mod_data[2][2][u]; p4877 = mod_data[2][1]
        r9 = mod_data[0][2][u]; p9 = mod_data[0][1]
        # CRT merge 1997 and 4877
        combined12 = []
        even4877 = [x for x in r4877 if x%2==0]
        odd4877 = [x for x in r4877 if x%2==1]
        for a in r1997:
            cands = even4877 if a%2==0 else odd4877
            for b in cands:
                g = gcd(p1997, p4877)
                if (b-a)%g != 0: continue
                m12, lc12 = crt_merge(a, p1997, b, p4877)
                combined12.append((m12, lc12))
        # merge with mod9
        combined = set()
        for m12, lc12 in combined12:
            for c in r9:
                g = gcd(lc12, p9)
                if (c-m12)%g != 0: continue
                m, lc = crt_merge(m12, lc12, c, p9)
                combined.add(m)
                global_period = lc
        global_res[u] = sorted(combined)

    # Small cases (n=5..8)
    def compute_f5_prefix():
        f = [0]*21; states = [(0, 1)]
        for n in range(1, 21):
            nc = [0]*32
            for bits,cnt in states:
                for add in range(2):
                    cb = (bits<<1)|add; ok=True
                    if n>=5:
                        v5=cb&31; b0=v5&1; b1=(v5>>1)&1; b3=(v5>>3)&1; b4=(v5>>4)&1
                        if b0==b4 and b1==b3: ok=False
                    if ok and n>=6:
                        v6=cb&63
                        if (v6&1)==((v6>>5)&1) and ((v6>>1)&1)==((v6>>4)&1) and ((v6>>2)&1)==((v6>>3)&1): ok=False
                    if not ok: continue
                    nb = (cb&((1<<n)-1)) if n<=5 else (cb&31)
                    nc[nb] += cnt
            states = [(m,nc[m]) for m in range(32 if n>5 else (1<<n)) if nc[m]>0]
            total_a = sum(c for _,c in states)
            total_str = 1<<n if n<63 else 0
            f[n] = f[n-1] + (total_str - total_a)
        return f
    f5 = compute_f5_prefix()
    f5m = [x%MOD for x in f5]

    # Count
    import bisect
    def count_res(residues, period, t_limit):
        if not residues: return 0
        full = t_limit // period; rem = t_limit % period
        tail = bisect.bisect_right(residues, rem)
        return full*len(residues)+tail

    answer = 0
    for n in range(5, min(LIMIT, 8)+1):
        if f5m[n] == 0: answer += 1
    if LIMIT >= 9:
        for u in range(6):
            n0 = 9+u
            if n0 > LIMIT: continue
            t_limit = (LIMIT-n0)//6
            answer += count_res(global_res[u], global_period, t_limit)
    return str(answer)

if __name__ == '__main__':
    print(solve())
