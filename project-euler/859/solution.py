class GameDB:
    def __init__(self):
        self.games = []
        self.intern = {}
        self.leq_cache = {}
        self.add_cache = {}
        self.win_cache = {}
        self.add_game([], [])

    def zero(self):
        return 0

    def dedup(self, v):
        return sorted(list(set(v)))

    def encode(self, L, R):
        return ",".join(map(str, L)) + "|" + ",".join(map(str, R))

    def pair_key(self, a, b):
        return (a << 32) | b

    def add_game(self, L, R):
        key = self.encode(L, R)
        if key in self.intern:
            return self.intern[key]
        idx = len(self.games)
        self.games.append((L, R))
        self.intern[key] = idx
        return idx

    def leq(self, g, h):
        key = self.pair_key(g, h)
        if key in self.leq_cache:
            return self.leq_cache[key]
            
        self.leq_cache[key] = True

        for gl in self.games[g][0]:
            if self.leq(h, gl):
                self.leq_cache[key] = False
                return False
                
        for hr in self.games[h][1]:
            if self.leq(hr, g):
                self.leq_cache[key] = False
                return False
                
        return True

    def canonical(self, L, R):
        L = self.dedup(L)
        R = self.dedup(R)

        changed = True
        while changed:
            changed = False

            keepL = []
            for i in range(len(L)):
                dominated = False
                for j in range(len(L)):
                    if i == j: continue
                    if self.leq(L[i], L[j]):
                        dominated = True
                        break
                if not dominated:
                    keepL.append(L[i])
            if len(keepL) != len(L):
                changed = True
            L = keepL

            keepR = []
            for i in range(len(R)):
                dominated = False
                for j in range(len(R)):
                    if i == j: continue
                    if self.leq(R[j], R[i]):
                        dominated = True
                        break
                if not dominated:
                    keepR.append(R[i])
            if len(keepR) != len(R):
                changed = True
            R = keepR

            gtemp = self.add_game(L, R)

            newL = []
            revL = False
            for a in L:
                AR = self.games[a][1]
                reversible = False
                for ar in AR:
                    if self.leq(ar, gtemp):
                        ARL = self.games[ar][0]
                        newL.extend(ARL)
                        reversible = True
                        revL = True
                        break
                if not reversible:
                    newL.append(a)
            if revL:
                L = self.dedup(newL)
                changed = True

            gtemp = self.add_game(L, R)

            newR = []
            revR = False
            for a in R:
                AL = self.games[a][0]
                reversible = False
                for al in AL:
                    if self.leq(gtemp, al):
                        ALR = self.games[al][1]
                        newR.extend(ALR)
                        reversible = True
                        revR = True
                        break
                if not reversible:
                    newR.append(a)
            if revR:
                R = self.dedup(newR)
                changed = True

        return self.add_game(L, R)

    def add(self, g, h):
        if g > h:
            g, h = h, g
        key = self.pair_key(g, h)
        if key in self.add_cache:
            return self.add_cache[key]

        L = []
        R = []

        for gl in self.games[g][0]: L.append(self.add(gl, h))
        for hl in self.games[h][0]: L.append(self.add(g, hl))
        for gr in self.games[g][1]: R.append(self.add(gr, h))
        for hr in self.games[h][1]: R.append(self.add(g, hr))

        res = self.canonical(L, R)
        self.add_cache[key] = res
        return res

    def win(self, g, turn):
        key = self.pair_key(g, turn)
        if key in self.win_cache:
            return self.win_cache[key]

        moves = self.games[g][0] if turn == 0 else self.games[g][1]
        if not moves:
            self.win_cache[key] = False
            return False

        for nxt in moves:
            if not self.win(nxt, 1 - turn):
                self.win_cache[key] = True
                return True

        self.win_cache[key] = False
        return False

    def cls(self, g):
        o = self.win(g, 0)
        e = self.win(g, 1)
        if o and e: return 'L'
        if not o and not e: return 'R'
        if o and not e: return 'N'
        return 'P'

def solve_C(N):
    db = GameDB()
    heap = [0] * (N + 1)
    heap[0] = db.zero()

    for n in range(1, N + 1):
        if n & 1:
            m = (n - 1) // 2
            x = db.add(heap[m], heap[m])
            heap[n] = db.canonical([x], [])
        else:
            m = (n - 2) // 2
            x = db.add(heap[m], heap[m])
            heap[n] = db.canonical([], [x])

    dp = [{} for _ in range(N + 1)]
    dp[0][db.zero()] = 1

    for size in range(1, N + 1):
        g = heap[size]
        for s in range(size, N + 1):
            if not dp[s - size]: continue
            for gid, cnt in dp[s - size].items():
                nxt = db.add(gid, g)
                dp[s][nxt] = dp[s].get(nxt, 0) + cnt

    ans = 0
    for gid, cnt in dp[N].items():
        c = db.cls(gid)
        if c == 'P' or c == 'R':
            ans += cnt
    return ans

def solve():
    return str(solve_C(300))

if __name__ == "__main__":
    print(solve())
