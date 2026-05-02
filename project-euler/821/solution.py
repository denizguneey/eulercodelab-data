def count_coprime6(x):
    if x <= 0:
        return 0
    return x - x // 2 - x // 3 + x // 6

def generate_smooth(N):
    v = []
    p2 = 1
    while p2 <= N:
        cur = p2
        while cur <= N:
            v.append(cur)
            if cur > N // 3:
                break
            cur *= 3
        if p2 > N // 2:
            break
        p2 *= 2
    return sorted(list(set(v)))

def generate_bad(N):
    b = []
    def push_if(x):
        if x <= N:
            b.append(x)
            
    push_if(6)
    push_if(24)
    push_if(54)
    
    x = 384
    while x <= N:
        b.append(x)
        if x > N // 8:
            break
        x *= 8
        
    x = 243
    while x <= N:
        b.append(x)
        if x > N // 27:
            break
        x *= 27
        
    return sorted(list(set(b)))

def solve_fast(N):
    smooth = generate_smooth(N)
    bad = generate_bad(N)
    
    fAt = [0] * len(smooth)
    ib = 0
    f = 0
    for i in range(len(smooth)):
        if ib < len(bad) and smooth[i] == bad[ib]:
            ib += 1
        else:
            f += 1
        fAt[i] = f
        
    ans = 0
    n = len(smooth)
    for i in range(n):
        L = smooth[i]
        R = smooth[i + 1] - 1 if i + 1 < n else N
        if R > N:
            R = N
            
        mLow = N // (R + 1) + 1
        mHigh = N // L
        if mLow > mHigh:
            continue
            
        cnt = count_coprime6(mHigh) - count_coprime6(mLow - 1)
        ans += fAt[i] * cnt
        
    return ans

def solve():
    ans = solve_fast(10000000000000000)
    return str(ans)

if __name__ == "__main__":
    print(solve())
