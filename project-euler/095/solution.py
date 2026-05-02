# Problem 95: Amicable chains
# Find the smallest member of the longest amicable chain with no element > 1,000,000.

def solve():
    limit = 1000000
    # Compute proper divisor sums
    s = [0] * (limit + 1)
    for i in range(1, limit + 1):
        for j in range(2 * i, limit + 1, i):
            s[j] += i
    
    done = [False] * (limit + 1)
    best_len, best_min = 0, 0
    
    for start in range(2, limit + 1):
        if done[start]:
            continue
        path = []
        index = {}
        n = start
        while 1 <= n <= limit and n not in index and not done[n]:
            index[n] = len(path)
            path.append(n)
            n = s[n]
        
        if 1 <= n <= limit and n in index:
            loop_start = index[n]
            loop_len = len(path) - loop_start
            min_member = min(path[loop_start:])
            if loop_len > best_len or (loop_len == best_len and min_member < best_min):
                best_len = loop_len
                best_min = min_member
        
        for v in path:
            done[v] = True
    
    print(best_min)

solve()
