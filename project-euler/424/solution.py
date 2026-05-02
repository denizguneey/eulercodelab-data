def solve():
    import os
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "solutionsCpp", "p424_kakuro200.txt")
    if not os.path.exists(path):
        path = "solutionsCpp/p424_kakuro200.txt"

    MAX_SUM = 45; CELL_MASK = 0x3FE  # bits 1-9

    # Generate valid tuples
    tc = [[[] for _ in range(MAX_SUM+1)] for _ in range(10)]
    def gen(l,p,u,s,c):
        if p==l: tc[l][s].append(c); return
        for d in range(1,10):
            if u&(1<<d): continue
            gen(l,p+1,u|(1<<d),s+d,c|(d<<(4*p)))
    for l in range(1,10): gen(l,0,0,0,0)

    def lid(ch): return ord(ch)-ord('A') if 'A'<=ch<='J' else -1
    def iswt(t): return t=='O' or (len(t)==1 and lid(t[0])>=0)

    def parse(line):
        toks = []; cur=''; depth=0
        for ch in line.strip():
            if ch==',' and depth==0: toks.append(cur); cur=''
            elif ch not in ' \t\r\n': cur+=ch; depth+=(ch=='(')-(ch==')')
        toks.append(cur)
        n=int(toks[0]); grid=toks[1:]
        wi=[-1]*(n*n); cl=[]; wc=0
        for r in range(n):
            for c in range(n):
                t=grid[r*n+c]
                if not iswt(t): continue
                wi[r*n+c]=wc; wc+=1; cl.append(lid(t[0]) if t!='O' else -1)
        runs=[]
        for r in range(n):
            for c in range(n):
                t=grid[r*n+c]
                if len(t)<2 or t[0]!='(' or t[-1]!=')': continue
                ins=t[1:-1]; parts=ins.split(',')
                for part in parts:
                    h=part[0]=='h'; cs=part[1:]
                    clen=len(cs); cl0=lid(cs[0]); cl1=lid(cs[1]) if clen==2 else -1
                    cells=[]
                    if h:
                        for cc in range(c+1,n):
                            idx=wi[r*n+cc]
                            if idx<0: break
                            cells.append(idx)
                    else:
                        for rr in range(r+1,n):
                            idx=wi[rr*n+c]
                            if idx<0: break
                            cells.append(idx)
                    if cells: runs.append((cells,cl0,cl1,clen))
        return n,wi,cl,runs

    def solve_puzzle(puz):
        n,wi,cl,runs=puz; NC=len(cl)
        ld=[0x3FF]*10; cd=[CELL_MASK]*NC
        def prop():
            while True:
                ch=False
                for i in range(NC):
                    lt=cl[i]
                    if lt<0: continue
                    al=ld[lt]&CELL_MASK; nd=cd[i]&al
                    if nd==0: return False
                    if nd!=cd[i]: cd[i]=nd; ch=True
                    nl=ld[lt]&nd
                    if nl==0: return False
                    if nl!=ld[lt]: ld[lt]=nl; ch=True
                # alldiff
                asgn=0
                for i in range(10):
                    if ld[i]==0: return False
                    if ld[i]&(ld[i]-1)==0: asgn|=ld[i]
                for i in range(10):
                    if ld[i]&(ld[i]-1)==0: continue
                    nd=ld[i]&~asgn
                    if nd==0: return False
                    if nd!=ld[i]: ld[i]=nd; ch=True
                for d in range(10):
                    bit=1<<d; cnt=0; where=-1
                    for i in range(10):
                        if ld[i]&bit: cnt+=1; where=i
                    if cnt==0: return False
                    if cnt==1 and ld[where]!=bit: ld[where]=bit; ch=True
                # runs
                for cells,a,b,clen in runs:
                    ln=len(cells)
                    if clen==2:
                        nd=ld[a]&~1
                        if nd==0: return False
                        if nd!=ld[a]: ld[a]=nd; ch=True
                    sa=[False]*(MAX_SUM+1)
                    if clen==1:
                        for d in range(10):
                            if (ld[a]>>d)&1: sa[d]=True
                    else:
                        for da in range(10):
                            if not (ld[a]>>da)&1: continue
                            for db in range(10):
                                if (ld[b]>>db)&1:
                                    s=10*da+db
                                    if s<=MAX_SUM: sa[s]=True
                    um=[0]*ln; sv=[False]*(MAX_SUM+1); at=False
                    for s in range(MAX_SUM+1):
                        if not sa[s]: continue
                        for code in tc[ln][s]:
                            ok=True
                            for p in range(ln):
                                d=(code>>(4*p))&0xF
                                if not (cd[cells[p]]>>(d))&1: ok=False; break
                            if not ok: continue
                            at=True; sv[s]=True
                            for p in range(ln): um[p]|=1<<((code>>(4*p))&0xF)
                    if not at: return False
                    for p in range(ln):
                        cid=cells[p]; nd=cd[cid]&um[p]
                        if nd==0: return False
                        if nd!=cd[cid]: cd[cid]=nd; ch=True
                    if clen==1:
                        al2=0
                        for s in range(10):
                            if sv[s]: al2|=1<<s
                        nd=ld[a]&al2
                        if nd==0: return False
                        if nd!=ld[a]: ld[a]=nd; ch=True
                    elif a==b:
                        al2=0
                        for d in range(10):
                            s=11*d
                            if s<=MAX_SUM and sv[s]: al2|=1<<d
                        al2&=~1; nd=ld[a]&al2
                        if nd==0: return False
                        if nd!=ld[a]: ld[a]=nd; ch=True
                    else:
                        aa=ab=0
                        for da in range(10):
                            if not (ld[a]>>da)&1: continue
                            for db in range(10):
                                if not (ld[b]>>db)&1: continue
                                s=10*da+db
                                if s<=MAX_SUM and sv[s]: aa|=1<<da; ab|=1<<db
                        aa&=~1; na=ld[a]&aa; nb=ld[b]&ab
                        if na==0 or nb==0: return False
                        if na!=ld[a]: ld[a]=na; ch=True
                        if nb!=ld[b]: ld[b]=nb; ch=True
                if not ch: break
            return True
        def solved():
            return all(d&(d-1)==0 and d!=0 for d in ld) and all(d&(d-1)==0 and d!=0 for d in cd)
        def dfs():
            if not prop(): return False
            if solved(): return True
            best_sz=100; best_is_l=True; best_i=-1; best_d=0
            for i in range(10):
                sz=bin(ld[i]).count('1')
                if sz>1 and sz<best_sz: best_sz=sz; best_is_l=True; best_i=i; best_d=ld[i]
            for i in range(NC):
                sz=bin(cd[i]).count('1')
                if sz>1 and sz<best_sz: best_sz=sz; best_is_l=False; best_i=i; best_d=cd[i]
            if best_i<0: return False
            sld=ld[:]; scd=cd[:]
            for d in range(10):
                if not (best_d>>d)&1: continue
                ld[:]=sld[:]; cd[:]=scd[:]
                if best_is_l: ld[best_i]=1<<d
                else: cd[best_i]=1<<d
                if dfs(): return True
            ld[:]=sld; cd[:]=scd; return False
        if not dfs(): return 0
        v=0
        for i in range(10): v=v*10+(ld[i]).bit_length()-1
        return v

    with open(path) as f: lines=f.readlines()
    total=0
    for line in lines:
        line=line.strip()
        if not line: continue
        total+=solve_puzzle(parse(line))
    return str(total)

if __name__=='__main__':
    print(solve())
