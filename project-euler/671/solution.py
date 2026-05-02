def solve():
    MOD = 1000004321

    def pm(b,e):
        r=1; b%=MOD
        while e>0:
            if e&1: r=r*b%MOD
            b=b*b%MOD; e>>=1
        return r
    def mi(x): return pm((x%MOD+MOD)%MOD,MOD-2)

    def build_matrix(k):
        states=[]; idx={}
        for rt in range(3):
            for rb in range(3):
                for pv in range(2):
                    for ct in range(k):
                        for cb in range(k):
                            ok=False
                            if pv==1: ok=(rt==0 and rb==0 and ct==cb)
                            else: ok=(ct!=cb)
                            if not ok: continue
                            i=len(states); states.append((rt,rb,pv,ct,cb))
                            idx[(rt,rb,pv,ct,cb)]=i
        S=len(states); adj=[[] for _ in range(S)]
        for i,(rt,rb,pv,ct,cb) in enumerate(states):
            if rt>0 and rb>0: adj[i].append(idx[(rt-1,rb-1,0,ct,cb)]); continue
            if rt>0 and rb==0:
                for lb in range(1,4):
                    for cb2 in range(k):
                        if cb2==ct or cb2==cb: continue
                        adj[i].append(idx[(rt-1,lb-1,0,ct,cb2)])
                continue
            if rt==0 and rb>0:
                for lt in range(1,4):
                    for ct2 in range(k):
                        if ct2==ct or ct2==cb: continue
                        adj[i].append(idx[(lt-1,rb-1,0,ct2,cb)])
                continue
            for c in range(k):
                if c==ct or c==cb: continue
                adj[i].append(idx[(0,0,1,c,c)])
            if pv==1:
                for lt in range(1,4):
                    for lb in range(1,4):
                        for ct2 in range(k):
                            if ct2==ct: continue
                            for cb2 in range(k):
                                if cb2==cb or cb2==ct2: continue
                                adj[i].append(idx[(lt-1,lb-1,0,ct2,cb2)])
        return S,adj

    def bm(s):
        C=[1]; B=[1]; L=0; m=1; b=1
        for n in range(len(s)):
            d=0
            for i in range(L+1): d=(d+C[i]*s[n-i])%MOD
            if d==0: m+=1; continue
            T=C[:]; coef=d*mi(b)%MOD
            while len(C)<len(B)+m: C.append(0)
            for i in range(len(B)): C[i+m]=(C[i+m]+MOD-coef*B[i]%MOD)%MOD
            if 2*L<=n: L=n+1-L; B=T; b=d; m=1
            else: m+=1
        C.pop(0); return [(MOD-x)%MOD for x in C]

    def lr(init,coef,n):
        L=len(coef)
        if L==0: return 0
        if n<len(init): return init[n]
        def cp(a,b):
            r=[0]*(2*L)
            for i in range(L):
                if a[i]==0: continue
                for j in range(L):
                    if b[j]==0: continue
                    r[i+j]=(r[i+j]+a[i]*b[j])%MOD
            for i in range(2*L-2,L-1,-1):
                if r[i]==0: continue
                for j in range(L): r[i-1-j]=(r[i-1-j]+r[i]*coef[j])%MOD
            return r[:L]
        pol=[0]*L; pol[0]=1; e=[0]*L
        if L==1: e[0]=coef[0]
        else: e[1]=1
        m=n
        while m>0:
            if m&1: pol=cp(pol,e)
            e=cp(e,e); m>>=1
        return sum(pol[i]*init[i] for i in range(L))%MOD

    def build_rec(k):
        S,adj=build_matrix(k)
        # Matrix power via sparse mult, trace sequence
        P=[[0]*S for _ in range(S)]
        for i in range(S): P[i][i]=1
        seq=[S%MOD]; last_L=0; stable=0
        for step in range(1,2001):
            nP=[[0]*S for _ in range(S)]
            for i in range(S):
                for kk in range(S):
                    if P[i][kk]==0: continue
                    for to in adj[kk]: nP[i][to]=(nP[i][to]+P[i][kk])%MOD
            P=nP; tr=sum(P[i][i] for i in range(S))%MOD; seq.append(tr)
            coef=bm(seq); L=len(coef)
            if L==last_L: stable+=1
            else: stable=0; last_L=L
            if L>0 and len(seq)>=2*L+5 and stable>=5: break
        if not coef: coef=[0]
        init=seq[:len(coef)]
        return init,coef

    def factorize(n):
        f=[]; p=2
        while p*p<=n:
            if n%p==0:
                c=0
                while n%p==0: n//=p; c+=1
                f.append((p,c))
            p+=1 if p==2 else 2
        if n>1: f.append((n,1))
        return f

    def gen_divs(facs):
        divs=[(1,1)]
        for p,e in facs:
            nd=[]
            for d,phi in divs:
                pp=1; ph=1
                nd.append((d,phi))
                for i in range(1,e+1):
                    pp*=p; ph=p-1 if i==1 else ph*p
                    nd.append((d*pp,phi*ph))
            divs=nd
        return divs

    k=10; n=10004003002001
    init,coef=build_rec(k)
    facs=factorize(n)
    divs=gen_divs(facs)
    total=0
    for d,phi in divs:
        total=(total+phi%MOD*lr(init,coef,n//d))%MOD
    return str(total*mi(n%MOD)%MOD)

if __name__=='__main__':
    print(solve())
