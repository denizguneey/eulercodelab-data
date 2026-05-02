def solve():
    kMod = 1000000007
    h = 10000
    w = 20000
    
    hw = ((h % kMod) * (w % kMod)) % kMod
    p2h = pow(2, h, kMod)
    p2w = pow(2, w, kMod)
    p2hw = pow(2, h + w, kMod)
    
    t0 = (9 * p2hw) % kMod
    
    c1 = (2 * hw - 8 * (w % kMod) - 10) % kMod
    t1 = (c1 * p2h) % kMod
    
    c2 = (2 * hw - 8 * (h % kMod) - 10) % kMod
    t2 = (c2 * p2w) % kMod
    
    t3 = (2 * hw + 10 * (h % kMod) + 10 * (w % kMod) + 10) % kMod
    
    ans = (t0 + t1 + t2 + t3) % kMod
    return str(ans)

if __name__ == "__main__":
    print(solve())
