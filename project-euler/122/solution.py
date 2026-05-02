# Problem 122: Efficient exponentiation
# Find shortest addition chain for each k up to 200.

def solve():
    limit = 200
    best = [float('inf')] * (limit + 1)
    best[1] = 0
    
    def dfs(chain, max_depth):
        depth = len(chain) - 1
        if depth >= max_depth: return
        last = chain[-1]
        for i in range(depth, -1, -1):
            nxt = last + chain[i]
            if nxt > limit or nxt <= last: continue
            if depth + 1 > best[nxt]: continue
            if depth + 1 < best[nxt]:
                best[nxt] = depth + 1
            chain.append(nxt)
            dfs(chain, max_depth)
            chain.pop()
    
    for max_depth in range(1, 16):
        dfs([1], max_depth)
        if all(best[k] < float('inf') for k in range(1, limit + 1)):
            break
    
    print(sum(best[k] for k in range(1, limit + 1)))

solve()
