# Problem 107: Minimal network
# Find the maximum saving by removing redundant edges (MST).

import os

def solve():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, '..', 'resources', 'documents', '0107_network.txt')
    with open(file_path) as f:
        lines = [line.strip() for line in f if line.strip()]
    
    n = len(lines)
    edges = []
    total_weight = 0
    for i in range(n):
        parts = lines[i].split(',')
        for j in range(i+1, n):
            if parts[j] != '-':
                w = int(parts[j])
                edges.append((w, i, j))
                total_weight += w
    
    # Kruskal's MST
    edges.sort()
    parent = list(range(n))
    rank = [0] * n
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry: return False
        if rank[rx] < rank[ry]: rx, ry = ry, rx
        parent[ry] = rx
        if rank[rx] == rank[ry]: rank[rx] += 1
        return True
    
    mst_weight = 0
    for w, u, v in edges:
        if union(u, v):
            mst_weight += w
    
    print(total_weight - mst_weight)

solve()
