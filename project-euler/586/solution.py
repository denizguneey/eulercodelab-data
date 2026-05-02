import math

def solve():
    LIMIT = 10**15; R = 40

    def sieve(n):
        ip=[True]*(n+1); ip[0]=ip[1]=False
        for i in range(2,int(n**0.5)+1):
            if ip[i]:
                for j in range(i*i,n+1,i): ip[j]=False
        return [i for i in range(2,n+1) if ip[i]]

    def isqrt(x):
        r=int(math.isqrt(x))
        while (r+1)*(r+1)<=x: r+=1
        while r*r>x: r-=1
        return r

    def pow_lim(b,e,lim):
        r=1
        for _ in range(e):
            if r>lim//b: return lim+1
            r*=b
        return r

    def nth_root(n,e):
        if e<=1 or n<=1: return n
        x=int(n**(1.0/e))
        if x<1: x=1
        while pow_lim(x+1,e,n)<=n: x+=1
        while pow_lim(x,e,n)>n: x-=1
        return x

    def split_primes(lim):
        return [p for p in sieve(lim) if p%5 in (1,4)]

    def gen_exp_pats(tau):
        pats=set()
        def rec(rem,mn,facs):
            if rem==1:
                if facs:
                    e=tuple(sorted((f-1 for f in facs),reverse=True))
                    pats.add(e)
                return
            for f in range(mn,rem+1):
                if f<2 or rem%f: continue
                rec(rem//f,f,facs+[f])
        rec(tau,2,[])
        return list(pats)

    sp_seed = split_primes(500)
    patterns = set()
    for tau in (2*R, 2*R+1):
        for pat in gen_exp_pats(tau):
            if len(pat)>len(sp_seed): continue
            prod=1; ok=True
            for i,e in enumerate(pat):
                v=pow_lim(sp_seed[i],e,LIMIT)
                if v>LIMIT//prod: ok=False; break
                prod*=v
            if ok: patterns.add(pat)
    if not patterns: return "0"

    # Estimate prime limit
    max_bound=0
    for pat in patterns:
        for j in range(len(pat)):
            others=sorted([pat[i] for i in range(len(pat)) if i!=j], reverse=True)
            fp=1; ok=True
            for i,e in enumerate(others):
                if i>=len(sp_seed): ok=False; break
                v=pow_lim(sp_seed[i],e,LIMIT)
                if v>LIMIT//fp: ok=False; break
                fp*=v
            if not ok or fp>LIMIT: continue
            rem=LIMIT//fp; b=nth_root(rem,pat[j])
            max_bound=max(max_bound,b)
    max_bound=max(max_bound,11)

    sp = split_primes(max_bound)
    if not sp: return "0"

    min_prod=LIMIT+1
    for pat in patterns:
        if len(pat)>len(sp): continue
        prod=1; ok=True
        for i,e in enumerate(sorted(pat,reverse=True)):
            v=pow_lim(sp[i],e,LIMIT)
            if v>LIMIT//prod: ok=False; break
            prod*=v
        if ok: min_prod=min(min_prod,prod)
    if min_prod>LIMIT: return "0"

    max_mult = LIMIT//min_prod; max_y = isqrt(max_mult)
    # Inert-only prefix: numbers with no prime factor p where p=5 or p%5 in {1,4}
    primes_all = sieve(max_y)
    inert_only = bytearray([1]*(max_y+1)); inert_only[0]=0
    for p in primes_all:
        if p==5 or p%5 in (1,4):
            for m in range(p,max_y+1,p): inert_only[m]=0
    ip = [0]*(max_y+1); s=0
    for i in range(max_y+1): s+=inert_only[i]; ip[i]=s

    # Multiplier table
    g = [0]*(max_mult+1)
    for x in range(1,max_mult+1):
        t=0; p5=1
        while p5<=x:
            y=isqrt(x//p5); t+=ip[y]
            if p5>x//5: break
            p5*=5
        g[x]=t

    # Power table
    exp_set = set()
    for pat in patterns:
        for e in pat: exp_set.add(e)
    exp_vals = sorted(exp_set)
    slot_map = {e:i for i,e in enumerate(exp_vals)}
    pow_tab = []
    for e in exp_vals:
        vals = []
        for i,p in enumerate(sp):
            v=pow_lim(p,e,LIMIT)
            if v>LIMIT: break
            vals.append(v)
        pow_tab.append(vals)

    # DFS over permutations
    from itertools import permutations
    total = 0
    for pat in patterns:
        for perm in set(permutations(pat)):
            if len(perm)>len(sp): continue
            prod=1; ok=True
            for i,e in enumerate(perm):
                pt=pow_tab[slot_map[e]]
                if i>=len(pt) or pt[i]==0 or pt[i]>LIMIT//prod: ok=False; break
                prod*=pt[i]
            if not ok: continue
            # DFS
            def dfs(pos, start, prod2):
                if pos==len(perm):
                    return g[LIMIT//prod2]
                pt=pow_tab[slot_map[perm[pos]]]
                rem_slots=len(perm)-pos; s=0
                for i in range(start, len(sp)-rem_slots+1):
                    if i>=len(pt) or pt[i]==0: break
                    pe=pt[i]
                    if pe>LIMIT//prod2: break
                    np=prod2*pe
                    # Tail fit check
                    tp=1; fit=True; idx2=i+1
                    for pp in range(pos+1,len(perm)):
                        pt2=pow_tab[slot_map[perm[pp]]]
                        if idx2>=len(pt2) or pt2[idx2]==0: fit=False; break
                        if pt2[idx2]>LIMIT//(np*tp) if tp<=LIMIT//np else True:
                            fit=False; break
                        tp*=pt2[idx2]; idx2+=1
                    if not fit: break
                    s+=dfs(pos+1, i+1, np)
                return s
            total += dfs(0, 0, 1)
    return str(total)

if __name__=='__main__':
    print(solve())
