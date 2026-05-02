import sys

# Set recursion limit high enough just in case, though max depth here is 32.
sys.setrecursionlimit(2000)

def solve(n=5):
    edge_count = 1 << n
    node_mask = (1 << (n - 1)) - 1
    
    used_edge = bytearray(edge_count)
    sequence = [0] * n
    used_edge[0] = 1
    
    total = [0]
    
    def dfs(node, used):
        if used == edge_count:
            if node != 0:
                return
            value = 0
            for i in range(edge_count):
                value = (value << 1) | sequence[i]
            total[0] += value
            return
            
        for bit in (0, 1):
            edge = ((node << 1) | bit) & (edge_count - 1)
            if used_edge[edge]:
                continue
            used_edge[edge] = 1
            sequence.append(bit)
            dfs(edge & node_mask, used + 1)
            sequence.pop()
            used_edge[edge] = 0
            
    dfs(0, 1)
    return str(total[0])

if __name__ == '__main__':
    print(solve())
