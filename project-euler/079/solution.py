# Problem 79: Passcode derivation
# Analyse the login keylog to determine the shortest possible secret passcode.

import os
from collections import defaultdict, deque

def solve():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, '..', 'resources', 'documents', '0079_keylog.txt')
    
    with open(file_path) as f:
        logs = [line.strip() for line in f if line.strip()]
    
    digits = set()
    edges = defaultdict(set)
    for log in logs:
        for c in log:
            digits.add(c)
        for i in range(len(log) - 1):
            edges[log[i]].add(log[i+1])
    
    # Topological sort
    in_degree = defaultdict(int)
    for d in digits:
        in_degree[d] += 0
    for u in edges:
        for v in edges[u]:
            in_degree[v] += 1
    
    queue = deque([d for d in digits if in_degree[d] == 0])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for v in sorted(edges[node]):
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    print(''.join(result))

solve()
