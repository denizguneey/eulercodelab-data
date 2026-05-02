import math
import sys
from collections import deque

sys.setrecursionlimit(20000)

class Edge:
    __slots__ = ['to', 'rev', 'cap']
    def __init__(self, to, rev, cap):
        self.to = to
        self.rev = rev
        self.cap = cap

class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.level = [-1] * n
        self.it = [0] * n

    def add_edge(self, u, v, cap):
        self.graph[u].append(Edge(v, len(self.graph[v]), cap))
        self.graph[v].append(Edge(u, len(self.graph[u]) - 1, 0.0))

    def bfs(self, s, t):
        for i in range(self.n):
            self.level[i] = -1
        self.level[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            for e in self.graph[v]:
                if e.cap > 1e-12 and self.level[e.to] < 0:
                    self.level[e.to] = self.level[v] + 1
                    q.append(e.to)
        return self.level[t] >= 0

    def dfs(self, v, t, f):
        if v == t: return f
        for i in range(self.it[v], len(self.graph[v])):
            self.it[v] = i
            e = self.graph[v][i]
            if e.cap <= 1e-12 or self.level[e.to] != self.level[v] + 1:
                continue
            got = self.dfs(e.to, t, min(f, e.cap))
            if got > 1e-12:
                e.cap -= got
                self.graph[e.to][e.rev].cap += got
                return got
        return 0.0

    def max_flow(self, s, t):
        flow = 0.0
        while self.bfs(s, t):
            for i in range(self.n):
                self.it[i] = 0
            while True:
                f = self.dfs(s, t, float('inf'))
                if f <= 1e-12: break
                flow += f
        return flow

def sieve_primes(n):
    spf = list(range(n + 1))
    for i in range(2, int(math.sqrt(n)) + 1):
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
    primes = [i for i in range(2, n + 1) if spf[i] == i]
    return primes

def solve_ln(n):
    primes = sieve_primes(n)
    
    a7 = []
    b9 = []
    mandatory_log = 0.0
    for p in primes:
        r = p % 10
        if r == 3: mandatory_log += math.log(p)
        if r == 7: a7.append(p)
        if r == 9: b9.append(p)
        
    forced = [False] * (n + 1)
    forced_log = 0.0
    for p in a7:
        cube = p * p * p
        if cube <= n:
            forced[p] = True
            forced_log += math.log(p)
            
    nonforced_a = [p for p in a7 if not forced[p]]
    
    edges = []
    used_a = [False] * (n + 1)
    used_b = [False] * (n + 1)
    
    import bisect
    for a in nonforced_a:
        limit = n // a
        idx = bisect.bisect_right(b9, limit)
        for i in range(idx):
            b = b9[i]
            edges.append((a, b))
            used_a[a] = True
            used_b[b] = True
            
    cover_log = 0.0
    if edges:
        id_a = [-1] * (n + 1)
        id_b = [-1] * (n + 1)
        node_count = 1
        
        for a in nonforced_a:
            if used_a[a]:
                id_a[a] = node_count
                node_count += 1
                
        for b in b9:
            if used_b[b]:
                id_b[b] = node_count
                node_count += 1
                
        source = 0
        sink = node_count
        node_count += 1
        
        dinic = Dinic(node_count)
        inf_cap = 1e30
        
        for a in nonforced_a:
            if used_a[a]:
                dinic.add_edge(source, id_a[a], math.log(a))
                
        for b in b9:
            if used_b[b]:
                dinic.add_edge(id_b[b], sink, math.log(b))
                
        for u, v in edges:
            dinic.add_edge(id_a[u], id_b[v], inf_cap)
            
        cover_log = dinic.max_flow(source, sink)
        
    return mandatory_log + forced_log + cover_log

def solve():
    ans = solve_ln(1000000)
    ans = round(ans * 1000000) / 1000000
    return f"{ans:.6f}"

if __name__ == "__main__":
    print(solve())
