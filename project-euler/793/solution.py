MOD = 50515093

def build_values(n):
    a = [0] * n
    s = 290797
    for i in range(n):
        a[i] = s
        s = (s * s) % MOD
    a.sort()
    return a

def count_pairs_leq(a, x):
    n = len(a)
    j = n - 1
    cnt = 0
    
    for i in range(n):
        while i < j and a[i] * a[j] > x:
            j -= 1
        if j <= i:
            break
        cnt += j - i
        
    return cnt

def solve_n(n):
    a = build_values(n)
    
    m = n * (n - 1) // 2
    target = (m + 1) // 2
    
    lo = 0
    hi = a[n - 1] * a[n - 2]
    
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if count_pairs_leq(a, mid) >= target:
            hi = mid
        else:
            lo = mid + 1
            
    return lo

def solve():
    return str(solve_n(1000003))

if __name__ == "__main__":
    print(solve())
