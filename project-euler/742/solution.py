import math
import functools

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def cmp_edges(a, b):
    lhs = a[0] * b[1]
    rhs = b[0] * a[1]
    if lhs < rhs: return -1
    elif lhs > rhs: return 1
    return 0

def get_edge_candidates(num_edges):
    primitive = [[0] * (num_edges + 1) for _ in range(num_edges + 1)]
    for y in range(1, num_edges + 1):
        for x in range(1, y):
            if gcd(x, y) == 1:
                primitive[y][x] = 1
                
    pref = [[0] * (num_edges + 1) for _ in range(num_edges + 1)]
    for y in range(1, num_edges + 1):
        row = 0
        for x in range(1, num_edges + 1):
            row += primitive[y][x]
            pref[y][x] = pref[y - 1][x] + row
            
    edges = []
    for y in range(1, num_edges + 1):
        for x in range(1, y):
            if not primitive[y][x]:
                continue
            count_smaller_edges = pref[y][x]
            if 2 + count_smaller_edges > num_edges:
                break
            edges.append((x, y))
            
    edges.sort(key=functools.cmp_to_key(cmp_edges))
    return edges

def filter_convex_hull(domain):
    domain.sort()
    out = []
    
    for s, a in domain:
        if out and out[-1][0] == s:
            continue
            
        while len(out) >= 2:
            s1, a1 = out[-1]
            s2, a2 = out[-2]
            
            lhs = (a - a1) * (s - s2)
            rhs = (a - a2) * (s - s1)
            
            if lhs >= rhs:
                break
            out.pop()
            
        if out and out[-1][1] <= a:
            continue
            
        out.append((s, a))
        
    return out

def combine_convex_hulls(d0, d1):
    merged = []
    i = 0
    j = 0
    while i < len(d0) and j < len(d1):
        if d0[i] <= d1[j]:
            merged.append(d0[i])
            i += 1
        else:
            merged.append(d1[j])
            j += 1
            
    while i < len(d0):
        merged.append(d0[i])
        i += 1
    while j < len(d1):
        merged.append(d1[j])
        j += 1
        
    return filter_convex_hull(merged)

def update_sa_domain(domain, edge):
    out = []
    x, y = edge
    for s, a in domain:
        ns = s + 2 * y
        na = a + 2 * x * (s + y)
        out.append((ns, na))
    return out

def solve():
    num_edges = 1000
    if num_edges < 4 or num_edges % 4 != 0:
        return "-1"
        
    q_edges = num_edges // 4
    if q_edges == 1:
        return "1"
        
    domain = [[] for _ in range(q_edges + 1)]
    domain[1].append((1, 0))
    
    edges = get_edge_candidates(q_edges)
    
    for edge in edges:
        for used in range(q_edges - 1, 0, -1):
            if not domain[used]:
                continue
            with_new = update_sa_domain(domain[used], edge)
            domain[used + 1] = combine_convex_hulls(domain[used + 1], with_new)
            
    best = 1 << 62
    for left in range(1, q_edges):
        d0 = domain[left]
        d1 = domain[q_edges - left]
        for s0, a0 in d0:
            for s1, a1 in d1:
                val = a0 + a1 + (s0 + 2) * (s1 + 2) - 2
                if val < best:
                    best = val
                    
    return str(best)

if __name__ == "__main__":
    print(solve())
