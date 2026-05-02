import math

def solve():
    N = 5000000

    # Totient sieve
    phi = list(range(N+1))
    for i in range(2, N+1):
        if phi[i]==i:
            for j in range(i, N+1, i): phi[j]-=phi[j]//i

    # f(s) = phi(s)/2 - R(s) where R counts primitive i^2+j^2 reps
    f = [0]*(N+1)
    for s in range(3, N+1): f[s] = phi[s]//2
    lim = int(math.isqrt(N))
    for i in range(2, lim+1):
        i2 = i*i
        for j in range(1, i):
            if math.gcd(i,j)!=1: continue
            s = i2+j*j
            if s>N: break
            f[s] -= 1

    # Prefix sum
    pref = [0]*(N+1)
    for i in range(1, N+1): pref[i] = pref[i-1]+f[i]

    def partial_sum_floor(m):
        ret=0; i=1
        while i<=m:
            q=m//i; j=m//q+1
            ret+=q*(pref[j-1]-pref[i-1]); i=j
        return ret

    # Type 1: sum f(s)*floor(n/s)
    cnt1 = 0
    for s in range(3, N+1):
        if f[s]==0: continue
        cnt1 += f[s]*(N//s)

    # Type 2 ordered
    cnt2 = 0; i=1
    while i<=N:
        q=N//i; j=N//q+1
        sf = pref[j-1]-pref[i-1]
        cnt2 += sf*partial_sum_floor(q); i=j

    # Overlap (simplified - 4-tuple coprime enumeration)
    def sq_flags(n):
        ok=[True]*(n+1); ok[0]=False
        for p in range(2, int(math.isqrt(n))+1):
            p2=p*p
            for j in range(p2,n+1,p2): ok[j]=False
        return ok

    lim2 = int(math.isqrt(N))
    isf = sq_flags(lim2)
    sf = [i for i in range(1,lim2+1) if isf[i]]
    sqs = [i*i for i in range(lim2+1)]

    cnt3 = 0
    for pi in range(len(sf)):
        p=sf[pi]
        if (p+1)*(p+1)>N: break
        for qi in range(len(sf)):
            q=sf[qi]; pq=p*q
            if (pq+1)*(p+q)>N: break
            if math.gcd(p,q)!=1: continue
            for ri in range(len(sf)):
                r=sf[ri]; pr=p*r
                if (pq+r)*(pr+q)>N: break
                if math.gcd(p,r)!=1 or math.gcd(q,r)!=1: continue
                for si in range(len(sf)):
                    s=sf[si]; rs=r*s; qs=q*s
                    if (pq+rs)*(pr+qs)>N: break
                    if math.gcd(p,s)!=1 or math.gcd(q,s)!=1 or math.gcd(r,s)!=1: continue
                    u=pq; v=rs; a2=pr; b2=qs
                    if u==v or a2==b2: continue
                    mx=N//(a2+b2)
                    for w1 in range(1,lim2+1):
                        uw1=u*sqs[w1]
                        if uw1+v>mx: break
                        if math.gcd(r,w1)!=1 or math.gcd(s,w1)!=1: continue
                        for w2 in range(1,lim2+1):
                            vw2=v*sqs[w2]; x2=uw1+vw2
                            if x2>mx: break
                            if uw1<=vw2: continue
                            if math.gcd(p,w2)!=1 or math.gcd(q,w2)!=1: continue
                            if math.gcd(w1,w2)!=1: continue
                            m2=N//x2
                            for w3 in range(1,lim2+1):
                                aw3=a2*sqs[w3]
                                if aw3+b2>m2: break
                                if math.gcd(q,w3)!=1 or math.gcd(s,w3)!=1: continue
                                for w4 in range(1,lim2+1):
                                    bw4=b2*sqs[w4]; y2=aw3+bw4
                                    if y2>m2: break
                                    if aw3<=bw4: continue
                                    if math.gcd(p,w4)!=1 or math.gcd(r,w4)!=1: continue
                                    if math.gcd(w3,w4)!=1: continue
                                    cnt3+=m2//y2

    return str(cnt1 + (cnt2-cnt3)//2)

if __name__=='__main__':
    print(solve())
