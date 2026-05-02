def solve_case(L, N, j):
    kRMod = 32745673
    kRSeed = 6563116
    kThreshold = 10000000

    r = kRSeed
    cumulative_gap = 0
    boundary = L - 10 - 20 * (j - 1)

    times = []
    
    for _ in range(1, N + 1):
        gap = (r % 1000) + 1
        cumulative_gap += gap
        
        eastward = r <= kThreshold
        t = (boundary - cumulative_gap) if eastward else (boundary + cumulative_gap)
        times.append(t)
        
        r = (r * r) % kRMod

    kth = N - j
    times.sort()
    return times[kth]

def solve():
    ans = solve_case(1000000000, 1000001, 500001)
    return str(ans)

if __name__ == '__main__':
    print(solve())
