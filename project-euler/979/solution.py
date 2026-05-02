import sys

class Node:
    __slots__ = ['layer', 'parent_count', 'adj']
    def __init__(self, layer, parent_count):
        self.layer = layer
        self.parent_count = parent_count
        self.adj = []

def build_graph(max_layer):
    graph = []
    
    def add_node(layer, parent_count):
        graph.append(Node(layer, parent_count))
        return len(graph) - 1
        
    def add_edge(u, v):
        graph[u].adj.append(v)
        graph[v].adj.append(u)
        
    root = add_node(0, 0)
    boundary = [root] * 7
    
    for depth in range(max_layer):
        n = len(boundary)
        generated = [-1] * n
        consumed = [False] * n
        
        for i in range(n):
            j = (i + 1) % n
            if consumed[i] or consumed[j]:
                continue
            if boundary[i] != boundary[j]:
                nid = add_node(depth + 1, 2)
                add_edge(nid, boundary[i])
                add_edge(nid, boundary[j])
                generated[i] = nid
                generated[j] = nid
                consumed[i] = True
                consumed[j] = True
                
        for i in range(n):
            if consumed[i]:
                continue
            nid = add_node(depth + 1, 1)
            add_edge(nid, boundary[i])
            generated[i] = nid
            consumed[i] = True
            
        new_layer = []
        for i in range(n):
            if i == 0 or generated[i] != generated[i - 1]:
                new_layer.append(generated[i])
                
        if len(new_layer) > 1 and new_layer[0] == new_layer[-1]:
            new_layer.pop()
            
        m = len(new_layer)
        for i in range(m):
            add_edge(new_layer[i], new_layer[(i + 1) % m])
            
        next_boundary = []
        for id in new_layer:
            out_edges = 4 if graph[id].parent_count == 1 else 3
            next_boundary.extend([id] * out_edges)
            
        boundary = next_boundary
        
    return graph

def step_counts(graph, cur):
    n = len(graph)
    nxt = [0] * n
    for i in range(n):
        s = 0
        for v in graph[i].adj:
            s += cur[v]
        nxt[i] = s
    return nxt

def check_value(step, got, expected):
    if got == expected:
        return True
    return False

def solve_impl(steps):
    validate_steps = 4
    build_steps = max(steps, validate_steps)
    max_layer = build_steps // 2
    
    graph = build_graph(max_layer)
    cur = [0] * len(graph)
    cur[0] = 1
    
    ok = True
    answer = 1 if steps == 0 else 0
    
    for step in range(1, build_steps + 1):
        cur = step_counts(graph, cur)
        
        if step == steps:
            answer = cur[0]
        if step == 2:
            ok &= check_value(step, cur[0], 7)
        if step == 3:
            ok &= check_value(step, cur[0], 14)
        if step == 4:
            ok &= check_value(step, cur[0], 119)
            
    if not ok:
        print("Validation failed", file=sys.stderr)
        sys.exit(1)
        
    return answer

def solve():
    return str(solve_impl(20))

if __name__ == "__main__":
    print(solve())
