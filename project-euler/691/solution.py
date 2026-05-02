import math

def solve():
    n = 5000000
    invphi = (math.sqrt(5) - 1) / 2

    # SAM
    class State:
        __slots__ = ['next', 'link', 'length', 'occ']
        def __init__(self):
            self.next = [-1, -1]; self.link = -1; self.length = 0; self.occ = 0

    st = [State() for _ in range(2*n)]
    sz = 1; last = 0
    beat_prev = 0

    for i in range(n):
        a = bin(i).count('1') & 1
        beat_cur = int(math.floor((i + 1) * invphi))
        b = beat_cur - beat_prev; beat_prev = beat_cur
        c = a ^ b

        cur = sz; sz += 1
        st[cur].length = st[last].length + 1; st[cur].occ = 1
        p = last
        while p != -1 and st[p].next[c] == -1:
            st[p].next[c] = cur; p = st[p].link
        if p == -1: st[cur].link = 0
        else:
            q = st[p].next[c]
            if st[p].length + 1 == st[q].length: st[cur].link = q
            else:
                clone = sz; sz += 1
                st[clone].next = st[q].next[:]; st[clone].link = st[q].link
                st[clone].length = st[p].length + 1; st[clone].occ = 0
                while p != -1 and st[p].next[c] == q:
                    st[p].next[c] = clone; p = st[p].link
                st[q].link = clone; st[cur].link = clone
        last = cur

    cnt_len = [0]*(n+1)
    for i in range(sz): cnt_len[st[i].length] += 1
    for i in range(1, n+1): cnt_len[i] += cnt_len[i-1]
    order = [0]*sz
    for i in range(sz-1, -1, -1):
        cnt_len[st[i].length] -= 1; order[cnt_len[st[i].length]] = i

    for i in range(sz-1, 0, -1):
        v = order[i]; p = st[v].link
        if p >= 0: st[p].occ += st[v].occ

    best = [0]*(n+1)
    for i in range(1, sz):
        o = st[i].occ
        if o <= n and st[i].length > best[o]: best[o] = st[i].length

    for k in range(n-1, 0, -1):
        if best[k] < best[k+1]: best[k] = best[k+1]

    return str(sum(v for v in best[1:] if v > 0))

if __name__ == '__main__':
    print(solve())
