# Problem 149: Searching for a maximum-sum subsequence

def solve():
    size = 2000
    total = size * size
    s = [0] * (total + 1)
    for k in range(1, 56):
        s[k] = (100003 - 200003*k + 300007*k*k*k) % 1000000 - 500000
    for k in range(56, total + 1):
        s[k] = (s[k-24] + s[k-55] + 1000000) % 1000000 - 500000
    
    def at(r, c):
        return s[r * size + c + 1]
    
    best = float('-inf')
    
    # Kadane's algorithm
    def kadane_update(v, cur):
        return max(v, cur + v)
    
    # Rows
    for r in range(size):
        cur = float('-inf')
        for c in range(size):
            cur = kadane_update(at(r, c), cur)
            if cur > best: best = cur
    
    # Columns
    for c in range(size):
        cur = float('-inf')
        for r in range(size):
            cur = kadane_update(at(r, c), cur)
            if cur > best: best = cur
    
    # Diagonal \ starting from row 0
    for cs in range(size):
        cur = float('-inf')
        r, c = 0, cs
        while r < size and c < size:
            cur = kadane_update(at(r, c), cur)
            if cur > best: best = cur
            r += 1; c += 1
    # Diagonal \ starting from col 0
    for rs in range(1, size):
        cur = float('-inf')
        r, c = rs, 0
        while r < size and c < size:
            cur = kadane_update(at(r, c), cur)
            if cur > best: best = cur
            r += 1; c += 1
    
    # Anti-diagonal / starting from row 0
    for cs in range(size):
        cur = float('-inf')
        r, c = 0, cs
        while r < size and c >= 0:
            cur = kadane_update(at(r, c), cur)
            if cur > best: best = cur
            r += 1; c -= 1
    # Anti-diagonal / starting from col size-1
    for rs in range(1, size):
        cur = float('-inf')
        r, c = rs, size - 1
        while r < size and c >= 0:
            cur = kadane_update(at(r, c), cur)
            if cur > best: best = cur
            r += 1; c -= 1
    
    print(best)

solve()
