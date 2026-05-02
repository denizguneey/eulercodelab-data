from decimal import Decimal, getcontext
import math

def solve():
    getcontext().prec = 120
    PI = Decimal('3.14159265358979323846264338327950288419716939937510'
                 '58209749445923078164062862089986280348253421170679')
    TAU = PI - 3
    N = 10**13

    def is_sq(n): r=int(math.isqrt(n)); return r*r==n

    def cf_period(d):
        a0=int(math.isqrt(d))
        if a0*a0==d: return []
        m=0; den=1; a=a0; period=[]
        while True:
            m=den*a-m; den=(d-m*m)//den; a=(a0+m)//den
            period.append(a)
            if den==1 and m==a0: break
        return period

    def convergents(d, qlim):
        a0=int(math.isqrt(d)); period=cf_period(d)
        conv=[(a0,1)]
        if not period: return conv
        pm2,qm2=1,0; pm1,qm1=a0,1; i=0
        while True:
            a=period[i%len(period)]; i+=1
            p=a*pm1+pm2; q=a*qm1+qm2
            conv.append((p,q))
            if q>qlim: break
            pm2,qm2=pm1,qm1; pm1,qm1=p,q
        return conv

    def modinv(a,m):
        b=m; x0,x1=1,0; aa=a
        while b:
            q=aa//b; aa,b=b,aa-q*b; x0,x1=x1,x0-q*x1
        if aa!=1 and aa!=-1: return -1
        return x0%m

    def best_bqa(d, NN):
        alpha=Decimal(d).sqrt()
        B=int((Decimal(NN)+PI+2)/alpha)
        if B>NN: B=NN
        conv=convergents(d,B)
        best_err=Decimal('1e1000'); best_a=0; best_b=0; found=False

        def eval_b(b):
            nonlocal best_err,best_a,best_b,found
            if abs(b)>B or abs(b)>NN: return
            val=alpha*Decimal(b); ar=PI-val; a0=int(ar+Decimal('0.5')) if ar>=0 else -int(-ar+Decimal('0.5'))
            for da in (-1,0,1):
                a=a0+da
                if abs(a)>NN: continue
                err=abs(ar-Decimal(a))
                if not found or err<best_err or (err==best_err and abs(a)<abs(best_a)):
                    found=True; best_a=a; best_b=b; best_err=err

        for p,q in conv:
            if q<=0: continue
            inv=modinv(p%q if p%q>=0 else p%q+q, q)
            if inv<0: continue
            qD=Decimal(q); r=int(TAU*qD)
            delta=qD*alpha-Decimal(p)
            if delta==0: continue
            jlo=max(0,r-25); jhi=min(q-1,r+25)
            for j in range(jlo,jhi+1):
                b0=(j*inv)%q
                tmin=(-B-b0+q-1)//q if -B-b0>=0 else -(-(- B-b0))//q
                # Proper ceil/floor div
                num=-B-b0
                tmin = num//q if num>=0 else -((-num)//q) if (-num)%q==0 else -((-num)//q+1) if num<0 else num//q
                tmin = math.ceil((-B-b0)/q) if q>0 else 0
                tmax = math.floor((B-b0)/q) if q>0 else 0
                if tmin>tmax: continue
                diff=Decimal(j)/qD+Decimal(b0)*delta/qD-TAU
                ratio=-diff/delta; t0=int(ratio+Decimal('0.5')) if ratio>=0 else -int(-ratio+Decimal('0.5'))
                ttlo=max(tmin,t0-25); tthi=min(tmax,t0+25)
                for t in range(ttlo,tthi+1):
                    eval_b(b0+t*q)
                eval_b(b0+tmin*q); eval_b(b0+tmax*q)
        return abs(best_a)

    ds = [d for d in range(2,100) if not is_sq(d)]
    total = sum(best_bqa(d,N) for d in ds)
    return str(total)

if __name__=='__main__':
    print(solve())
