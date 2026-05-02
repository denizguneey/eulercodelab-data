from math import gcd

def solve():
    N = 100

    def sieve(n):
        ip=[True]*(n+1); ip[0]=ip[1]=False
        for i in range(2,int(n**0.5)+1):
            if ip[i]:
                for j in range(i*i,n+1,i): ip[j]=False
        return [i for i in range(2,n+1) if ip[i]]

    primes = sieve(5000000)

    def factorize(n):
        f=[]
        for p in primes:
            if p*p>n: break
            if n%p==0:
                f.append(p)
                while n%p==0: n//=p
        if n>1: f.append(n)
        return f

    # GF(2) polynomial operations using Python ints (unlimited precision)
    def pdeg(p):
        if p==0: return -1
        return p.bit_length()-1

    def pmod(a,m):
        dm=pdeg(m)
        if dm<0: return a
        while True:
            da=pdeg(a)
            if da<dm: break
            a^=m<<(da-dm)
        return a

    def pdiv(a,m):
        q=0; dm=pdeg(m)
        while True:
            da=pdeg(a)
            if da<dm: break
            s=da-dm; q|=1<<s; a^=m<<s
        return q

    def pgcd(a,b):
        while b: a,b=b,pmod(a,b)
        return a

    def pmulmod(a,b,m):
        a=pmod(a,m); b=pmod(b,m)
        r=0
        while b:
            if b&1: r^=a
            b>>=1; a<<=1
            if pdeg(a)==pdeg(m): a^=m
        return r

    def ppowmod(base,exp,m):
        r=1
        while exp>0:
            if exp&1: r=pmulmod(r,base,m)
            base=pmulmod(base,base,m); exp>>=1
        return r

    def berlekamp(f):
        m=pdeg(f)
        if m<=1: return [f]
        # Build Q matrix (x^(2j) mod f for j=0..m-1)
        rows=[0]*m; power=1; x2=pmod(4,f)  # x^2
        # Actually x=2 in poly representation: bit 1 set = x^1
        # x^2 = 4 = bit 2
        power=1  # x^0
        for col in range(m):
            for row in range(m):
                if (power>>row)&1: rows[row]^=1<<col
            power=pmulmod(power,x2,f)
        # Q-I
        for i in range(m): rows[i]^=1<<i
        # Row reduce
        pivot=[]; rank=0
        for col in range(m):
            sel=-1
            for r in range(rank,m):
                if (rows[r]>>col)&1: sel=r; break
            if sel<0: continue
            rows[rank],rows[sel]=rows[sel],rows[rank]
            pivot.append(col)
            for r in range(m):
                if r!=rank and (rows[r]>>col)&1: rows[r]^=rows[rank]
            rank+=1
        is_pivot=set(pivot)
        basis=[]
        for col in range(m):
            if col in is_pivot: continue
            vec=1<<col
            for i in range(rank):
                if (rows[i]>>col)&1: vec|=1<<pivot[i]
            basis.append(vec)
        factors=[f]
        for b in basis:
            if b==0 or b==1: continue
            nxt=[]
            for h in factors:
                if pdeg(h)<=1: nxt.append(h); continue
                g=pgcd(h,b)
                if g!=1 and g!=h:
                    nxt.append(g); nxt.append(pdiv(h,g)); continue
                b1=b^1; g=pgcd(h,b1)
                if g!=1 and g!=h:
                    nxt.append(g); nxt.append(pdiv(h,g))
                else: nxt.append(h)
            factors=nxt
        return factors

    def order_in_factor(lam,mod):
        if lam==0: return 0
        if lam==1: return 1
        deg=pdeg(mod); cur=lam; e=0
        while True:
            cur=pmulmod(cur,cur,mod); e+=1
            if cur==lam or e>deg: break
        if e>deg or e>63: return 0
        order=(1<<e)-1; reduced=order
        for p in factorize(order):
            while reduced%p==0:
                trial=reduced//p
                if ppowmod(lam,trial,mod)==1: reduced=trial
                else: break
        return reduced

    def orders_for_m(m):
        f=1|(1<<m)  # x^m + 1
        factors=berlekamp(f)
        orders=[]
        x=2  # x polynomial
        for g in factors:
            xpow=ppowmod(x,m-1,g)
            lam=pmod(x^xpow,g)
            orders.append(order_in_factor(lam,g))
        return orders

    def lcm(a,b): return a//gcd(a,b)*b

    def periods_for_n(n,orders,k):
        periods={1}
        for ord_val in orders:
            opts=[1]
            if ord_val==0: pass
            elif ord_val==1:
                for s in range(1,k+1): opts.append(1<<s)
            else:
                for s in range(k+1): opts.append(ord_val<<s)
            nxt=set()
            for p in periods:
                for o in opts: nxt.add(lcm(p,o))
            periods=nxt
        return periods

    cache={}
    global_periods=set()
    for n in range(3,N+1):
        m=n; k=0
        while m%2==0: m>>=1; k+=1
        if m not in cache: cache[m]=orders_for_m(m)
        per=periods_for_n(n,cache[m],k)
        global_periods|=per

    return str(sum(global_periods))

if __name__=='__main__':
    print(solve())
