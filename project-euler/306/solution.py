def compute_grundy(n):
    grundy = [0] * (n + 1)
    seen = [-1] * 2048
    
    for length in range(1, n + 1):
        for left in range((length - 2) // 2 + 1):
            right = length - 2 - left
            value = grundy[left] ^ grundy[right]
            seen[value] = length
            
        while seen[grundy[length]] == length:
            grundy[length] += 1
            
    return grundy

def solve(limit=1000000):
    prefix = 100
    period = 34
    max_precompute = max(prefix + period, 1200)
    g = compute_grundy(max_precompute)
    
    wins = 0
    for length in range(1, limit + 1):
        if length <= prefix:
            sg = g[length]
        else:
            sg = g[(length - prefix) % period + prefix]
        if sg != 0:
            wins += 1
            
    return str(wins)

if __name__ == '__main__':
    print(solve())
