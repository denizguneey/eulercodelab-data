import bisect

def solve():
    MOD_S = 50515093; t = 100000

    # Generate rectangles
    s = 290797; vals = [s]
    for _ in range(4*t-1): s = s*s%MOD_S; vals.append(s)
    rects = []
    for i in range(t):
        a,b,c,d = vals[4*i],vals[4*i+1],vals[4*i+2],vals[4*i+3]
        rects.append((min(a,b),max(a,b),min(c,d),max(c,d)))

    # Coordinate compress y
    ys = sorted(set([0, MOD_S] + [r[2] for r in rects] + [r[3]+1 for r in rects]))
    yi = {v:i for i,v in enumerate(ys)}
    n = len(ys)-1

    # Segment tree with rotation by 12
    sz = 4*n+4
    sm = [[0]*12 for _ in range(sz)]
    lz = [0]*sz

    def build(idx, l, r):
        if l == r: sm[idx][0] = ys[l+1]-ys[l]; return
        m = (l+r)//2; build(2*idx,l,m); build(2*idx+1,m+1,r)
        for i in range(12): sm[idx][i] = sm[2*idx][i]+sm[2*idx+1][i]

    def rot(idx, sh):
        sh %= 12
        if sh == 0: return
        old = sm[idx][:]; 
        for i in range(12): sm[idx][(i+sh)%12] = old[i]
        lz[idx] = (lz[idx]+sh)%12

    def push(idx):
        if lz[idx]:
            rot(2*idx, lz[idx]); rot(2*idx+1, lz[idx]); lz[idx]=0

    def pull(idx):
        for i in range(12): sm[idx][i] = sm[2*idx][i]+sm[2*idx+1][i]

    def update(idx, l, r, ql, qr, delta):
        if ql>r or qr<l: return
        if ql<=l and r<=qr: rot(idx, delta); return
        push(idx); m=(l+r)//2
        update(2*idx,l,m,ql,qr,delta); update(2*idx+1,m+1,r,ql,qr,delta); pull(idx)

    build(1, 0, n-1)
    events = []
    for x1,x2,y1,y2 in rects:
        events.append((x1,y1,y2,1))
        if x2+1 < MOD_S: events.append((x2+1,y1,y2,-1))
    events.sort()
    cnt = [0]*12; cx = 0; ei = 0
    while ei < len(events):
        nx = events[ei][0]
        w = nx - cx
        if w > 0:
            for r in range(12): cnt[r] += sm[1][r]*w
        while ei < len(events) and events[ei][0] == nx:
            _,y1,y2,delta = events[ei]
            l = bisect.bisect_left(ys, y1); rr = bisect.bisect_left(ys, y2+1)-1
            if l <= rr: update(1,0,n-1,l,rr,delta)
            ei += 1
        cx = nx
    if cx < MOD_S:
        w = MOD_S - cx
        for r in range(12): cnt[r] += sm[1][r]*w
    ans = cnt[0]*12
    for r in range(1,12): ans += cnt[r]*r
    return str(ans)

if __name__ == '__main__':
    print(solve())
