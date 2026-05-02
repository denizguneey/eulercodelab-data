memo = {}

def prefix_counts(t, x):
    if t == 0 or x < 0: return (0, 0)
    if t == 1: return (1, 0)
    key = (t, x)
    if key in memo: return memo[key]
    
    if (t % 2) == 0:
        u = t // 2
        x1 = (x - 1) // 4
        x3 = (x - 3) // 4
        a_pos, a_neg = prefix_counts(u, x1)
        b_pos, b_neg = prefix_counts(u, x3)
        if (u % 2) == 0:
            res = (a_pos + b_pos, a_neg + b_neg)
        else:
            res = (a_pos + b_neg, a_neg + b_pos)
    else:
        u = t // 2
        x0 = x // 4
        x2 = (x - 2) // 4
        u0_p, u0_n = prefix_counts(u, x0)
        u2_p, u2_n = prefix_counts(u, x2)
        v0_p, v0_n = prefix_counts(u + 1, x0)
        v2_p, v2_n = prefix_counts(u + 1, x2)
        
        if (u % 2) == 1:
            res = (u2_p + v0_p, u0_n + v2_p)
        else:
            res = (u2_n + v0_p, u0_n + v2_n)
            
    memo[key] = res
    return res

def count_total(t, x):
    pos, neg = prefix_counts(t, x)
    return pos + neg

def g(t, c):
    if t == 0 or c == 0 or c > t: return 0
    lo = 0
    hi = 1
    while count_total(t, hi) < c:
        hi *= 2
    while lo < hi:
        mid = (lo + hi) // 2
        if count_total(t, mid) >= c:
            hi = mid
        else:
            lo = mid + 1
    return lo

def solve():
    memo.clear()
    fib = [0] * 46
    fib[0] = 1
    fib[1] = 1
    for i in range(2, 46):
        fib[i] = fib[i-1] + fib[i-2]
        
    total_val = 0
    for t in range(2, 46):
        total_val += g(fib[t], fib[t-1])
        
    return str(total_val)

if __name__ == '__main__':
    print(solve())
