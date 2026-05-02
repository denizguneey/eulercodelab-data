def build_grundy(limit):
    g = [0] * (limit + 1)
    seen = [-1] * 512
    
    for n in range(1, limit + 1):
        k = 1
        while k * k <= n:
            val = g[n - k * k]
            if val >= len(seen):
                seen.extend([-1] * (val + 64))
            seen[val] = n
            k += 1
            
        while seen[g[n]] == n:
            g[n] += 1
            
    return g

def solve(limit=100000):
    g = build_grundy(limit)
    max_g = max(g)
    
    prefix = [0] * (max_g + 1)
    suffix = [0] * (max_g + 1)
    
    for n in range(limit + 1):
        suffix[g[n]] += 1
        
    answer = 0
    for b in range(limit + 1):
        gb = g[b]
        prefix[gb] += 1
        
        for ga in range(max_g + 1):
            gc = ga ^ gb
            if gc > max_g:
                continue
            answer += prefix[ga] * suffix[gc]
            
        suffix[gb] -= 1
        
    return str(answer)

if __name__ == '__main__':
    print(solve())
