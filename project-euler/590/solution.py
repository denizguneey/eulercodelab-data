def solve():
    MOD = 10**9; N = 50000
    P2T = 9; P2C = 1562500  # ord_{5^9}(2)

    def sieve(n):
        ip=[True]*(n+1); ip[0]=ip[1]=False
        for i in range(2,int(n**0.5)+1):
            if ip[i]:
                for j in range(i*i,n+1,i): ip[j]=False
        return [i for i in range(2,n+1) if ip[i]]

    def pm(b,e,m):
        r=1; b%=m
        while e>0:
            if e&1: r=r*b%m
            b=b*b%m; e>>=1
        return r

    def cap9(a,b):
        p=a*b; return min(p,P2T)

    # Pre-build pow2 tables
    small=[1]*P2T
    for i in range(1,P2T): small[i]=2*small[i-1]%MOD
    cyc=[0]*P2C; v=2*small[P2T-1]%MOD
    for i in range(P2C): cyc[i]=v; v=2*v%MOD

    def pow2_mod(em, ec):
        if ec<P2T: return small[ec]
        idx=em
        if idx>=P2T: idx-=P2T
        else: idx+=P2C-P2T
        return cyc[idx]

    # d_list: for each prime p <= N, d = floor(log_p(N)) + 1
    primes = sieve(N)
    d_list = []
    for p in primes:
        d=0; x=N
        while x>0: x//=p; d+=1
        d_list.append(d)

    # Group by d value
    from collections import Counter
    cnt = Counter(d_list)
    groups = sorted(cnt.items(), key=lambda x: (-x[1], -x[0]))

    def build_binom(n2):
        row=[0]*(n2+1); row[0]=1
        for i in range(1,n2+1):
            for k in range(i,0,-1): row[k]=(row[k]+row[k-1])%MOD
        return row

    def build_group(d,count):
        binom=build_binom(count)
        pdm=[1]*(count+1); pd1m=[1]*(count+1)
        pdc=[1]*(count+1); pd1c=[1]*(count+1)
        for k in range(1,count+1):
            pdm[k]=pdm[k-1]*d%P2C; pd1m[k]=pd1m[k-1]*(d-1)%P2C
            pdc[k]=cap9(pdc[k-1],d); pd1c[k]=cap9(pd1c[k-1],d-1)
        choices=[]
        for i in range(count+1):
            c=binom[i]; coef=(MOD-c)%MOD if i&1 else c
            em=pd1m[i]*pdm[count-i]%P2C
            ec=cap9(pd1c[i],pdc[count-i])
            choices.append((coef,em,ec))
        return choices

    # Build rest states from groups[1:]
    group_choices = [build_group(d,c) for d,c in groups]
    states = [(1,1,1)]  # (coef, exp_mod, exp_cap)
    for gi in range(1,len(groups)):
        nxt=[]
        for sc,se,sec in states:
            for cc,ce,cec in group_choices[gi]:
                nc=sc*cc%MOD
                if nc==0: continue
                ne=se*ce%P2C; nec=cap9(sec,cec)
                nxt.append((nc,ne,nec))
        states=nxt

    # Combine with lead group
    total=0
    for pc,pe,pec in group_choices[0]:
        for sc,se,sec in states:
            c=pc*sc%MOD
            if c==0: continue
            ec=cap9(pec,sec); em=pe*se%P2C
            v=pow2_mod(em,ec)
            total=(total+c*v)%MOD
    return str(total%MOD)

if __name__=='__main__':
    print(solve())
