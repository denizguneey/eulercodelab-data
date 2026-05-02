# Problem 83: Path sum: four ways
# Find the minimal path sum from top-left to bottom-right (any direction).

import os, heapq

def solve():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, '..', 'resources', 'documents', '0083_matrix.txt')
    with open(file_path) as f:
        matrix = [list(map(int, line.strip().split(','))) for line in f if line.strip()]
    n = len(matrix)
    dist = [[float('inf')] * n for _ in range(n)]
    dist[0][0] = matrix[0][0]
    pq = [(matrix[0][0], 0, 0)]
    while pq:
        d, i, j = heapq.heappop(pq)
        if d > dist[i][j]: continue
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < n:
                nd = d + matrix[ni][nj]
                if nd < dist[ni][nj]:
                    dist[ni][nj] = nd
                    heapq.heappush(pq, (nd, ni, nj))
    print(dist[-1][-1])

solve()
