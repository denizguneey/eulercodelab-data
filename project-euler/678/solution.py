import math

def solve():
    N = 10**18

    def isqrt(n):
        r=int(math.isqrt(n))
        while (r+1)*(r+1)<=n: r+=1
        while r*r>n: r-=1
        return r

    def pow_lim(b,e):
        v=1
        for _ in range(e):
            if v>N//b: return N+1
            v*=b
        return v

    def spf_sieve(n):
        s=list(range(n+1)); s[0]=s[1]=0
        for i in range(2,int(n**0.5)+1):
            if s[i]==i:
                for j in range(i*i,n+1,i):
                    if s[j]==j: s[j]=i
        return s

    def factorize(x,spf):
        f=[]; v=x
        while v>1:
            p=spf[v]; e=0
            while v%p==0: v//=p; e+=1
            f.append((p,e))
        return f

    def cnt_sq(c,f_exp,spf):
        fac=factorize(c,spf); prod=1; all_even=True; e2=0
        for p,e0 in fac:
            e=e0*f_exp
            if p==2: e2=e
            elif e&1: all_even=False
            if p%4==3 and e&1: return 0
            if p%4==1: prod*=e+1
        r2=4*prod
        zero=4 if (all_even and e2%2==0) else 0
        eq=4 if (all_even and e2>=1 and (e2-1)%2==0) else 0
        return (r2-zero-eq)//8

    def divisors(fac):
        d=[1]
        for p,e in fac:
            old=len(d); mul=1
            for i in range(1,e+1):
                mul*=p
                for j in range(old): d.append(d[j]*mul)
        return d

    def cnt_cubes(n2,fac_n):
        divs=divisors(fac_n); count=0
        for u in divs:
            v=n2//u; u2=u*u
            if u2<=v: continue
            t=u2-v
            if t%3!=0: continue
            p=t//3
            if u2<4*p: continue
            delta=u2-4*p; s=isqrt(delta)
            if s*s!=delta: continue
            if s>=u or (u-s)&1: continue
            a=(u-s)//2; b=(u+s)//2
            if a==0 or a>=b: continue
            if a**3+b**3==n2: count+=1
        return count

    # Generate entries
    max_f=0
    while (1<<max_f)<=N and max_f<62: max_f+=1
    entries=[]; max_c=0
    for f in range(3,max_f+1):
        for c in range(2,10**7):
            v=pow_lim(c,f)
            if v>N: break
            entries.append((v,c,f))
            if c>max_c: max_c=c

    perfect_mask={}
    for v,c,f in entries:
        perfect_mask[v]=perfect_mask.get(v,0)|(1<<f)

    filt=[0]*(max_f+1)
    for e in range(max_f+1):
        m=0
        for f in range(3,max_f+1):
            if e==0 or f%e!=0: m|=1<<f
        filt[e]=m

    spf=spf_sieve(max_c)
    ans=0

    # Sum-of-two-squares
    for v,c,f in entries:
        ans+=cnt_sq(c,f,spf)

    # Sum-of-two-cubes
    cache3={}
    for v,c,f in entries:
        if f%3==0: continue
        if v in cache3: ans+=cache3[v]; continue
        fac_c=factorize(c,spf)
        fac_n=[(p,e*f) for p,e in fac_c]
        val=cnt_cubes(v,fac_n); cache3[v]=val; ans+=val

    # Higher powers (e>=4)
    for e in range(4,max_f+1):
        pw=[0]
        for b in range(1,10**7):
            v=pow_lim(b,e)
            if v>N: break
            pw.append(v)
        mb=len(pw)-1
        if mb<2: continue
        mf=filt[e]; even_e=(e&1)==0
        for b in range(2,mb+1):
            pb=pw[b]; amax=b-1
            while amax>0 and pw[amax]>N-pb: amax-=1
            if amax<=0: continue
            start=2 if (even_e and b&1) else 1
            step=2 if (even_e and b&1) else 1
            for a in range(start,amax+1,step):
                s=pb+pw[a]
                if s in perfect_mask:
                    ans+=bin(perfect_mask[s]&mf).count('1')
    return str(ans)

if __name__=='__main__':
    print(solve())
