def max_seed(limit):
    lo = 0
    hi = 1
    def seed_first_area(p):
        return 8 * p * p * p + p
        
    while seed_first_area(hi) <= limit:
        hi *= 2
        
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if seed_first_area(mid) <= limit:
            lo = mid
        else:
            hi = mid - 1
    return lo

def sum_for_seed(seed, limit):
    total = 0
    stack = [(seed, 0, seed)]
    
    while stack:
        p, q, area = stack.pop()
        
        p2 = p * p
        a = 8 * p2 + 1
        b = 4 * p
        c = 4 * p * (4 * p2 + 1)
        
        q1 = a * q + b * area
        s1 = c * q + a * area
        
        if s1 > 0 and s1 <= limit:
            total += s1
            stack.append((p, q1, s1))
            stack.append((q1, p, s1))
            stack.append((q1, -p, s1))
            
    return total

def solve():
    limit = 10000000000
    pmax = max_seed(limit)
    if pmax <= 0: return "0"
    
    ans = 0
    for seed in range(1, pmax + 1):
        ans += sum_for_seed(seed, limit)
        
    return str(ans)

if __name__ == '__main__':
    print(solve())
