import math

def solve():
    MOD = 10**9+7; N = 10**9

    def isqrt(x):
        r=int(math.isqrt(x))
        while (r+1)*(r+1)<=x: r+=1
        while r*r>x: r-=1
        return r

    def isqrt_big(x):
        if x<=0: return 0
        r=int(math.isqrt(x))
        while (r+1)*(r+1)<=x: r+=1
        while r*r>x: r-=1
        return r

    def floor_sqrt3_mul(n):
        return isqrt_big(3*n*n)

    def floor_div_sqrt3(n,m):
        nn=n*n; den=3*m*m
        t=isqrt_big(nn//den)
        while den*(t+1)*(t+1)<=nn: t+=1
        while den*t*t>nn: t-=1
        return t

    def div_sum(n):
        res=0; i=1
        while i<=n:
            q=n//i; j=n//q
            res+=q*(j-i+1); i=j+1
        return res

    def tri(n): return n*(n+1)//2

    def floor_qsqrt3(a,b,c):
        if b==0: return a//c if (a>=0 or a%c==0) else -((-a+c-1)//c)
        fb=isqrt_big(3*b*b)
        x=(a+fb)//c
        bb3=3*b*b
        while True:
            y=(x+1)*c-a
            if y<=0 or y*y<=bb3: x+=1
            else: break
        while True:
            y=x*c-a
            if y<=0 or y*y<=bb3: break
            x-=1
        return x

    def beatty_sum(a,b,c,n):
        res=0; sign=1
        while n>0:
            f=floor_qsqrt3(a,b,c)
            if f>1:
                res+=sign*(f-1)*tri(n)
                a-=(f-1)*c
            m=floor_qsqrt3(a*n,b*n,c)
            res+=sign*tri(m)
            n=m-n
            if n<=0: break
            # alpha/(alpha-1): alpha = (a+b*sqrt3)/c
            ac=a-c
            A=a*ac-3*b*b; B=-b*c; D=ac*ac-3*b*b
            if D<0: A,B,D=-A,-B,-D
            if B<0: A,B=-A,-B
            from math import gcd
            g=gcd(gcd(abs(A),abs(B)),abs(D))
            if g>1: A//=g; B//=g; D//=g
            a,b,c=A,B,D; sign=-sign
        return res

    def beatty_sqrt3(cv,n):
        if n<=0: return 0
        return beatty_sum(0,cv,1,n)

    def linear_sieve(n):
        spf=[0]*(n+1); mu=[0]*(n+1); primes=[]; mu[1]=1; spf[1]=1
        for i in range(2,n+1):
            if spf[i]==0:
                spf[i]=i; primes.append(i); mu[i]=-1
            for p in primes:
                if i*p>n: break
                spf[i*p]=p
                if i%p==0: mu[i*p]=0; break
                mu[i*p]=-mu[i]
        return spf,mu

    def sf_divs(n,spf):
        divs=[[] for _ in range(n+1)]
        divs[1]=[(1,1)]
        for x in range(2,n+1):
            v=x; ps=[]
            while v>1:
                p=spf[v]; ps.append(p)
                while v%p==0: v//=p
            k=len(ps); dd=[]
            for mask in range(1<<k):
                d=1; bc=0
                for i in range(k):
                    if mask&(1<<i): d*=ps[i]; bc+=1
                dd.append((d,-1 if bc&1 else 1))
            divs[x]=dd
        return divs

    def all_divs(n,spf):
        divs=[[] for _ in range(n+1)]
        divs[1]=[1]
        for x in range(2,n+1):
            v=x; p=spf[v]; e=0
            while v%p==0: v//=p; e+=1
            base=divs[v]; out=[]
            pe=1
            for i in range(e+1):
                for d in base: out.append(d*pe)
                pe*=p
            divs[x]=out
        return divs

    M=N//2; L=floor_div_sqrt3(M,1); V_strip=isqrt_big(L)
    X=N//4; V_hex=isqrt_big(X) if X>0 else 0
    mx=max(1,V_strip,V_hex)
    spf,mu=linear_sieve(mx)
    sfd=sf_divs(mx,spf); ald=all_divs(mx,spf)

    base=2*div_sum(M)

    s1=0; s2=0; diag1=0; diag2=0
    for v in range(1,V_strip+1):
        Umax=L//v
        for d in ald[v]:
            m=v//d; hi=Umax//d
            if hi<m: continue
            w=N//(2*d); lo=m-1
            cnt=0; sm=0
            for q,muq in sfd[m]:
                cnt+=muq*(hi//q-lo//q)
                hiq=hi//q; loq=lo//q
                if hiq>0:
                    c=v*q
                    sm+=muq*(beatty_sqrt3(c,hiq)-beatty_sqrt3(c,loq))
            s1+=w*cnt; s2+=sm
        diag1+=N//(2*v); diag2+=floor_sqrt3_mul(v)

    S1=2*s1-diag1; S2=2*s2-diag2
    strip=base+4*(S1-S2)

    # Hex sum
    d_cache={}
    def D(n2):
        if n2<=0: return 0
        if n2 in d_cache: return d_cache[n2]
        v=div_sum(n2); d_cache[n2]=v; return v

    def cnt_mod3(lo,hi,r):
        if hi<lo: return 0
        rem=lo%3
        if rem<0: rem+=3
        delta=(r-rem)%3
        first=lo+delta
        if first>hi: return 0
        return (hi-first)//3+1

    extra=0
    for v in range(1,V_hex+1):
        disc0=4*X-3*v*v
        if disc0<=0: break
        Umax=(-v+isqrt_big(disc0))//2; u=v+1
        sfv=sfd[v]; vm=v%3
        while u<=Umax:
            t=u*u+u*v+v*v; q=X//t
            if q==0: break
            T=X//q
            disc=4*T-3*v*v
            uhi=min((-v+isqrt_big(disc))//2,Umax)
            lo1=u-1; total=0
            for d,mud in sfv:
                total+=mud*(uhi//d-lo1//d)
            if vm!=0:
                bad=0
                for d,mud in sfv:
                    dm3=d%3; inv=1 if dm3==1 else 2
                    tlo=(u+d-1)//d; thi=uhi//d
                    rr=(vm*inv)%3
                    bad+=mud*cnt_mod3(tlo,thi,rr)
                total-=bad
            if total!=0: extra+=total*D(q)
            u=uhi+1

    H=D(X)+2*extra
    total=strip-4*H
    return str(total%MOD)

if __name__=='__main__':
    print(solve())
