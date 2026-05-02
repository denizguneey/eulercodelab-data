def solve():
    MOD = 10**9+7; NMAX = 10000
    inv2 = pow(2,MOD-2,MOD); inv6 = pow(6,MOD-2,MOD); inv24 = pow(24,MOD-2,MOD)

    # Build planted tree sequences
    s_all=[0]*(NMAX+1); s_no=[0]*(NMAX+1)
    s_all_sq=[0]*(NMAX+1); s_no_sq=[0]*(NMAX+1)
    p_r=[0]*(NMAX+1); p_b=[0]*(NMAX+1); p_y=[0]*(NMAX+1)

    def up_sq(s,sq,n):
        v=s[n]
        if v==0: return
        mx=min(n-1,NMAX-n)
        for k in range(1,mx+1):
            if s[k]==0: continue
            sq[n+k]=(sq[n+k]+2*v*s[k])%MOD
        if 2*n<=NMAX: sq[2*n]=(sq[2*n]+v*v)%MOD

    def c3(s,sq,t):
        if t<=1: return 0
        r=0
        for k in range(1,t): r=(r+s[k]*sq[t-k])%MOD
        return r

    def sc2(s,t):
        if t<=1: return 0
        r=0
        for u in range(2,t,2):
            k=t-u
            if k<1: break
            r=(r+s[k]*s[u//2])%MOD
        return r

    for n in range(1,NMAX+1):
        t=n-1; base=1 if t==0 else 0
        s1a=s_all[t]; s2a=s_all_sq[t]; s3a=c3(s_all,s_all_sq,t)
        sc2a=sc2(s_all,t); c2a=s_all[t//2] if t%2==0 else 0
        c3a=s_all[t//3] if t%3==0 else 0
        m1a=s1a; m2a=(s2a+c2a)*inv2%MOD
        m3a=(s3a+3*sc2a+2*c3a)%MOD*inv6%MOD
        s1n=s_no[t]; s2n=s_no_sq[t]; s3n=c3(s_no,s_no_sq,t)
        sc2n=sc2(s_no,t); c2n=s_no[t//2] if t%2==0 else 0
        c3n=s_no[t//3] if t%3==0 else 0
        m1n=s1n; m2n=(s2n+c2n)*inv2%MOD
        p_r[n]=(base+m1a+m2a+m3a)%MOD
        p_b[n]=(base+m1a+m2a)%MOD
        p_y[n]=(base+m1n+m2n)%MOD
        s_all[n]=(p_r[n]+p_b[n]+p_y[n])%MOD
        s_no[n]=(p_r[n]+p_b[n])%MOD
        up_sq(s_all,s_all_sq,n); up_sq(s_no,s_no_sq,n)

    def shift(s,k):
        out=[0]*(NMAX+1)
        for i in range(1,NMAX//k+1): out[i*k]=s[i]
        return out

    def conv(a,b):
        out=[0]*(NMAX+1)
        for i in range(1,NMAX+1):
            if a[i]==0: continue
            for j in range(1,NMAX-i+1):
                if b[j]==0: continue
                out[i+j]=(out[i+j]+a[i]*b[j])%MOD
        return out

    def conv_stride(a,base,stride):
        out=[0]*(NMAX+1)
        for k in range(1,NMAX//stride+1):
            c=base[k]
            if c==0: continue
            off=stride*k
            for j in range(1,NMAX-off+1):
                if a[j]==0: continue
                out[j+off]=(out[j+off]+a[j]*c)%MOD
        return out

    c2_all=shift(s_all,2); c3_all=shift(s_all,3); c4_all=shift(s_all,4)
    c2_no=shift(s_no,2); c3_no=shift(s_no,3)
    all_cube=conv(s_all_sq,s_all); all_four=conv(s_all_sq,s_all_sq)
    all_c2=conv_stride(s_all,s_all,2); all_sq_c2=conv_stride(s_all_sq,s_all,2)
    all_c3=conv_stride(s_all,s_all,3)
    no_cube=conv(s_no_sq,s_no); no_c2=conv_stride(s_no,s_no,2)
    c2_sq_all=[0]*(NMAX+1)
    for i in range(1,NMAX//2+1): c2_sq_all[2*i]=s_all_sq[i]

    a_all=[0]*(NMAX+1)
    for n in range(1,NMAX+1):
        t=n-1; base=1 if t==0 else 0
        m2a=(s_all_sq[t]+c2_all[t])*inv2%MOD
        m3a=(all_cube[t]+3*all_c2[t]+2*c3_all[t])%MOD*inv6%MOD
        m4a=(all_four[t]+6*all_sq_c2[t]+3*c2_sq_all[t]+8*all_c3[t]+6*c4_all[t])%MOD*inv24%MOD
        m2n=(s_no_sq[t]+c2_no[t])*inv2%MOD
        m3n=(no_cube[t]+3*no_c2[t]+2*c3_no[t])%MOD*inv6%MOD
        ar=(base+s_all[t]+m2a+m3a+m4a)%MOD
        ab=(base+s_all[t]+m2a+m3a)%MOD
        ay=(base+s_no[t]+m2n+m3n)%MOD
        a_all[n]=(ar+ab+ay)%MOD

    py_sq=conv(p_y,p_y)
    pa_x2=shift(s_all,2); py_x2=shift(p_y,2)
    g=[0]*(NMAX+1)
    for n in range(1,NMAX+1):
        d=(s_all_sq[n]-py_sq[n])%MOD
        e2=(s_all_sq[n]+pa_x2[n]-py_sq[n]-py_x2[n])%MOD
        eh=e2*inv2%MOD
        g[n]=(a_all[n]+eh-d)%MOD
    return str(g[NMAX]%MOD)

if __name__=='__main__':
    print(solve())
