import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(2000000)

def solve():
    n = 20
    N = 1 << n
    kMod = 1001001011

    succ = [0] * N
    for x in range(N):
        b1 = x & 1
        b2 = (x >> 1) & 1
        b3 = (x >> 2) & 1
        last = b1 & (b2 ^ b3)
        succ[x] = (x >> 1) | (last << (n - 1))

    head = [-1] * N
    to = [0] * N
    next_edge = [-1] * N
    
    # We build the reverse graph to find trees attaching to cycles
    for v in range(N):
        u = succ[v]
        to[v] = v
        next_edge[v] = head[u]
        head[u] = v

    color = [0] * N
    pos = [-1] * N
    in_cycle = [0] * N
    cycles = []
    
    for start in range(N):
        if color[start] != 0:
            continue
            
        path = []
        v = start
        while color[v] == 0:
            color[v] = 1
            pos[v] = len(path)
            path.append(v)
            v = succ[v]
            
        if color[v] == 1:
            cycle_start = pos[v]
            cyc = []
            for i in range(cycle_start, len(path)):
                node = path[i]
                in_cycle[node] = 1
                cyc.append(node)
            cycles.append(cyc)
            
        for node in path:
            color[node] = 2
            pos[node] = -1

    dp0 = [0] * N
    dp1 = [0] * N
    done = [0] * N

    def compute_tree(root):
        if done[root]:
            return
            
        st = [(root, False)]
        while st:
            u, expanded = st.pop()
            if not expanded:
                st.append((u, True))
                e = head[u]
                while e != -1:
                    ch = to[e]
                    if not in_cycle[ch]:
                        if not done[ch]:
                            st.append((ch, False))
                    e = next_edge[e]
            else:
                ways0 = 1
                ways1 = 1
                e = head[u]
                while e != -1:
                    ch = to[e]
                    if not in_cycle[ch]:
                        sm = (dp0[ch] + dp1[ch]) % kMod
                        ways0 = (ways0 * sm) % kMod
                        ways1 = (ways1 * dp0[ch]) % kMod
                    e = next_edge[e]
                    
                dp0[u] = ways0
                dp1[u] = ways1
                done[u] = 1

    answer = 1
    
    for cyc in cycles:
        m = len(cyc)
        w0 = [1] * m
        w1 = [1] * m
        
        for i in range(m):
            u = cyc[i]
            a0 = 1
            a1 = 1
            
            e = head[u]
            while e != -1:
                ch = to[e]
                if not in_cycle[ch]:
                    compute_tree(ch)
                    a0 = (a0 * (dp0[ch] + dp1[ch])) % kMod
                    a1 = (a1 * dp0[ch]) % kMod
                e = next_edge[e]
                
            w0[i] = a0
            w1[i] = a1
            
        component_count = 0
        if m == 1:
            component_count = w0[0]
        else:
            dp_prev0 = w0[0]
            dp_prev1 = 0
            for i in range(1, m):
                ndp0 = ((dp_prev0 + dp_prev1) * w0[i]) % kMod
                ndp1 = (dp_prev0 * w1[i]) % kMod
                dp_prev0 = ndp0
                dp_prev1 = ndp1
            component_count = (component_count + dp_prev0 + dp_prev1) % kMod
            
            dp_prev0 = 0
            dp_prev1 = w1[0]
            for i in range(1, m):
                ndp0 = ((dp_prev0 + dp_prev1) * w0[i]) % kMod
                ndp1 = (dp_prev0 * w1[i]) % kMod
                dp_prev0 = ndp0
                dp_prev1 = ndp1
                
            component_count = (component_count + dp_prev0) % kMod
            
        answer = (answer * component_count) % kMod

    return str(answer)

if __name__ == '__main__':
    print(solve())
