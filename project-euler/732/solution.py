def ceil_div_by_sqrt2(hsum):
    target = hsum * hsum
    lo = 0
    hi = hsum
    while lo < hi:
        mid = lo + (hi - lo) // 2
        lhs = 2 * mid * mid
        if lhs >= target:
            hi = mid
        else:
            lo = mid + 1
    return lo

def solve():
    kMod = 1000000007
    n = 1000
    
    h = [0] * n
    l = [0] * n
    q = [0] * n
    
    pow5 = 1
    for idx in range(3 * n):
        if idx > 0:
            pow5 = (pow5 * 5) % kMod
            
        r = (pow5 % 101) + 50
        troll = idx // 3
        
        if idx % 3 == 0:
            h[troll] = r
        elif idx % 3 == 1:
            l[troll] = r
        else:
            q[troll] = r
            
    hsum = sum(h)
    ceil_h_over_sqrt2 = ceil_div_by_sqrt2(hsum)
    
    jobs = []
    max_deadline = 0
    for i in range(n):
        start_deadline = hsum + l[i] - ceil_h_over_sqrt2
        completion_deadline = start_deadline + h[i]
        jobs.append((completion_deadline, h[i], q[i]))
        if completion_deadline > max_deadline:
            max_deadline = completion_deadline
            
    jobs.sort(key=lambda x: (x[0], x[1]))
    
    kNeg = -1000000000
    dp = [kNeg] * (max_deadline + 1)
    dp[0] = 0
    
    for deadline, p, job_q in jobs:
        for t in range(deadline, p - 1, -1):
            prev = dp[t - p]
            if prev == kNeg:
                continue
            cand = prev + job_q
            if cand > dp[t]:
                dp[t] = cand
                
    best = max(dp)
    return str(best)

if __name__ == "__main__":
    print(solve())
