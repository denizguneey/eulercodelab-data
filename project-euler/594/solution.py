import math

def solve():
    SQRT2 = math.sqrt(2)

    class Num:
        __slots__=('a','b')
        def __init__(self,a=0,b=0): self.a=a; self.b=b
        def __add__(s,o): return Num(s.a+o.a,s.b+o.b)
        def __sub__(s,o): return Num(s.a-o.a,s.b-o.b)
        def __mul__(s,o): return Num(s.a*o.a+2*s.b*o.b,s.a*o.b+s.b*o.a)
        def __eq__(s,o): return s.a==o.a and s.b==o.b
        def __hash__(s): return hash((s.a,s.b))
        def val(s): return s.a+s.b*SQRT2
        def zero(s): return s.a==0 and s.b==0

    class Pt:
        __slots__=('x','y')
        def __init__(s,x=None,y=None): s.x=x or Num(); s.y=y or Num()
        def __add__(s,o): return Pt(s.x+o.x,s.y+o.y)
        def __sub__(s,o): return Pt(s.x-o.x,s.y-o.y)
        def __eq__(s,o): return s.x==o.x and s.y==o.y
        def __hash__(s): return hash((s.x.a,s.x.b,s.y.a,s.y.b))
        def key(s): return (s.x.a,s.x.b,s.y.a,s.y.b)

    def sign_num(v):
        if v.zero(): return 0
        return -1 if v.val()<0 else 1

    def cross(a,b,c):
        ab=b-a; ac=c-a
        return ab.x*ac.y-ab.y*ac.x

    def on_seg(a,b,p):
        cr=cross(a,b,p)
        if not cr.zero(): return False
        def mn(x,y): return x if sign_num(x-y)<=0 else y
        def mx(x,y): return x if sign_num(x-y)>=0 else y
        if sign_num(p.x-mn(a.x,b.x))<0 or sign_num(p.x-mx(a.x,b.x))>0: return False
        if sign_num(p.y-mn(a.y,b.y))<0 or sign_num(p.y-mx(a.y,b.y))>0: return False
        return True

    def seg_ix(a,b,c,d):
        o1=sign_num(cross(a,b,c)); o2=sign_num(cross(a,b,d))
        o3=sign_num(cross(c,d,a)); o4=sign_num(cross(c,d,b))
        if o1==0 and on_seg(a,b,c): return True
        if o2==0 and on_seg(a,b,d): return True
        if o3==0 and on_seg(c,d,a): return True
        if o4==0 and on_seg(c,d,b): return True
        return o1!=o2 and o3!=o4

    def pip(p,poly):
        px,py=p.x.val(),p.y.val(); inside=False; n=len(poly)
        for i in range(n):
            a,b=poly[i],poly[(i+1)%n]
            if on_seg(a,b,p): return True
            ay,by=a.y.val(),b.y.val()
            if (ay>py)!=(by>py):
                ax,bx=a.x.val(),b.x.val()
                xin=ax+(bx-ax)*(py-ay)/(by-ay)
                if xin>px: inside=not inside
        return inside

    dirs=[Pt(Num(2,0),Num(0,0)),Pt(Num(0,1),Num(0,1)),Pt(Num(0,0),Num(2,0)),
          Pt(Num(0,-1),Num(0,1)),Pt(Num(-2,0),Num(0,0)),Pt(Num(0,-1),Num(0,-1)),
          Pt(Num(0,0),Num(-2,0)),Pt(Num(0,1),Num(0,-1))]

    def build_verts(steps):
        pts=[Pt()]; cur=Pt()
        for d in steps: cur=cur+dirs[d]; pts.append(cur)
        return pts

    def sa(steps):
        if not steps: return 0.0
        pts=build_verts(steps)[:-1]
        area=0.0
        for i in range(len(pts)):
            a,b=pts[i],pts[(i+1)%len(pts)]
            area+=a.x.val()*b.y.val()-b.x.val()*a.y.val()
        return 0.5*area

    def to_ccw(steps):
        return [((s+4)&7) for s in reversed(steps)]

    def make_ek(a,b):
        ka,kb=a.key(),b.key()
        return (ka,kb) if ka<kb else (kb,ka)

    def edges_from(steps):
        edges={}; cur=Pt()
        for d in steps:
            nxt=cur+dirs[d]; ek=make_ek(cur,nxt)
            edges[ek]=(cur,nxt); cur=nxt
        return edges

    def extract_cycles(edge_map):
        if not edge_map: return []
        edges=[]; outgoing={}
        for ek,(fr,to) in edge_map.items():
            diff=to-fr; di=-1
            for i in range(8):
                if diff.x==dirs[i].x and diff.y==dirs[i].y: di=i; break
            if di<0: return None
            eid=len(edges); edges.append([fr.key(),to.key(),di,False])
            outgoing.setdefault(fr.key(),[]).append(eid)
        cycles=[]; used=0
        def pick():
            best=None; bi=-1
            for i,(fk,_,_,u) in enumerate(edges):
                if u: continue
                fp=Pt(Num(fk[0],fk[1]),Num(fk[2],fk[3]))
                if best is None or (fp.y.val(),fp.x.val())<(best.y.val(),best.x.val()):
                    best=fp; bi=i
            return bi
        while used<len(edges):
            si=pick()
            if si<0: return None
            ci=si; steps=[]
            while True:
                e=edges[ci]
                if e[3]: return None
                e[3]=True; used+=1; steps.append(e[2])
                head=e[1]; outs=outgoing.get(head,[])
                bn=-1; bd=9
                for cid in outs:
                    if edges[cid][3] and cid!=si: continue
                    delta=(edges[cid][2]-e[2]+8)&7
                    if delta<bd: bd=delta; bn=cid
                if bn<0: return None
                if bn==si: break
                ci=bn
            cycles.append(steps)
        return cycles

    memo={}
    def dfs(key):
        if key in memo: return memo[key]
        if not key: return 1
        steps=list(key); pts=build_verts(steps); n=len(steps)
        mi=0; mp=pts[0]
        for i in range(n):
            if (pts[i].y.val(),pts[i].x.val())<(mp.y.val(),mp.x.val()): mp=pts[i]; mi=i
        p=mp; d=steps[mi]
        be=[(pts[i],pts[i+1]) for i in range(n)]
        base_e=edges_from(steps)
        total=0
        for delta in range(1,4):
            vd=(d+delta)&7; u=dirs[d]; v=dirs[vd]
            p1=p; p2=p+u; p3=p2+v; p4=p+v
            if not pip(p4,pts) or not pip(p3,pts): continue
            te=[(p1,p2),(p2,p3),(p3,p4),(p4,p1)]; ok=True
            for ta,tb in te:
                for ca,cb in be:
                    if (ta==ca and tb==cb) or (ta==cb and tb==ca): continue
                    if ta==ca or ta==cb or tb==ca or tb==cb: continue
                    if seg_ix(ta,tb,ca,cb): ok=False; break
                if not ok: break
            if not ok: continue
            edges=dict(base_e)
            cw=[(p1,p4),(p4,p3),(p3,p2),(p2,p1)]
            for ea,eb in cw:
                ek=make_ek(ea,eb)
                if ek in edges: del edges[ek]
                else: edges[ek]=(ea,eb)
            cycles=extract_cycles(edges)
            if cycles is None: continue
            if not cycles: total+=1; continue
            ways=1
            for cy in cycles:
                if sa(cy)<0: cy=to_ccw(cy)
                ways*=dfs(tuple(cy))
            total+=ways
        memo[key]=total
        return total

    a,b=4,2
    steps=[]
    lens=[a,b,a,b,a,b,a,b]
    for i in range(8):
        for _ in range(lens[i]): steps.append(i)
    return str(dfs(tuple(steps)))

if __name__=='__main__':
    print(solve())
