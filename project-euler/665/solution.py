import heapq

def solve():
    M = 10000000

    # Successor set (union-find style)
    class SSet:
        def __init__(self): self.par = {}
        def next_free(self, v):
            if v not in self.par: return v
            self.par[v] = self.next_free(self.par[v])
            return self.par[v]
        def insert(self, v):
            if v in self.par: return
            self.par[v] = self.next_free(v+1)

    used = SSet(); dif_set = SSet(); low_set = SSet()
    he_set = SSet(); ho_set = SSet()
    pending = []  # min-heap on activate_x

    def insert_s(s):
        if s % 2 == 0: he_set.insert(s//2)
        else: ho_set.insert((s-1)//2)

    dif_set.insert(0); low_set.insert(0); insert_s(0)

    def activate(x):
        while pending and pending[0][0] <= x:
            _, tv, sv = heapq.heappop(pending)
            low_set.insert(tv); insert_s(sv)

    total = 0; x = 1
    while x <= M:
        activate(x); x = used.next_free(x)
        if x > M: break
        y = x + 1
        while True:
            y1 = used.next_free(y)
            y2 = x + dif_set.next_free(y1 - x)
            y3 = 2*x + low_set.next_free(y2 - 2*x)
            shift = x//2 if x%2==0 else x//2+1
            if x%2==0: y4 = shift + he_set.next_free(y3-shift)
            else: y4 = shift + ho_set.next_free(y3-shift)
            if y4 == y: break
            y = y4

        used.insert(x); used.insert(y)
        if x+y <= M: total += x+y
        dif_set.insert(y-x); low_set.insert(y-2*x); insert_s(2*y-x)
        heapq.heappush(pending, (y+1, x-2*y, 2*x-y))
        x += 1

    return str(total)

if __name__ == '__main__':
    print(solve())
