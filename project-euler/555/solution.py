def solve():
    p = 1000000
    m = 1000000
    total = 0
    for g in range(1, p + 1):
        tMax = p // g
        if tMax < 2: continue
        
        cnt = tMax - 1
        sum_t = tMax * (tMax + 1) // 2 - 1
        
        A1 = cnt * g * (m + g + 1)
        A2 = cnt * g * (g - 1) // 2
        B = g * g * sum_t
        total += A1 + A2 - B
    return str(total)

if __name__ == '__main__':
    print(solve())
